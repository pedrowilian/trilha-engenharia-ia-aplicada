"""Solucao de referencia — Licao 027, Exercicio 2.

Compara a propagacao do gradiente por 10 camadas com sigmoid (derivada <= 0.25,
some) e com ReLU na regiao ativa (derivada 1, preserva o gradiente).
"""
import numpy as np


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def main():
    a = 0.5
    grad_sig = 1.0
    for _ in range(10):
        s = sigmoid(a)
        grad_sig *= s * (1.0 - s)     # derivada da sigmoid
        a = s

    grad_relu = 1.0
    for _ in range(10):
        grad_relu *= 1.0              # ReLU ativa: derivada 1

    print(f"grad final (sigmoid): {grad_sig:.3e}")
    print(f"grad final (ReLU):    {grad_relu:.3e}")
    print(f"sigmoid desapareceu (< 1e-3): {grad_sig < 1e-3}")
    print(f"ReLU preservou (~1):          {np.isclose(grad_relu, 1.0)}")


if __name__ == "__main__":
    main()
