"""Solução de referência — Exercício 3 da Lição 042.

Cabeças com projeções independentes produzem mapas de atenção diferentes sobre a
MESMA sequência — evidência de que cada cabeça pode se especializar.
"""
import numpy as np


def softmax(x, axis=-1):
    x = x - np.max(x, axis=axis, keepdims=True)
    e = np.exp(x)
    return e / np.sum(e, axis=axis, keepdims=True)


rng = np.random.default_rng(0)
n, d_model, h = 6, 8, 4
d_k = d_model // h
X = rng.normal(0, 1, size=(n, d_model))

argmaxes = []
for c in range(h):
    Wq = rng.normal(0, 1, size=(d_model, d_k))
    Wk = rng.normal(0, 1, size=(d_model, d_k))
    P = softmax((X @ Wq) @ (X @ Wk).T / np.sqrt(d_k), axis=-1)
    argmaxes.append(P.argmax(axis=1).tolist())

for c in range(h):
    print(f"cabeca {c}: posicao mais atendida por linha = {argmaxes[c]}")
print("todas as cabecas iguais:", all(argmaxes[c] == argmaxes[0] for c in range(h)))
