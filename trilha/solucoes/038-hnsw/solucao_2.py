"""Solução de referência — Exercício 2 da Lição 038.

Busca hierárquica em duas camadas (estilo HNSW): a camada de cima é esparsa e
permite saltos longos; a de baixo tem todos os nós e refina o resultado. Compara
o número de saltos (hops) com a busca de camada única.
"""
import math


def dist(u, v):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(u, v)))


coords = {i: [float(i), 0.0] for i in range(10)}
layer0 = {i: [j for j in (i - 1, i + 1) if 0 <= j <= 9] for i in range(10)}
layer1 = {0: [5], 5: [0, 9], 9: [5]}
q = [8.3, 0.0]


def greedy_em(grafo, q, entrada):
    atual, hops = entrada, 0
    while True:
        melhor = min([atual] + grafo[atual], key=lambda n: (dist(q, coords[n]), n))
        if melhor == atual:
            break
        atual, hops = melhor, hops + 1
    return atual, hops


no_sl, hops_sl = greedy_em(layer0, q, 0)
entrada1, hops1 = greedy_em(layer1, q, 0)
no_h, hops0 = greedy_em(layer0, q, entrada1)
print(f"single-layer: no={no_sl} hops={hops_sl}")
print(f"hierarquico:  no={no_h} hops={hops1 + hops0} (L1={hops1} + L0={hops0})")
