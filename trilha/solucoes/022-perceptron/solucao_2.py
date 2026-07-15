"""Solucao de referencia — Licao 022, Exercicio 2.

Projeta a mao os pesos de um perceptron que implementa a porta NOT
(uma unica entrada). NOT(x) = 1 quando x = 0; usa w negativo e vies positivo.
"""
import numpy as np


def degrau(z):
    return 1 if z >= 0.0 else 0


def main():
    w = -1.0     # peso negativo: entrada alta empurra z para baixo
    b = 0.5      # vies positivo: com x=0, z=0.5 >= 0 -> saida 1
    for x in [0, 1]:
        z = w * x + b
        print(f"x={x} z={z:+.1f} NOT={degrau(z)}")


if __name__ == "__main__":
    main()
