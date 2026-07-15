"""Solução de referência — Exercício 1 da Lição 041.

Constrói o positional encoding sinusoidal e inspeciona shape, faixa de valores
e a linha de uma posição.
"""
import numpy as np

np.set_printoptions(precision=4, suppress=True)


def positional_encoding(n_pos, d, base=10000.0):
    pos = np.arange(n_pos)[:, None]
    i = np.arange(d)[None, :]
    angulo = pos / (base ** (2 * (i // 2) / d))
    pe = np.zeros((n_pos, d))
    pe[:, 0::2] = np.sin(angulo[:, 0::2])
    pe[:, 1::2] = np.cos(angulo[:, 1::2])
    return pe


pe = positional_encoding(6, 8)
print("shape:", pe.shape)
print(f"min: {pe.min():.4f}  max: {pe.max():.4f}")
print("PE[posicao 1] =", np.round(pe[1], 4))
