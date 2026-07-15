"""Exercício 3 — Efeito do parâmetro ef.

Setup:
    coords = {"e": [0.0, 0.0], "A": [1.0, 1.0], "B": [1.0, -1.0],
              "C": [2.0, 2.0], "T": [3.0, 0.0]}
    grafo = {"e": ["A", "B"], "A": ["e", "C"], "B": ["e", "T"],
             "C": ["A"], "T": ["B"]}
    q = [3.1, 0.0]   # entrada em "e"; o nó exato é "T"

Tarefa:
    Implemente search_layer(q, entrada, ef) (busca em feixe do HNSW: mantém os
    ef melhores candidatos; para quando o melhor candidato a expandir é pior que
    o pior do resultado). Varra ef em {1, 2, 3} e imprima o nó achado, as
    comparações e se acertou o exato. Esperado: ef=1 erra em C; ef>=2 acerta T.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/038-hnsw/solucao_3.saida.txt
"""
import math

coords = {"e": [0.0, 0.0], "A": [1.0, 1.0], "B": [1.0, -1.0],
          "C": [2.0, 2.0], "T": [3.0, 0.0]}
grafo = {"e": ["A", "B"], "A": ["e", "C"], "B": ["e", "T"],
         "C": ["A"], "T": ["B"]}
q = [3.1, 0.0]

# TODO: implementar search_layer(q, entrada, ef) e varrer ef em {1, 2, 3}.
