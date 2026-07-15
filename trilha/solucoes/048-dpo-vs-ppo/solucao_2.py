"""Solução de referência — Exercício 2 da Lição 048.

Efeito de beta sobre a perda do DPO para uma diferença de log-ratios fixa.
"""
import numpy as np


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


# Diferenca de log-ratios entre escolhida e rejeitada (fixa); variamos beta.
delta = 2.0
for beta in [0.05, 0.1, 0.5]:
    margem = beta * delta
    perda = -np.log(sigmoid(margem))
    print(f"beta={beta}: margem={margem:.3f} perda={perda:.4f}")
