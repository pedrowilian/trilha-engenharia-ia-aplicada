"""Solução de referência — Exercício 2 da Lição 032.

Calcula TF-IDF (com IDF suavizado) de termos selecionados sobre um corpus
pequeno, do zero, usando apenas a biblioteca padrão.

Definições usadas:
    tf(t, d)  = contagem de t em d / total de tokens em d
    idf(t)    = ln((1 + N) / (1 + df(t))) + 1     (idf suavizado)
    tfidf     = tf * idf
"""
import math

corpus = [
    "o gato dorme",
    "o cachorro corre",
    "o gato corre",
]


def tokenizar(texto):
    return texto.lower().split()


def doc_freq(termo, corpus):
    return sum(1 for doc in corpus if termo in tokenizar(doc))


def idf(termo, corpus):
    n = len(corpus)
    return math.log((1 + n) / (1 + doc_freq(termo, corpus))) + 1


def tf(termo, doc):
    toks = tokenizar(doc)
    return toks.count(termo) / len(toks)


def tfidf(termo, doc, corpus):
    return tf(termo, doc) * idf(termo, corpus)


doc = corpus[0]  # "o gato dorme"
for termo in ["o", "gato", "dorme"]:
    print(f"{termo:>6}: df={doc_freq(termo, corpus)} "
          f"idf={idf(termo, corpus):.4f} tfidf={tfidf(termo, doc, corpus):.4f}")
