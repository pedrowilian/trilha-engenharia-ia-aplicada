"""Licao 022 — Exercicio 2: projetar a mao a porta NOT.

Tarefa:
- Um perceptron de UMA entrada implementa NOT se o peso for negativo e o vies
  positivo (ex.: w = -1.0, b = 0.5).
- Para x em {0, 1}, calcule z = w*x + b e a saida degrau(z).
- Imprima, por linha, `x=... z=... NOT=...` (z com sinal e 1 casa decimal).

Criterio binario: saida IDENTICA a
trilha/solucoes/022-perceptron/solucao_2.saida.txt
"""
import numpy as np


def degrau(z):
    return 1 if z >= 0.0 else 0


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
