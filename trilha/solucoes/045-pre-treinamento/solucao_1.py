"""Solução de referência — Exercício 1 da Lição 045.

Perda média de pré-treino (cross-entropy do próximo token) sobre um corpus,
com teacher forcing.
"""
import numpy as np

vocab = ["a", "b", "c"]
idx = {t: i for i, t in enumerate(vocab)}
P = np.array([
    [0.1, 0.7, 0.2],   # depois de "a"
    [0.2, 0.2, 0.6],   # depois de "b"
    [0.5, 0.3, 0.2],   # depois de "c"
])
corpus = "cabbac"

nll_total = 0.0
n = 0
for ant, prox in zip(corpus[:-1], corpus[1:]):
    p = P[idx[ant], idx[prox]]
    nll_total += -np.log(p)
    n += 1
ce = nll_total / n

print(f"pares de treino    = {n}")
print(f"cross-entropy media= {ce:.4f}")
print(f"perplexidade       = {np.exp(ce):.4f}")
