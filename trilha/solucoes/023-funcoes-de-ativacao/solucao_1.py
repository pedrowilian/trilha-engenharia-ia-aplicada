"""Solucao de referencia — Licao 023, Exercicio 1.

Implementa tanh e sua derivada analitica (1 - tanh^2) e valida contra a
aproximacao numerica por diferencas finitas centrais em z = 0.8.
"""
import numpy as np


def tanh(z):
    return np.tanh(z)


def dtanh(z):
    return 1.0 - np.tanh(z) ** 2


def main():
    z = 0.8
    h = 1e-5
    analitico = dtanh(z)
    numerico = (tanh(z + h) - tanh(z - h)) / (2 * h)
    print(f"tanh(0.8)      = {tanh(z):.6f}")
    print(f"deriv analitica= {analitico:.6f}")
    print(f"deriv numerica = {numerico:.6f}")
    print(f"diferenca < 1e-6: {abs(analitico - numerico) < 1e-6}")


if __name__ == "__main__":
    main()
