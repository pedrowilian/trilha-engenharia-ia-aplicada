"""Solução de referência — Exercício 2 da Lição 040.

Mostra por que dividimos os scores por sqrt(d_k): em alta dimensão o produto
interno tem desvio-padrão ~sqrt(d_k); sem escala, a softmax satura (vira quase
one-hot) e os gradientes desaparecem.
"""
import numpy as np


def softmax(x, axis=-1):
    x = x - np.max(x, axis=axis, keepdims=True)
    e = np.exp(x)
    return e / np.sum(e, axis=axis, keepdims=True)


rng = np.random.default_rng(0)
d_k = 64
Q = rng.normal(0, 1, size=(1, d_k))
K = rng.normal(0, 1, size=(5, d_k))

brutos = (Q @ K.T)[0]
escalados = brutos / np.sqrt(d_k)
print(f"desvio-padrao scores brutos:    {brutos.std():.4f}")
print(f"desvio-padrao scores escalados: {escalados.std():.4f}")
print(f"peso maximo sem escala:  {softmax(brutos).max():.4f}")
print(f"peso maximo com escala:  {softmax(escalados).max():.4f}")
