"""Solução de referência — Exercício 3 da Lição 043.

Bloco de encoder completo (atenção + residual/norm + FFN + residual/norm). A saída
tem a MESMA forma da entrada, permitindo empilhar blocos.
"""
import numpy as np

np.set_printoptions(precision=4, suppress=True)


def softmax(x, axis=-1):
    x = x - np.max(x, axis=axis, keepdims=True)
    e = np.exp(x)
    return e / np.sum(e, axis=axis, keepdims=True)


def layer_norm(x, eps=1e-5):
    mu = x.mean(axis=-1, keepdims=True)
    var = x.var(axis=-1, keepdims=True)
    return (x - mu) / np.sqrt(var + eps)


def self_attention(X, Wq, Wk, Wv):
    Q, K, V = X @ Wq, X @ Wk, X @ Wv
    d_k = Q.shape[-1]
    return softmax(Q @ K.T / np.sqrt(d_k), axis=-1) @ V


rng = np.random.default_rng(55)
n, d_model, d_ff = 4, 6, 12
X = rng.normal(0, 1, size=(n, d_model))
Wq = rng.normal(0, 1, (d_model, d_model))
Wk = rng.normal(0, 1, (d_model, d_model))
Wv = rng.normal(0, 1, (d_model, d_model))
W1 = rng.normal(0, 1, (d_model, d_ff))
W2 = rng.normal(0, 1, (d_ff, d_model))

a = self_attention(X, Wq, Wk, Wv)
x1 = layer_norm(X + a)
f = np.maximum(0.0, x1 @ W1) @ W2
Y = layer_norm(x1 + f)

print("entrada shape:", X.shape, "-> saida shape:", Y.shape)
print("shape preservado:", X.shape == Y.shape)
print("media por linha (apos norm):", np.round(Y.mean(axis=-1), 4))
print("Y[0] =", np.round(Y[0], 4))
