"""Exercício 2 — Latência sequencial vs paralela.

Setup:
    duracoes = [150, 90, 300, 120, 60]   # ms por subtarefa
    coordenacao = 70                     # ms de overhead do supervisor

Tarefa:
    Calcule `lat_single` como a soma das durações e `lat_multi` como
    `max + coordenacao` (use inteiros). Imprima
    `latencia single (sequencial): {ls}`, `latencia multi (paralelo): {lm}`
    e `ganho: {ls - lm}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/082-single-vs-multi-agente/solucao_2.saida.txt
"""
import numpy as np

duracoes = np.array([150, 90, 300, 120, 60])
coordenacao = 70

# TODO: compare a latência sequencial (soma) com a paralela (max + overhead).
