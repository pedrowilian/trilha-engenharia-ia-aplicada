"""Solução de referência — Exercício 1 da Lição 043.

LayerNorm normaliza cada linha (token) para média 0 e variância 1 ao longo das
features, independentemente da escala original.
"""
import numpy as np

np.set_printoptions(precision=4, suppress=True)


def layer_norm(x, eps=1e-5):
    mu = x.mean(axis=-1, keepdims=True)
    var = x.var(axis=-1, keepdims=True)
    return (x - mu) / np.sqrt(var + eps)


X = np.array([[2.0, 4.0, 6.0, 8.0],
              [1.0, 1.0, 1.0, 5.0],
              [-3.0, 0.0, 3.0, 6.0]])
Y = layer_norm(X)
print("apos layer_norm =\n", np.round(Y, 4))
print("media por linha:", np.round(Y.mean(axis=-1), 4))
print("desvio por linha:", np.round(Y.std(axis=-1), 4))
