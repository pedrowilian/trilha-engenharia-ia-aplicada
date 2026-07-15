"""Solução de referência — Exercício 1 da Lição 042.

split_heads / merge_heads são inversos exatos: concatenar as cabeças recupera a
matriz original para qualquer número de cabeças que divida d_model.
"""
import numpy as np


def split_heads(M, h):
    n, d_model = M.shape
    return M.reshape(n, h, d_model // h).transpose(1, 0, 2)


def merge_heads(ctx):
    h, n, d_k = ctx.shape
    return ctx.transpose(1, 0, 2).reshape(n, h * d_k)


X = np.arange(24.0).reshape(4, 6)
for h in [1, 2, 3]:
    cabecas = split_heads(X, h)
    rec = merge_heads(cabecas)
    print(f"h={h}: shape cabecas {cabecas.shape} | round-trip exato: {np.array_equal(rec, X)}")
