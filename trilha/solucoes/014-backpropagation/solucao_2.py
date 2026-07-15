"""Solucao de referencia — Licao 014, Exercicio 2.

Backprop de um passo em um neuronio sigmoide com perda BCE, seguido de uma
atualizacao de gradient descent. Mostra que a perda diminui apos o passo.
"""
import math


def sigmoid(z):
    return 1.0 / (1.0 + math.exp(-z))


def forward(w, b, x, y):
    p = sigmoid(w * x + b)
    L = -(y * math.log(p) + (1 - y) * math.log(1 - p))
    return p, L


def main():
    x, y = 1.5, 1.0
    w, b = -1.0, 0.0
    eta = 0.5

    p, L0 = forward(w, b, x, y)
    dL_dz = p - y
    dL_dw = dL_dz * x
    dL_db = dL_dz
    # um passo de gradient descent
    w -= eta * dL_dw
    b -= eta * dL_db
    _, L1 = forward(w, b, x, y)

    print(f"perda antes:  {L0:.4f}")
    print(f"dL/dw={dL_dw:.4f} dL/db={dL_db:.4f}")
    print(f"perda depois: {L1:.4f}")
    print("perda diminuiu:", L1 < L0)


if __name__ == "__main__":
    main()
