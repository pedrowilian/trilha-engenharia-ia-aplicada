"""Licao 017 — Exercicio 2: validacao cruzada k-fold do zero.

Tarefa:
- f(x) = sin(1.2*x). Use np.random.default_rng(42), X=linspace(-3,3,40),
  y = f(X) + N(0, 0.3).
- Implemente k-fold (k=5) com np.array_split sobre os indices. Para cada grau
  em [1,2,3,4,5], calcule o erro de validacao medio; imprima `grau=<g>: erro_cv=...`
  (4 casas) e `melhor grau (k-fold): <g>`.

Criterio binario: saida IDENTICA a
trilha/solucoes/017-overfitting-validacao-cruzada/solucao_2.saida.txt
"""
import numpy as np


def f(x):
    return np.sin(1.2 * x)


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
