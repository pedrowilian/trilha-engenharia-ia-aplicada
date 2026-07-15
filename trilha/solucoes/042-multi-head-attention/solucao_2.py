"""Solução de referência — Exercício 2 da Lição 042.

Multi-head attention completa do zero: split em cabeças, atenção escalada em lote,
merge e projeção final W^O. A saída preserva a forma (n, d_model).
"""
import numpy as np

np.set_printoptions(precision=4, suppress=True)


def softmax(x, axis=-1):
    x = x - np.max(x, axis=axis, keepdims=True)
    e = np.exp(x)
    return e / np.sum(e, axis=axis, keepdims=True)


def split_heads(M, h):
    n, d_model = M.shape
    return M.reshape(n, h, d_model // h).transpose(1, 0, 2)


def merge_heads(ctx):
    h, n, d_k = ctx.shape
    return ctx.transpose(1, 0, 2).reshape(n, h * d_k)


rng = np.random.default_rng(7)
n, d_model, h = 5, 12, 3
X = rng.normal(0, 1, size=(n, d_model))
Wq = rng.normal(0, 1, size=(d_model, d_model))
Wk = rng.normal(0, 1, size=(d_model, d_model))
Wv = rng.normal(0, 1, size=(d_model, d_model))
Wo = rng.normal(0, 1, size=(d_model, d_model))

d_k = d_model // h
Q = split_heads(X @ Wq, h)
K = split_heads(X @ Wk, h)
V = split_heads(X @ Wv, h)
pesos = softmax(Q @ K.transpose(0, 2, 1) / np.sqrt(d_k), axis=-1)
ctx = pesos @ V
saida = merge_heads(ctx) @ Wo

print("saida shape:", saida.shape)
print("soma de cada linha dos pesos (deve ser 1):")
print(np.round(pesos.sum(axis=-1), 4))
print("saida[0] =", np.round(saida[0], 4))
