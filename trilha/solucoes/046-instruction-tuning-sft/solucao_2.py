"""Solução de referência — Exercício 2 da Lição 046.

Perda mascarada do SFT: cross-entropy média apenas sobre os tokens da resposta.
"""
import numpy as np

p_alvo = np.array([0.4, 0.7, 0.3, 0.95, 0.5, 0.6])
mascara = np.array([0, 0, 0, 1, 1, 1])

nll = -np.log(p_alvo)
perda_mascarada = (nll * mascara).sum() / mascara.sum()

print("nll por token   :", np.round(nll, 4).tolist())
print("tokens de resposta:", int(mascara.sum()))
print(f"perda mascarada   = {perda_mascarada:.4f}")
