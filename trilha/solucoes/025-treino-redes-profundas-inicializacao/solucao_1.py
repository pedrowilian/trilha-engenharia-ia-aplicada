"""Solucao de referencia — Licao 025, Exercicio 1.

Inicializacao aleatoria QUEBRA a simetria: ao contrario do init com zeros, os
gradientes dos neuronios ocultos passam a ser diferentes entre si.
"""
import numpy as np


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def main():
    rng = np.random.default_rng(7)
    x = np.array([1.0, 2.0, 3.0])
    W1 = rng.standard_normal((4, 3)) * 0.5
    b1 = np.zeros(4)
    h = sigmoid(W1 @ x + b1)
    dh = h * (1.0 - h)            # supondo dL/dh = 1
    dW1 = np.outer(dh, x)
    iguais = np.allclose(dW1[0], dW1[1]) and np.allclose(dW1[1], dW1[2])
    print("ativacoes ocultas:", np.round(h, 4))
    print("linhas de dW1 identicas:", iguais)
    print("simetria quebrada:", not iguais)


if __name__ == "__main__":
    main()
