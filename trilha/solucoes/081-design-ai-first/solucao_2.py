"""Solução de referência — Exercício 2 da Lição 081.

Escolha de solução por utilidade ponderada sobre precisão/latência/custo.
"""
import numpy as np

nomes = ["regra", "leve", "forte"]
M = np.array([
    [0.70, 8.0, 0.2],
    [0.90, 200.0, 1.5],
    [0.97, 900.0, 7.0],
])

prec = M[:, 0]
lat_norm = M[:, 1] / M[:, 1].max()
custo_norm = M[:, 2] / M[:, 2].max()
utilidade = 0.6 * prec - 0.25 * lat_norm - 0.15 * custo_norm

for nome, u in zip(nomes, utilidade):
    print(f"{nome:>6}: utilidade={u:.3f}")

melhor = nomes[int(np.argmax(utilidade))]
print("escolhido:", melhor)
