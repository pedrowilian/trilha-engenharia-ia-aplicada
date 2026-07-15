"""Exercício 2 — Quando cosseno e L2 discordam.

Setup:
    q = [1.0, 1.0]
    docs = {"A": [8.0, 8.0], "B": [1.0, 0.0], "C": [0.0, 3.0]}

Tarefa:
    Produza o ranking por cosseno (decrescente) e por L2 (crescente), ambos
    com desempate alfabético, e imprima o topo de cada um e se discordam.
    Esperado: top cosseno=A top L2=B; os rankings discordam: True.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/035-metricas-distancia-similaridade/solucao_2.saida.txt
"""
import math

q = [1.0, 1.0]
docs = {"A": [8.0, 8.0], "B": [1.0, 0.0], "C": [0.0, 3.0]}

# TODO: implementar cos_sim e l2, ranquear e comparar os dois rankings.
