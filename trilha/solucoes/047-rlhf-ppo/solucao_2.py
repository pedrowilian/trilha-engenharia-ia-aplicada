"""Solução de referência — Exercício 2 da Lição 047.

Recompensa efetiva com penalidade KL: r_efetiva = r - beta * KL(politica||ref).
"""
import numpy as np

# Recompensa do reward model por amostra e divergência KL contra a referência.
r = np.array([2.0, 1.0, -0.5, 0.4])
kl = np.array([0.5, 3.0, 0.2, 1.0])
beta = 0.2

r_efetiva = r - beta * kl
for i, (ri, ki, re) in enumerate(zip(r, kl, r_efetiva)):
    print(f"amostra {i}: r={ri:+.2f} kl={ki:.2f} r_efetiva={re:+.4f}")
print(f"recompensa efetiva media = {r_efetiva.mean():.4f}")
