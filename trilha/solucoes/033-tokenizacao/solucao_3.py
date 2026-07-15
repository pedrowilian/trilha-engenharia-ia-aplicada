"""Solução de referência — Exercício 3 da Lição 033 (ROUND-TRIP / ida-e-volta).

Demonstra um tokenizador REVERSÍVEL no estilo SentencePiece: o espaço é
codificado pelo metasímbolo '▁', o texto vira uma lista de IDs inteiros e a
decodificação reconstrói o texto ORIGINAL com IGUALDADE EXATA.

Propriedade verificada (R3.6):  destokenizar(tokenizar(texto)) == texto
e, em forma de ida-e-volta texto -> ids -> texto, o segundo parse iguala o
primeiro.
"""

ESPACO = "\u2581"  # '▁' — metasímbolo de espaço do SentencePiece


def construir_vocab(textos):
    """Vocabulário determinístico: todos os caracteres (com espaços já
    codificados como '▁') ordenados, mapeados a IDs estáveis."""
    chars = set()
    for t in textos:
        chars.update(t.replace(" ", ESPACO))
    return {c: i for i, c in enumerate(sorted(chars))}


def tokenizar(texto, vocab):
    """texto -> lista de IDs (1 ID por caractere; espaço vira '▁')."""
    return [vocab[c] for c in texto.replace(" ", ESPACO)]


def destokenizar(ids, inv_vocab):
    """lista de IDs -> texto, desfazendo o metasímbolo de espaço."""
    return "".join(inv_vocab[i] for i in ids).replace(ESPACO, " ")


textos = ["busca vetorial é incrível", "RAG: tokens -> ids -> tokens"]
vocab = construir_vocab(textos)
inv_vocab = {i: c for c, i in vocab.items()}

print(f"tamanho do vocabulario: {len(vocab)}")
for texto in textos:
    ids = tokenizar(texto, vocab)
    reconstruido = destokenizar(ids, inv_vocab)
    # Ida-e-volta: parse -> serialize -> parse com igualdade exata.
    ids_2 = tokenizar(reconstruido, vocab)
    print(f"texto:        {texto!r}")
    print(f"num ids:      {len(ids)}")
    print(f"reconstruido: {reconstruido!r}")
    print(f"igual ao original: {reconstruido == texto}")
    print(f"ids estaveis (2o parse igual): {ids_2 == ids}")

assert all(destokenizar(tokenizar(t, vocab), inv_vocab) == t for t in textos)
print("round-trip OK")
