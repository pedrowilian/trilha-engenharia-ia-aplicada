"""Solução de referência — Exercício 3 da Lição 078.

Mostra o efeito do fator de escala alpha/r na saída de uma camada adaptada por
LoRA: y = x·(W0 + (alpha/r)·B·A).
"""
import numpy as np

rng = np.random.default_rng(3)
d, k, r = 5, 4, 2
W0 = rng.normal(size=(d, k))
B = rng.normal(size=(d, r))
A = rng.normal(size=(r, k))
x = np.ones(d)

base = x @ W0
print(f"||y|| base (so W0): {np.linalg.norm(base):.4f}")
for alpha in [2, 4, 16]:
    escala = alpha / r
    y = x @ (W0 + escala * (B @ A))
    print(f"alpha={alpha:>2}: escala={escala:.1f} ||y||={np.linalg.norm(y):.4f}")
