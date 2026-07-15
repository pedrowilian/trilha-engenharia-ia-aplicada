"""Licao 015 — Exercicio 1: regressao ridge (L2) por solucao fechada.

Tarefa:
- Implemente `ridge(X, y, lam)` = solve(X^T X + lam*I, X^T y) com numpy.
- Para os dados dados, imprima, para lambda em [0.0, 5.0, 50.0]:
  `lambda=...: w=[w0, w1] norma_L2=...` (4 casas).
- Ao final, imprima `norma decresce com lambda: <bool>`.

Criterio binario: saida IDENTICA a
trilha/solucoes/015-regularizacao/solucao_1.saida.txt
"""
import numpy as np

X = np.array([[1.0, 4.0],
              [1.0, 2.0],
              [1.0, 6.0],
              [1.0, 8.0],
              [1.0, 10.0]])
y = np.array([9.0, 5.0, 13.0, 17.0, 21.0])


def ridge(X, y, lam):
    raise NotImplementedError


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
