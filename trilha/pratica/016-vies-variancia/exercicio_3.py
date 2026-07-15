"""Licao 016 — Exercicio 3: mais dados reduzem a variancia.

Tarefa:
- f(x) = 0.5*x^2, modelo de grau 4. Em x0=1.5, sigma=1.0, M=1500
  (use np.random.default_rng(5)).
- Para n em [10, 40, 160], estime a variancia das predicoes em x0 sobre M
  datasets de tamanho n; imprima `n=<n>: variancia=...` (4 casas) e
  `variancia cai com mais dados: <bool>`.

Criterio binario: saida IDENTICA a
trilha/solucoes/016-vies-variancia/solucao_3.saida.txt
"""
import numpy as np


def f(x):
    return 0.5 * x ** 2


def variancia_no_ponto(n, rng, x0, sigma, M, grau=4):
    raise NotImplementedError


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
