"""Exercício 3 — Forward pass de uma rede neural de 2 camadas.

Setup: pesos e vieses fixos de uma rede com camada oculta (ReLU) e camada de saída.
Objetivo: calcular h = ReLU(W1 @ x + b1) e y = W2 @ h + b2 para uma entrada fixa.
"""
import numpy as np

x = np.array([1.0, 2.0])

W1 = np.array([[0.5, -0.5],
               [1.0,  0.0],
               [-1.0, 2.0]])   # 3x2
b1 = np.array([0.0, 1.0, -1.0])

W2 = np.array([[1.0, 0.0, -1.0],
               [0.5, 0.5, 0.5]])  # 2x3
b2 = np.array([0.0, 0.0])


def relu(z):
    return np.maximum(0.0, z)


h = relu(W1 @ x + b1)
y = W2 @ h + b2

print("h (camada oculta):", h.tolist())
print("y (saida):", y.tolist())
