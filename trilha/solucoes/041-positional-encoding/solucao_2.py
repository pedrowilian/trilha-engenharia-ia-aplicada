"""Solução de referência — Exercício 2 da Lição 041.

Soma o positional encoding ao embedding de um token e mostra que a mesma palavra
em posições diferentes recebe representações distintas.
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


e = np.array([1.0, 0.0, 0.0, 0.0])
pe = positional_encoding(4, 4)
rep0 = e + pe[0]
rep2 = e + pe[2]
print("token na posicao 0:", np.round(rep0, 4))
print("token na posicao 2:", np.round(rep2, 4))
print("representacoes diferentes:", not np.allclose(rep0, rep2))
