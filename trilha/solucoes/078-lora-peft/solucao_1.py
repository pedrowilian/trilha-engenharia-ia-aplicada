"""Solução de referência — Exercício 1 da Lição 078.

Constrói a atualização de baixo posto ΔW = B·A e compara seu posto e número de
parâmetros com os de uma matriz cheia W0 de mesmo formato.
"""
import numpy as np

rng = np.random.default_rng(7)
d, k, r = 8, 5, 3
B = rng.normal(size=(d, r))
A = rng.normal(size=(r, k))
delta = B @ A
W0 = rng.normal(size=(d, k))
W = W0 + delta

print("shape delta:", delta.shape)
print("posto de delta (BA):", int(np.linalg.matrix_rank(delta)))
print("posto de W0 (cheia):", int(np.linalg.matrix_rank(W0)))
print("parametros LoRA (B,A):", B.size + A.size)
print("parametros da matriz cheia:", W0.size)
