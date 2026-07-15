"""Exercício 1 — Produto matriz-vetor do zero e verificação de linearidade.

Setup: matriz A 2x2 que define a transformação T(x) = A @ x.
Objetivo: implementar matvec(A, x) e checar T(a*u + b*v) = a*T(u) + b*T(v).
"""
import numpy as np

A = np.array([[2.0, -1.0],
              [0.0,  3.0]])


def matvec(A, x):
    """Produto matriz-vetor: cada saída é o produto interno de uma linha por x."""
    return [float(sum(A[i][k] * x[k] for k in range(len(x)))) for i in range(len(A))]


u = np.array([1.0, 2.0])
v = np.array([3.0, -1.0])
a, b = 2.0, -1.0

esquerda = matvec(A, a * u + b * v)
direita = (a * np.array(matvec(A, u)) + b * np.array(matvec(A, v))).tolist()

print("T(a*u + b*v):", esquerda)
print("a*T(u)+b*T(v):", direita)
print("linear?", np.allclose(esquerda, direita))
