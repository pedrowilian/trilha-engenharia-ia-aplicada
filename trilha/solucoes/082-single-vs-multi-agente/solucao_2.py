"""Solução de referência — Exercício 2 da Lição 082.

Latência: single = soma sequencial; multi = max paralelo + coordenação.
"""
import numpy as np

duracoes = np.array([150, 90, 300, 120, 60])
coordenacao = 70

lat_single = int(duracoes.sum())
lat_multi = int(duracoes.max() + coordenacao)

print("latencia single (sequencial):", lat_single)
print("latencia multi (paralelo):", lat_multi)
print("ganho:", lat_single - lat_multi)
