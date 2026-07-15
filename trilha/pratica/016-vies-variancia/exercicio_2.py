"""Licao 016 — Exercicio 2: curva em U do erro de teste.

Tarefa:
- f(x) = sin(1.5*x). Use np.random.default_rng(3), x_treino=linspace(-3,3,11)
  com ruido N(0, 0.25), e x_teste=linspace(-3,3,200) com alvo verdadeiro f(x_teste).
- Para grau de 1 a 9, ajuste um polinomio e calcule o erro de teste (MSE);
  imprima `grau=<g>: erro_teste=...` (4 casas) e, ao final,
  `melhor grau (menor erro_teste): <g>`.

Criterio binario: saida IDENTICA a
trilha/solucoes/016-vies-variancia/solucao_2.saida.txt
"""
import numpy as np


def f(x):
    return np.sin(1.5 * x)


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
