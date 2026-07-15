"""Solução de referência — Exercício 2 da Lição 098.

Estimativa por Monte Carlo: soma de durações triangulares (otimista, provável,
pessimista) por tarefa, com semente fixa para reprodutibilidade.
"""
import numpy as np

rng = np.random.default_rng(7)
tarefas = [(1, 2, 4), (2, 4, 7)]
n = 10000
totais = np.zeros(n)
for (o, m, p) in tarefas:
    totais += rng.triangular(o, m, p, size=n)

p50 = np.percentile(totais, 50)
p85 = np.percentile(totais, 85)
print(f"p50: {p50:.1f} dias")
print(f"p85: {p85:.1f} dias")
