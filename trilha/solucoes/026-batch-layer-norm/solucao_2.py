"""Solucao de referencia — Licao 026, Exercicio 2.

Batch Norm com gamma e beta: confirma que a media da saida por feature fica ~beta
e o desvio-padrao ~|gamma|, independentemente da escala da entrada.
"""
import numpy as np


def batch_norm(X, gamma, beta, eps=1e-5):
    mu = X.mean(axis=0)
    var = X.var(axis=0)
    Xn = (X - mu) / np.sqrt(var + eps)
    return gamma * Xn + beta


def main():
    X = np.array([[1.0, 100.0],
                  [3.0, 300.0],
                  [5.0, 500.0],
                  [7.0, 700.0]])
    gamma = np.array([3.0, 0.5])
    beta = np.array([5.0, -2.0])
    Y = batch_norm(X, gamma, beta)
    media = np.round(Y.mean(axis=0), 4)
    std = np.round(Y.std(axis=0), 4)
    print("media da saida:", media)
    print("std da saida:  ", std)
    print("media ~= beta:", np.allclose(media, beta, atol=1e-3))
    print("std ~= |gamma|:", np.allclose(std, np.abs(gamma), atol=1e-3))


if __name__ == "__main__":
    main()
