"""Solucao de referencia - Exercicio 2 da Licao 057.

Recuperacao top-k por cosseno: ordena os documentos por similaridade decrescente
(desempate por id) e devolve os k melhores.
"""
import re

import numpy as np


corpus = {
    "d1": "gato e cachorro sao animais domesticos",
    "d2": "python e uma linguagem de programacao",
    "d3": "cachorro late e o gato mia",
    "d4": "java e python sao linguagens populares",
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


def recuperar(pergunta, k=2):
    qv = vetorizar(pergunta)
    ranking = sorted(((d, cosseno(qv, vetorizar(corpus[d]))) for d in corpus),
                     key=lambda t: (-t[1], t[0]))
    return ranking[:k]


pergunta = "linguagem python"
for d, s in recuperar(pergunta, k=2):
    print(f"{d} {s:.4f}")
