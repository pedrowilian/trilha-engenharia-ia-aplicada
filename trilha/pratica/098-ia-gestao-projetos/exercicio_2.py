"""Exercício 2 — Estimativa de prazo por Monte Carlo.

Setup: rng = np.random.default_rng(7), tarefas = [(1, 2, 4), (2, 4, 7)],
n = 10000.

Tarefa:
    Some `n` amostras de duração triangular (otimista, provável, pessimista) por
    tarefa, formando a distribuição do prazo total. Imprima
    `p50: {valor:.1f} dias` e `p85: {valor:.1f} dias` (use np.percentile).

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/098-ia-gestao-projetos/solucao_2.saida.txt.
"""
import numpy as np

rng = np.random.default_rng(7)
tarefas = [(1, 2, 4), (2, 4, 7)]
n = 10000

# TODO: some as duracoes triangulares e imprima p50 e p85.
