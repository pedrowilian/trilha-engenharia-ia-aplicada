"""Exercicio 3 - Metrica offline versus online.

Setup (dado):
    offline_total = 10 ; offline_acertos = 9        # dataset rotulado
    online_total = 500 ; online_positivos = 310     # polegares para cima reais

Tarefa:
    Calcule offline_acc = acertos/total e online_sat = positivos/total, depois a
    lacuna = offline_acc - online_sat. Imprima, nesta ordem:
    "offline accuracy: <4 casas> (<acertos>/<total>)",
    "online satisfacao: <4 casas> (<positivos>/<total>)",
    "lacuna offline-online: <sinal+4 casas>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/086-metricas-datasets-avaliacao/solucao_3.saida.txt
"""

offline_total = 10
offline_acertos = 9
online_total = 500
online_positivos = 310

# TODO: calcule as duas metricas e a lacuna, e imprima no formato pedido.
