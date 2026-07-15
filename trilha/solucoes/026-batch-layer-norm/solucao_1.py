"""Solucao de referencia — Licao 026, Exercicio 1.

Padroniza um batch por feature (media 0, variancia 1) e confirma o resultado.
"""
import numpy as np


def padronizar(X, eps=1e-5):
    mu = X.mean(axis=0)
    var = X.var(axis=0)
    return (X - mu) / np.sqrt(var + eps)


def main():
    X = np.array([[2.0, 10.0],
                  [4.0, 20.0],
                  [6.0, 30.0],
                  [8.0, 40.0]])
    Xn = padronizar(X)
    print("normalizado:\n", np.round(Xn, 4))
    print("media por feature:", np.round(Xn.mean(axis=0), 4))
    print("std por feature:  ", np.round(Xn.std(axis=0), 4))


if __name__ == "__main__":
    main()
