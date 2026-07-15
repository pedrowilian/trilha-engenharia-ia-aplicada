"""Exercício 1 — Perda do DPO a partir de log-probs.

Setup: as log-probabilidades (somadas sobre a resposta) da política e da
referência, e o `beta`, abaixo.

Tarefa:
    Calcule as recompensas implícitas r = beta * (logp_pi - logp_ref) para a
    resposta escolhida e a rejeitada, a margem e a perda -log sigmoid(margem).
    Imprima `r_chosen`, `r_rejected`, `margem` (com sinal, 4 casas) e
    `perda DPO` (4 casas).

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/048-dpo-vs-ppo/solucao_1.saida.txt
"""
import numpy as np


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


logp_pi = {"chosen": -1.5, "rejected": -3.0}
logp_ref = {"chosen": -2.0, "rejected": -2.0}
beta = 0.1

# TODO: calcular as recompensas implicitas, a margem, a perda DPO e imprimir.
