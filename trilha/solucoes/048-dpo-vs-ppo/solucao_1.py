"""Solução de referência — Exercício 1 da Lição 048.

Perda do DPO a partir das log-probabilidades da política e da referência, via a
recompensa implícita r = beta * (logp_pi - logp_ref).
"""
import numpy as np


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


# Log-probs (somadas sobre a resposta) da política e da referência.
logp_pi = {"chosen": -1.5, "rejected": -3.0}
logp_ref = {"chosen": -2.0, "rejected": -2.0}
beta = 0.1

r_chosen = beta * (logp_pi["chosen"] - logp_ref["chosen"])
r_rejected = beta * (logp_pi["rejected"] - logp_ref["rejected"])
perda = -np.log(sigmoid(r_chosen - r_rejected))
print(f"r_chosen   = {r_chosen:+.4f}")
print(f"r_rejected = {r_rejected:+.4f}")
print(f"margem     = {r_chosen - r_rejected:+.4f}")
print(f"perda DPO  = {perda:.4f}")
