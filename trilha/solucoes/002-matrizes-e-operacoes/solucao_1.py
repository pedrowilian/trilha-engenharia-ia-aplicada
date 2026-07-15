"""Exercício 1 — Multiplicação de matrizes implementada do zero.

Setup: A e B são matrizes 2x2.
Objetivo: implementar matmul(A, B) com laços e conferir contra o numpy.
"""
import numpy as np


def matmul(A, B):
    """Produto de matrizes: (A@B)[i][j] = soma_k A[i][k] * B[k][j]."""
    m, n = len(A), len(A[0])
    n2, p = len(B), len(B[0])
    assert n == n2, "dimensões incompatíveis"
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(p)]
            for i in range(m)]


A = [[1.0, 2.0], [3.0, 4.0]]
B = [[5.0, 6.0], [7.0, 8.0]]

AB = matmul(A, B)
print("A@B (do zero):", AB)
print("confere numpy?", np.allclose(np.array(AB), np.array(A) @ np.array(B)))
