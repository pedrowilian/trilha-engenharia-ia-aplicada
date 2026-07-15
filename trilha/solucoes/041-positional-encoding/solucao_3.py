"""Solução de referência — Exercício 3 da Lição 041.

Verifica a propriedade de deslocamento relativo do encoding sinusoidal: o produto
interno entre duas posições depende apenas do deslocamento entre elas.
"""
import numpy as np


def positional_encoding(n_pos, d, base=10000.0):
    pos = np.arange(n_pos)[:, None]
    i = np.arange(d)[None, :]
    angulo = pos / (base ** (2 * (i // 2) / d))
    pe = np.zeros((n_pos, d))
    pe[:, 0::2] = np.sin(angulo[:, 0::2])
    pe[:, 1::2] = np.cos(angulo[:, 1::2])
    return pe


pe = positional_encoding(12, 16)
for k in range(6):
    print(f"k={k}: PE[0]·PE[{k}] = {pe[0] @ pe[k]:.4f}")
print("PE[2]·PE[5] == PE[4]·PE[7] (k=3):", bool(np.isclose(pe[2] @ pe[5], pe[4] @ pe[7])))
