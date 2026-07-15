"""Solução de referência — Exercício 1 da Lição 032.

Constrói um vocabulário ordenado a partir de um corpus e vetoriza cada
documento como um vetor de contagens (bag-of-words), do zero.
"""

corpus = [
    "o gato dorme",
    "o cachorro corre",
    "o gato corre",
]


def tokenizar(texto):
    return texto.lower().split()


def construir_vocabulario(corpus):
    vocab = set()
    for doc in corpus:
        vocab.update(tokenizar(doc))
    return sorted(vocab)


def bag_of_words(doc, vocab):
    indice = {termo: i for i, termo in enumerate(vocab)}
    vetor = [0] * len(vocab)
    for tok in tokenizar(doc):
        vetor[indice[tok]] += 1
    return vetor


vocab = construir_vocabulario(corpus)
print(f"vocabulario: {vocab}")
for doc in corpus:
    print(f"{doc!r} -> {bag_of_words(doc, vocab)}")
