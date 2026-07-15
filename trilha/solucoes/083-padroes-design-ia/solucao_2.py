"""Solução de referência — Exercício 2 da Lição 083.

Semantic cache: hit quando a maior similaridade de cosseno >= limiar.
"""
import numpy as np

cache_emb = np.array([
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0],
])
cache_resp = ["A", "B", "C"]


def cosseno(a, b):
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))


def consultar(q, limiar):
    sims = [cosseno(q, e) for e in cache_emb]
    i = int(np.argmax(sims))
    if sims[i] >= limiar:
        return "hit", cache_resp[i], round(sims[i], 3)
    return "miss", None, round(sims[i], 3)


consultas = [
    np.array([0.95, 0.05, 0.0]),
    np.array([0.0, 0.30, 0.95]),
    np.array([0.6, 0.6, 0.0]),
]
limiar = 0.9

for q in consultas:
    estado, resp, sim = consultar(q, limiar)
    print(f"sim={sim} -> {estado} | {resp}")
