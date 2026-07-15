"""Solução de referência — Exercício 1 da Lição 049.

Efeito da temperatura sobre a softmax dos logits do próximo token.
"""
import numpy as np


def softmax(logits, T=1.0):
    z = np.asarray(logits, dtype=float) / T
    z = z - z.max()
    e = np.exp(z)
    return e / e.sum()


logits = np.array([2.0, 1.0, 0.5, -1.0])
for T in [0.5, 1.0, 2.0]:
    p = softmax(logits, T)
    dist = " ".join(f"{x:.4f}" for x in p)
    print(f"T={T}: [{dist}]  max={p.max():.4f}")
