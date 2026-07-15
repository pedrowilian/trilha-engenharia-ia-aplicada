"""Exercício 1 — Perda de preferência do reward model (Bradley-Terry).

Setup: as recompensas atribuídas pelo reward model às respostas escolhida (w) e
rejeitada (l), abaixo.

Tarefa:
    Calcule a margem (r_chosen - r_rejected), a perda de Bradley-Terry por par
    (-log sigmoid(margem)) e a perda média. Imprima cada par (`margem` com sinal
    e 2 casas, `perda` com 4 casas) e a `perda media` (4 casas).

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/047-rlhf-ppo/solucao_1.saida.txt
"""
import numpy as np


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


r_chosen = np.array([3.0, 0.5, 2.0, -0.5])
r_rejected = np.array([1.0, 1.5, 2.0, -1.5])

# TODO: calcular margens, perdas de Bradley-Terry e imprimir os resultados.
