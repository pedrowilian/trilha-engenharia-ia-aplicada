"""Solução de referência — Exercício 2 da Lição 004.

Calcula a SVD de uma matriz e mede o erro de reconstrução e a energia
(variância) capturada por aproximações de posto k = 1, 2 e 3.
"""
import numpy as np

C = np.array([[3.0, 0.0, 0.0],
              [0.0, 2.0, 0.0],
              [0.0, 0.0, 1.0]])

U, S, Vt = np.linalg.svd(C, full_matrices=False)
print(f"Valores singulares: {[round(float(s), 4) for s in S]}")

total = (S ** 2).sum()
for k in (1, 2, 3):
    aprox = (U[:, :k] * S[:k]) @ Vt[:k, :]
    erro = np.linalg.norm(C - aprox)
    energia = (S[:k] ** 2).sum() / total
    print(f"rank-{k}: erro={erro:.4f} energia={energia * 100:.1f}%")
