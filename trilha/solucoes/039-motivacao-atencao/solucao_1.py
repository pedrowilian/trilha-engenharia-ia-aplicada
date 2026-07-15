"""Solução de referência — Exercício 1 da Lição 039.

Decaimento da influência de x_0 numa recorrência linear h_t = a*h_{t-1} + x_t:
a sensibilidade de h_t a x_0 é a**t, que cai exponencialmente com a distância.
"""
import numpy as np

a = 0.8
T = 12
influencia = a ** np.arange(T + 1)
for t in [0, 4, 8, 12]:
    print(f"t={t:>2}: influencia={influencia[t]:.6f}")

limiar = 0.1
primeiro = next(t for t in range(T + 1) if influencia[t] < limiar)
print(f"primeiro t com influencia < {limiar}: {primeiro}")
