"""Solução de referência — Exercício 3 da Lição 067.

Recuperação por similaridade do cosseno: retorna os top-2 episódios mais
parecidos com a consulta. Determinístico.
"""
import numpy as np

memoria = [
    ("python e linguagem", np.array([1.0, 0.0, 0.0])),
    ("cobra python", np.array([0.8, 0.2, 0.0])),
    ("cafe quente", np.array([0.0, 0.0, 1.0])),
]


def cosseno(u, v):
    return float(u @ v / (np.linalg.norm(u) * np.linalg.norm(v)))


consulta = np.array([1.0, 0.0, 0.0])
ranking = sorted(memoria, key=lambda e: cosseno(consulta, e[1]), reverse=True)
for texto, vetor in ranking[:2]:
    print(f"{texto}: {cosseno(consulta, vetor):.3f}")
