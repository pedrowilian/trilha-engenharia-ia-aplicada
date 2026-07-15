"""Solução de referência — Exercício 1 da Lição 038.

Busca greedy num grafo de vizinhança navegável (NSW): a cada passo, move-se para
o vizinho mais próximo da consulta; para quando nenhum vizinho melhora. É o
mecanismo básico da camada de busca do HNSW.
"""
import math


def dist(u, v):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(u, v)))


coords = {i: [float(i), 0.0] for i in range(7)}
grafo = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [2, 4, 0, 6],
         4: [3, 5], 5: [4, 6], 6: [5, 3]}
q = [4.2, 0.0]


def greedy(q, entrada):
    atual = entrada
    caminho = [atual]
    while True:
        melhor = min([atual] + grafo[atual], key=lambda n: (dist(q, coords[n]), n))
        if melhor == atual:
            break
        atual = melhor
        caminho.append(atual)
    return atual, caminho


no, caminho = greedy(q, 0)
print("caminho:", caminho)
print("no encontrado:", no, f"(dist {dist(q, coords[no]):.4f})")
