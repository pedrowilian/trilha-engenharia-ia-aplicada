"""Solucao de referencia - Exercicio 2 da Licao 059.

Complementaridade denso x esparso: cada documento tem um texto (para o BM25
lexical) e um embedding (para o denso semantico). Para uma consulta cuja
parafrase casa semanticamente com um documento e cujo termo exato casa com outro,
os dois rankings divergem no topo - exatamente o que motiva a fusao hibrida.
"""
import collections
import math
import re

import numpy as np


corpus = {
    "d1": {"texto": "politica de reembolso", "emb": [0.8, 0.6]},
    "d2": {"texto": "devolucao do valor", "emb": [1.0, 0.0]},
    "d3": {"texto": "horario de atendimento", "emb": [0.0, 1.0]},
}
consulta_texto = "reembolso"
consulta_emb = [1.0, 0.0]


def tok(t):
    return re.findall(r"[a-z0-9]+", t.lower())


docs = {d: tok(corpus[d]["texto"]) for d in corpus}
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
    s = 0.0
    for t in tok(query):
        if t not in df:
            continue
        f = tf[t]
        s += idf(t) * (f * (k1 + 1)) / (f + k1 * (1 - b + b * dl / avgdl))
    return s


def cosseno(a, b):
    a, b = np.array(a, float), np.array(b, float)
    n = np.linalg.norm(a) * np.linalg.norm(b)
    return 0.0 if n == 0 else float(a @ b / n)


denso = sorted(((d, cosseno(consulta_emb, corpus[d]["emb"])) for d in corpus),
               key=lambda t: (-t[1], t[0]))
esparso = sorted(((d, bm25(consulta_texto, d)) for d in corpus),
                 key=lambda t: (-t[1], t[0]))

print("ranking denso:", [d for d, _ in denso])
print("ranking esparso:", [d for d, _ in esparso])
print("top-1 denso:", denso[0][0], "| top-1 esparso:", esparso[0][0])
