"""Exercício 3 — Independência linear e coordenadas em uma base.

Setup: dois vetores b1, b2 em R^2 e um vetor x.
Objetivo: verificar se {b1, b2} formam uma base (determinante != 0) e
calcular as coordenadas de x nessa base.
"""
import numpy as np

b1 = np.array([2.0, 0.0])
b2 = np.array([0.0, 3.0])
B = np.column_stack([b1, b2])

det = float(np.linalg.det(B))
eh_base = abs(det) > 1e-9

x = np.array([6.0, 9.0])
coords = np.linalg.solve(B, x)

print("determinante:", round(det, 4))
print("forma base? ", eh_base)
print("coordenadas:", np.round(coords, 4).tolist())
