"""Solucao de referencia — Licao 022, Exercicio 3.

Demonstra empiricamente que um perceptron NAO resolve o XOR: treina por 100
epocas e registra a MELHOR acuracia vista em qualquer epoca (nunca chega a 4/4).
"""
import numpy as np


def degrau(z):
    return 1 if z >= 0.0 else 0


def acuracia(w, b, X, y):
    preds = [degrau(np.dot(w, xi) + b) for xi in X]
    return sum(int(p == t) for p, t in zip(preds, y))


def main():
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
    y = np.array([0, 1, 1, 0])      # XOR
    w = np.zeros(2)
    b = 0.0
    eta = 1.0
    melhor = acuracia(w, b, X, y)
    for epoca in range(100):
        for xi, alvo in zip(X, y):
            pred = degrau(np.dot(w, xi) + b)
            erro = alvo - pred
            if erro != 0:
                w = w + eta * erro * xi
                b = b + eta * erro
        melhor = max(melhor, acuracia(w, b, X, y))
    print(f"melhor acuracia em 100 epocas: {melhor}/4")
    print(f"resolveu o XOR (4/4): {melhor == 4}")


if __name__ == "__main__":
    main()
