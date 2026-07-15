"""Solução de referência — Exercício 2 da Lição 049.

Filtragem top-k: mantém apenas os k tokens mais prováveis e renormaliza.
"""
import numpy as np


def softmax(logits):
    z = logits - logits.max()
    e = np.exp(z)
    return e / e.sum()


logits = np.array([2.0, 1.0, 0.5, 0.0, -1.0])
p = softmax(logits)
k = 3

idx = np.argsort(-p)[:k]
mascara = np.zeros_like(p)
mascara[idx] = 1.0
p_top = p * mascara
p_top = p_top / p_top.sum()

print("p original:", np.round(p, 4).tolist())
print(f"top-{k} indices:", sorted(idx.tolist()))
print("p top-k   :", np.round(p_top, 4).tolist())
