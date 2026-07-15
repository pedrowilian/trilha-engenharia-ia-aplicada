"""Solução de referência — Exercício 2 da Lição 033.

Tokenização estilo WordPiece: dado um vocabulário de subpalavras (com prefixo
'##' para continuações), segmenta cada palavra pelo maior prefixo que está no
vocabulário (greedy longest-match). Se não for possível, devolve '[UNK]'.
"""

vocab = {"un", "happy", "##happy", "play", "##ing", "##ed", "##ness", "##ly"}


def wordpiece(palavra, vocab):
    tokens = []
    inicio = 0
    while inicio < len(palavra):
        fim = len(palavra)
        encontrado = None
        while fim > inicio:
            sub = palavra[inicio:fim]
            candidato = sub if inicio == 0 else "##" + sub
            if candidato in vocab:
                encontrado = candidato
                break
            fim -= 1
        if encontrado is None:
            return ["[UNK]"]
        tokens.append(encontrado)
        inicio = fim
    return tokens


for palavra in ["unhappy", "playing", "playedly", "xyz"]:
    print(f"{palavra:>8} -> {wordpiece(palavra, vocab)}")
