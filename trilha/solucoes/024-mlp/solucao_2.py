"""Solucao de referencia — Licao 024, Exercicio 2.

Verifica que o MLP com pesos a mao (camada oculta ReLU) classifica TODOS os
quatro casos do XOR corretamente (4/4) — algo impossivel para um perceptron.
"""
import numpy as np


def relu(z):
    return np.maximum(0.0, z)


def main():
    W1 = np.array([[1.0, 1.0], [1.0, 1.0]])
    b1 = np.array([0.0, -1.0])
    W2 = np.array([1.0, -2.0])
    b2 = 0.0
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
    alvo = [0, 1, 1, 0]
    acertos = 0
    for x, t in zip(X, alvo):
        h = relu(W1 @ x + b1)
        classe = int((W2 @ h + b2) >= 0.5)
        acertos += int(classe == t)
        print(f"x={x.astype(int)} classe={classe} alvo={t}")
    print(f"acertos={acertos}/4 resolveu o XOR: {acertos == 4}")


if __name__ == "__main__":
    main()
