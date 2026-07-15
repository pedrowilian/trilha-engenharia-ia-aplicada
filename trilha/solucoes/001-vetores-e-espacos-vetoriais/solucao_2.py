"""Exercício 2 — Resolver uma combinação linear.

Setup: vetores u1, u2 em R^2 e um vetor alvo.
Objetivo: encontrar coeficientes (a1, a2) tais que a1*u1 + a2*u2 = alvo e
reconstruir o alvo a partir deles.
"""
import numpy as np

u1 = np.array([1.0, 2.0])
u2 = np.array([3.0, 1.0])
alvo = np.array([5.0, 5.0])

A = np.column_stack([u1, u2])          # colunas são u1 e u2
coef = np.linalg.solve(A, alvo)        # resolve A @ coef = alvo

print("coeficientes:", np.round(coef, 4).tolist())
print("reconstrucao:", np.round(coef[0] * u1 + coef[1] * u2, 4).tolist())
