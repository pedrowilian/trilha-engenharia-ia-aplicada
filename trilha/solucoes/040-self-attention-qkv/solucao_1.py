"""Solução de referência — Exercício 1 da Lição 040.

Scaled dot-product self-attention do zero: projeta X em Q/K/V, calcula os pesos
de atenção via softmax estável e devolve (saida, pesos).
"""
import numpy as np

np.set_printoptions(precision=4, suppress=True)

X = np.array([
    [2.0, 0.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, 2.0],
    [1.0, 1.0, 1.0, 0.0],
    [0.0, 2.0, 1.0, 1.0],
])
Wq = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 0.0], [0.0, 1.0]])
Wk = np.array([[0.0, 1.0], [1.0, 0.0], [0.0, 1.0], [1.0, 0.0]])
Wv = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0], [0.0, 1.0]])


def softmax(x, axis=-1):
    x = x - np.max(x, axis=axis, keepdims=True)
    e = np.exp(x)
    return e / np.sum(e, axis=axis, keepdims=True)


def self_attention(X, Wq, Wk, Wv):
    Q, K, V = X @ Wq, X @ Wk, X @ Wv
    d_k = Q.shape[-1]
    pesos = softmax(Q @ K.T / np.sqrt(d_k), axis=-1)
    return pesos @ V, pesos


saida, pesos = self_attention(X, Wq, Wk, Wv)
print("pesos de atencao =")
print(np.round(pesos, 4))
print("posicao mais atendida por linha:", pesos.argmax(axis=1).tolist())
