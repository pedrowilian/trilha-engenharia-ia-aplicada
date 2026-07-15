"""Exercício 3 — Round-trip: ida-e-volta texto -> ids -> texto (igualdade exata).

Setup:
    textos = ["busca vetorial é incrível", "RAG: tokens -> ids -> tokens"]
    ESPACO = "\\u2581"   # metasímbolo '▁' que codifica o espaço (SentencePiece)

Tarefa:
    1. Construa um vocabulário determinístico de caracteres (espaços -> '▁').
    2. Implemente tokenizar(texto) -> lista de ids e destokenizar(ids) -> texto.
    3. Verifique a propriedade de IDA-E-VOLTA: destokenizar(tokenizar(t)) == t,
       byte a byte, e que um 2o parse produz os MESMOS ids.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/033-tokenizacao/solucao_3.saida.txt
    (todo texto com "igual ao original: True" e final "round-trip OK").
"""

ESPACO = "\u2581"
textos = ["busca vetorial é incrível", "RAG: tokens -> ids -> tokens"]

# TODO: construir vocab, tokenizar/destokenizar e provar o round-trip exato.
