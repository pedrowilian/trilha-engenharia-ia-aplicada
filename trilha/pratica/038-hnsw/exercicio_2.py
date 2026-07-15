"""Exercício 2 — Camadas hierárquicas reduzem saltos.

Setup:
    coords = {i: [float(i), 0.0] for i in range(10)}
    layer0 = cadeia (cada nó ligado a i-1 e i+1)
    layer1 = {0: [5], 5: [0, 9], 9: [5]}   # esparsa, com saltos longos
    q = [8.3, 0.0]   # entrada no nó 0

Tarefa:
    Implemente greedy_em(grafo, q, entrada) contando saltos (hops). Compare a
    busca de camada única (só layer0) com a hierárquica (layer1 e depois
    layer0). Esperado: single-layer hops=8; hierarquico hops=3.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/038-hnsw/solucao_2.saida.txt
"""
import math

coords = {i: [float(i), 0.0] for i in range(10)}
layer0 = {i: [j for j in (i - 1, i + 1) if 0 <= j <= 9] for i in range(10)}
layer1 = {0: [5], 5: [0, 9], 9: [5]}
q = [8.3, 0.0]

# TODO: implementar greedy_em e comparar single-layer com hierárquico.
