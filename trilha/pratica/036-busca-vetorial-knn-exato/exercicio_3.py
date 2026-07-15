"""Exercício 3 — Custo O(n·d) da busca exata.

Setup:
    vetores = {f"v{i}": [i, i+1, i+2, i+3] for i in range(8)}   # 8 vetores 4D
    q = [3.0, 3.0, 3.0, 3.0]

Tarefa:
    Instrumente a distância com um contador (classe BaseVetorial com
    calculos_distancia). Faça a busca exata e imprima o vizinho mais próximo,
    o número de cálculos de distância e o custo n*d.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/036-busca-vetorial-knn-exato/solucao_3.saida.txt
    (calculos de distancia: 8; custo O(n*d) = 8 * 4 = 32).
"""
import math

vetores = {f"v{i}": [i, i + 1, i + 2, i + 3] for i in range(8)}
q = [3.0, 3.0, 3.0, 3.0]

# TODO: criar BaseVetorial com contador, fazer busca_exata e imprimir o custo.
