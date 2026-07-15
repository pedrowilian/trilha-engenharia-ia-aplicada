"""Solucao de referencia - Exercicio 1 da Licao 059.

Recuperacao esparsa com BM25: pontua cada documento pela soma, sobre os termos da
consulta, do IDF (raridade do termo) ponderado pela frequencia do termo no
documento com saturacao (k1) e normalizacao por comprimento (b).
"""
import collections
import math
import re


corpus = {
    "d1": "o gato preto dorme",
    "d2": "o cachorro corre no parque",
    "d3": "o gato e o cachorro brincam",
}


def tok(t):
    return re.findall(r"[a-z0-9]+", t.lower())


docs = {d: tok(corpus[d]) for d in corpus}
N = len(docs)
avgdl = sum(len(v) for v in docs.values()) / N
df = collections.Counter()
for v in docs.values():
    for t in set(v):
        df[t] += 1


def idf(t):
    n = df.get(t, 0)
    return math.log(1 + (N - n + 0.5) / (n + 0.5))


def bm25(query, d, k1=1.5, b=0.75):
    tf = collections.Counter(docs[d])
    dl = len(docs[d])
    score = 0.0
    for t in tok(query):
        if t not in df:
            continue
        f = tf[t]
        score += idf(t) * (f * (k1 + 1)) / (f + k1 * (1 - b + b * dl / avgdl))
    return score


query = "gato cachorro"
for d in sorted(corpus):
    print(f"{d} {bm25(query, d):.4f}")
