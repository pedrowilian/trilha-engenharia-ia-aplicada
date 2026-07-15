"""Solucao de referencia — Licao 026, Exercicio 3.

Contrasta os eixos de Batch Norm e Layer Norm na MESMA matriz: BN normaliza as
colunas (features sobre o batch); LN normaliza as linhas (features por exemplo).
"""
import numpy as np


def batch_norm(X, eps=1e-5):
    return (X - X.mean(axis=0)) / np.sqrt(X.var(axis=0) + eps)


def layer_norm(X, eps=1e-5):
    mu = X.mean(axis=1, keepdims=True)
    var = X.var(axis=1, keepdims=True)
    return (X - mu) / np.sqrt(var + eps)


def main():
    X = np.array([[1.0, 2.0, 6.0],
                  [4.0, 4.0, 4.0]])
    bn = batch_norm(X)
    ln = layer_norm(X)
    print("BN -> media por COLUNA:", np.round(bn.mean(axis=0), 4))
    print("LN -> media por LINHA: ", np.round(ln.mean(axis=1), 4))


if __name__ == "__main__":
    main()
