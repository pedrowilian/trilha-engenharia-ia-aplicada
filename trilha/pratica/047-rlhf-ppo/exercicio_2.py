"""Exercício 2 — Recompensa efetiva com penalidade KL.

Setup: a recompensa do reward model por amostra (`r`), a divergência KL contra a
referência (`kl`) e o peso `beta`, abaixo.

Tarefa:
    Calcule a recompensa efetiva r_efetiva = r - beta * kl e imprima cada amostra
    (`r` e `r_efetiva` com sinal; `kl` com 2 casas) e a
    `recompensa efetiva media` (4 casas).

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/047-rlhf-ppo/solucao_2.saida.txt
"""
import numpy as np

r = np.array([2.0, 1.0, -0.5, 0.4])
kl = np.array([0.5, 3.0, 0.2, 1.0])
beta = 0.2

# TODO: calcular r_efetiva e imprimir os resultados.
