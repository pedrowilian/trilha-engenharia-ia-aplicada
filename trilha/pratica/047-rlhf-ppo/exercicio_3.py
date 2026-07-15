"""Exercício 3 — Objetivo clipado do PPO.

Setup: a razão de probabilidade nova/antiga (`ratio`), a vantagem estimada (`A`)
e o `eps` do clipping, abaixo.

Tarefa:
    Calcule o termo não-clipado (ratio*A), o clipado (clip(ratio, 1-eps, 1+eps)*A)
    e o objetivo L_clip = min dos dois. Imprima cada `i` (`ratio` com 2 casas, `A`
    com sinal, `L_clip` com 4 casas) e o `objetivo PPO (media)` (4 casas).

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/047-rlhf-ppo/solucao_3.saida.txt
"""
import numpy as np


def clip(x, lo, hi):
    return np.minimum(np.maximum(x, lo), hi)


ratio = np.array([1.30, 0.70, 1.05, 0.90])
A = np.array([1.0, 1.0, -1.0, -1.0])
eps = 0.2

# TODO: calcular o objetivo clipado do PPO e imprimir os resultados.
