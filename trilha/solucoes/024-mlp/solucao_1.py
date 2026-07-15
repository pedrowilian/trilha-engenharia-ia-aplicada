"""Solucao de referencia — Licao 024, Exercicio 1.

Forward pass de um MLP 2 -> 3 -> 1 com pesos fixos e ativacao sigmoid na
camada oculta. Imprime a camada oculta e a saida.
"""
import numpy as np


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def main():
    W1 = np.array([[0.5, -0.5], [1.0, 1.0], [-1.0, 0.5]])  # 3 ocultos, 2 entradas
    b1 = np.array([0.0, -0.5, 0.2])
    W2 = np.array([1.0, -1.0, 0.5])                        # 1 saida, 3 ocultos
    b2 = 0.1
    x = np.array([1.0, 2.0])
    h = sigmoid(W1 @ x + b1)
    y = sigmoid(W2 @ h + b2)
    print(f"shapes: x={x.shape} h={h.shape}")
    print("h:", np.round(h, 4))
    print(f"saida: {y:.4f}")


if __name__ == "__main__":
    main()
