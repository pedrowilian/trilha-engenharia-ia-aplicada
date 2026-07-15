"""Exercício 1 — Vetorizador bag-of-words do zero.

Setup:
    corpus = ["o gato dorme", "o cachorro corre", "o gato corre"]

Tarefa:
    1. Construa o vocabulário ORDENADO (termos distintos do corpus).
    2. Implemente bag_of_words(doc, vocab) -> lista de contagens.
    3. Imprima o vocabulário e o vetor de contagens de cada documento, p.ex.:
        vocabulario: ['cachorro', 'corre', 'dorme', 'gato', 'o']
        'o gato dorme' -> [0, 0, 1, 1, 1]
        ...

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/032-nlp-fundamentos/solucao_1.saida.txt
"""

corpus = [
    "o gato dorme",
    "o cachorro corre",
    "o gato corre",
]

# TODO: tokenizar, construir o vocabulário ordenado e vetorizar cada documento.
