"""Licao 017 — Exercicio 3: curva de aprendizado.

Tarefa:
- f(x) = 0.5*x^2. Use np.random.default_rng(7), X_full=linspace(-4,4,100),
  y_full = f + N(0,1). Validacao = 1 a cada 5 pontos; o resto e o pool de treino,
  embaralhado com rng.shuffle.
- Para n em [6, 20, 80], ajuste grau 2 nos primeiros n pontos do pool e meca
  erro de treino e de validacao; imprima
  `n_treino=<n>: erro_treino=... erro_val=... lacuna=...` (4 casas) e
  `lacuna encolhe com mais dados: <bool>`.

Criterio binario: saida IDENTICA a
trilha/solucoes/017-overfitting-validacao-cruzada/solucao_3.saida.txt
"""
import numpy as np


def f(x):
    return 0.5 * x ** 2


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
