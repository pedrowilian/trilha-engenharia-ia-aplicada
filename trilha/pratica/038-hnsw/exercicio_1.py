"""Exercício 1 — Busca greedy em grafo navegável.

Setup:
    coords = {i: [float(i), 0.0] for i in range(7)}
    grafo = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [2, 4, 0, 6],
             4: [3, 5], 5: [4, 6], 6: [5, 3]}
    q = [4.2, 0.0]   # entrada no nó 0

Tarefa:
    Implemente greedy(q, entrada) que salta para o vizinho mais próximo
    (desempate por id) até estabilizar. Imprima o caminho e o nó final com a
    distância. Esperado: caminho [0, 3, 4]; nó 4 a dist 0.2000.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/038-hnsw/solucao_1.saida.txt
"""
import math

coords = {i: [float(i), 0.0] for i in range(7)}
grafo = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [2, 4, 0, 6],
         4: [3, 5], 5: [4, 6], 6: [5, 3]}
q = [4.2, 0.0]

# TODO: implementar dist e greedy(q, entrada) e imprimir o caminho e o nó final.
