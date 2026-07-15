"""Solução de referência — Exercício 3 da Lição 047.

Objetivo clipado do PPO: L_clip = min(ratio*A, clip(ratio, 1-eps, 1+eps)*A).
"""
import numpy as np


def clip(x, lo, hi):
    return np.minimum(np.maximum(x, lo), hi)


# Razão de probabilidade nova/antiga e vantagem estimada por amostra.
ratio = np.array([1.30, 0.70, 1.05, 0.90])
A = np.array([1.0, 1.0, -1.0, -1.0])
eps = 0.2

nao_clipado = ratio * A
clipado = clip(ratio, 1 - eps, 1 + eps) * A
objetivo = np.minimum(nao_clipado, clipado)
for i in range(len(ratio)):
    print(f"i={i}: ratio={ratio[i]:.2f} A={A[i]:+.1f} L_clip={objetivo[i]:+.4f}")
print(f"objetivo PPO (media) = {objetivo.mean():.4f}")
