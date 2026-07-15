"""Solução de referência — Exercício 3 da Lição 048.

Perda DPO média e acurácia de preferência sobre um batch de pares, a partir dos
log-ratios (logp_pi - logp_ref) de cada resposta.
"""
import numpy as np


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


# Log-ratios (logp_pi - logp_ref) para resposta escolhida (h_w) e rejeitada (h_l).
h_w = np.array([0.8, 0.1, -0.2, 1.0, 0.3])
h_l = np.array([0.2, 0.4, -0.5, 0.5, 0.3])
beta = 0.2

margem = beta * (h_w - h_l)
perda = -np.log(sigmoid(margem)).mean()
acuracia = (margem > 0).mean()
print("margens:", np.round(margem, 4).tolist())
print(f"perda DPO media = {perda:.4f}")
print(f"acuracia de preferencia = {acuracia:.2f}")
