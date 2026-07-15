"""Exercício 3 — Perda média e acurácia de preferência num batch.

Setup: os log-ratios (logp_pi - logp_ref) da resposta escolhida (`h_w`) e da
rejeitada (`h_l`) para cada par do batch, e o `beta`, abaixo.

Tarefa:
    Calcule margem = beta*(h_w - h_l), a perda DPO média (-log sigmoid(margem)) e
    a acurácia de preferência (fração de margens > 0). Imprima `margens` (lista,
    4 casas), `perda DPO media` (4 casas) e `acuracia de preferencia` (2 casas).

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/048-dpo-vs-ppo/solucao_3.saida.txt
"""
import numpy as np


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


h_w = np.array([0.8, 0.1, -0.2, 1.0, 0.3])
h_l = np.array([0.2, 0.4, -0.5, 0.5, 0.3])
beta = 0.2

# TODO: calcular margens, perda DPO media, acuracia e imprimir os resultados.
