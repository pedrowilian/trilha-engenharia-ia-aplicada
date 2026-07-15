"""Licao 016 — Exercicio 1: vies^2 e variancia empiricos.

Tarefa:
- f(x) = 0.5*x^2. Em x0=2.0, com sigma=1.0 e M=2000 datasets reamostrados
  (use np.random.default_rng(10) e x_treino = linspace(-3, 3, 15)).
- Estime vies^2 e variancia das predicoes para um modelo de grau 0 e um de grau 3.
- Imprima `grau 0: vies^2=... variancia=...`, `grau 3: ...` (4 casas),
  `grau 0 tem mais vies: <bool>` e `grau 3 tem mais variancia: <bool>`.

Criterio binario: saida IDENTICA a
trilha/solucoes/016-vies-variancia/solucao_1.saida.txt
"""
import numpy as np


def f(x):
    return 0.5 * x ** 2


def bias_var(grau, rng, x_treino, x0, sigma, M):
    raise NotImplementedError


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
