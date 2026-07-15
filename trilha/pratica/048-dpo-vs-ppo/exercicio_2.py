"""Exercício 2 — Efeito de beta sobre a perda do DPO.

Setup: uma diferença de log-ratios fixa `delta` e a lista de valores de `beta`,
abaixo.

Tarefa:
    Para cada `beta`, calcule a margem efetiva beta*delta e a perda
    -log sigmoid(margem). Imprima `beta`, `margem` (3 casas) e `perda` (4 casas).

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/048-dpo-vs-ppo/solucao_2.saida.txt
"""
import numpy as np


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


delta = 2.0
betas = [0.05, 0.1, 0.5]

# TODO: para cada beta, calcular margem e perda e imprimir os resultados.
