"""Exercicio 1 - Precisao, revocacao e F1.

Setup (dado):
    relevantes  = {"d2", "d4", "d6"}        # gabarito
    recuperados = {"d1", "d2", "d3", "d4"}  # saida do sistema

Tarefa:
    Calcule TP/FP/FN por operacoes de conjunto, depois precisao = TP/(TP+FP),
    revocacao = TP/(TP+FN) e F1 = 2*P*R/(P+R). Imprima, nesta ordem:
    "TP=<n> FP=<n> FN=<n>", "precisao: <4 casas>", "revocacao: <4 casas>",
    "f1: <4 casas>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/086-metricas-datasets-avaliacao/solucao_1.saida.txt
"""

relevantes = {"d2", "d4", "d6"}
recuperados = {"d1", "d2", "d3", "d4"}

# TODO: calcule TP/FP/FN e as metricas, e imprima no formato pedido.
