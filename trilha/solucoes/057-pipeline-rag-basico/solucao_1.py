"""Solucao de referencia - Exercicio 1 da Licao 057.

Representacao vetorial (bag-of-words sobre um vocabulario fixo) e similaridade do
cosseno entre a consulta e cada documento. E a recuperacao densa em sua forma
mais simples e deterministica.
"""
import re

import numpy as np


corpus = {
    "d1": "gato e cachorro sao animais domesticos",
    "d2": "python e uma linguagem de programacao",
    "d3": "cachorro late e o gato mia",
}


def tokenizar(t):
    return re.findall(r"[a-z0-9]+", t.lower())


vocab = sorted({tok for txt in corpus.values() for tok in tokenizar(txt)})
idx = {t: i for i, t in enumerate(vocab)}


def vetorizar(texto):
    v = np.zeros(len(vocab))
    for tok in tokenizar(texto):
        if tok in idx:
            v[idx[tok]] += 1.0
    return v


def cosseno(a, b):
    na, nb = np.linalg.norm(a), np.linalg.norm(b)
    if na == 0 or nb == 0:
        return 0.0
    return float(a @ b / (na * nb))


pergunta = "o gato e o cachorro"
qv = vetorizar(pergunta)
for d in sorted(corpus):
    print(f"{d} {cosseno(qv, vetorizar(corpus[d])):.4f}")
