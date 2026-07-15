"""Exercício 3 — Inversa e resolução de sistema linear.

Setup: matriz A 2x2 inversível e vetor b.
Objetivo: calcular a inversa, confirmar A @ A_inv = I e resolver A x = b.
"""
import numpy as np

A = np.array([[4.0, 3.0],
              [6.0, 3.0]])
b = np.array([10.0, 12.0])

A_inv = np.linalg.inv(A)
identidade = np.round(A @ A_inv, 4) + 0.0   # + 0.0 evita -0.0 na impressão
x = A_inv @ b

print("inversa:", np.round(A_inv, 4).tolist())
print("A@A_inv:", identidade.tolist())
print("x:", np.round(x, 4).tolist())
