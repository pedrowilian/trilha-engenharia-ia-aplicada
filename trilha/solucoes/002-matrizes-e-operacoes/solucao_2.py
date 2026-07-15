"""Exercício 2 — Propriedades da transposta.

Setup: A é 2x3 e B é 3x2.
Objetivo: verificar (A^T)^T = A e (A@B)^T = B^T @ A^T.
"""
import numpy as np

A = np.array([[1.0, 2.0, 3.0],
              [4.0, 5.0, 6.0]])
B = np.array([[1.0, 0.0],
              [0.0, 1.0],
              [2.0, 1.0]])

print("(A.T).T == A?", np.array_equal(A.T.T, A))
print("(A@B).T == B.T@A.T?", np.array_equal((A @ B).T, B.T @ A.T))
print("A@B:", (A @ B).tolist())
