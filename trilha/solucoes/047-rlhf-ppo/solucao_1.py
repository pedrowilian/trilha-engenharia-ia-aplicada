"""Solução de referência — Exercício 1 da Lição 047.

Perda de preferência do reward model (Bradley-Terry): -log sigmoid(r_w - r_l).
"""
import numpy as np


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


# Recompensas atribuídas pelo reward model às respostas escolhida (w) e rejeitada (l).
r_chosen = np.array([3.0, 0.5, 2.0, -0.5])
r_rejected = np.array([1.0, 1.5, 2.0, -1.5])

margens = r_chosen - r_rejected
perdas = -np.log(sigmoid(margens))
for i, (m, p) in enumerate(zip(margens, perdas)):
    print(f"par {i}: margem={m:+.2f}  perda={p:.4f}")
print(f"perda media = {perdas.mean():.4f}")
