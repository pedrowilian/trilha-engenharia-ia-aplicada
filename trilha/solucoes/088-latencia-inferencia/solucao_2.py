"""Solucao de referencia - Exercicio 2 da Licao 088.

Percentis de latencia pelo metodo nearest-rank (deterministico): ordena as
amostras e seleciona a posicao teto(p/100 * n). Os percentis revelam a cauda que
a media esconde - p95/p99 sao o que o usuario sente nos piores casos.
"""
import math


def percentil(amostras, p):
    ordenado = sorted(amostras)
    n = len(ordenado)
    rank = math.ceil(p / 100 * n)
    rank = max(1, min(rank, n))
    return ordenado[rank - 1]


latencias = [200, 210, 190, 205, 195, 800, 215, 198, 202, 207, 199, 700]
for p in [50, 95, 99]:
    print(f"p{p}: {percentil(latencias, p)} ms")
media = sum(latencias) / len(latencias)
print(f"media: {media:.1f} ms")
print(f"max: {max(latencias)} ms")
