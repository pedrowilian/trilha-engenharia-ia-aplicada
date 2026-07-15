"""Exercício 2 — Segmentação WordPiece (greedy longest-match).

Setup:
    vocab = {"un", "happy", "##happy", "play", "##ing", "##ed", "##ness", "##ly"}
    palavras = ["unhappy", "playing", "playedly", "xyz"]

Tarefa:
    Implemente wordpiece(palavra, vocab) que casa o MAIOR prefixo do
    vocabulário (continuações com prefixo "##") e devolve ["[UNK]"] quando
    nenhum pedaço inicial casa. Imprima cada palavra e seus tokens.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/033-tokenizacao/solucao_2.saida.txt
"""

vocab = {"un", "happy", "##happy", "play", "##ing", "##ed", "##ness", "##ly"}
palavras = ["unhappy", "playing", "playedly", "xyz"]

# TODO: implementar wordpiece(palavra, vocab) e imprimir os tokens de cada palavra.
