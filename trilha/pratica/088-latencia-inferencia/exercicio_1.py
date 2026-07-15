"""Exercicio 1 - Decomposicao de latencia e streaming.

Setup (dado):
    ttft_ms = 250 ; tempo_por_token_ms = 15 ; tokens_saida = 200

Tarefa:
    Calcule latencia_total = ttft_ms + tokens_saida * tempo_por_token_ms. A
    latencia percebida com streaming e o proprio TTFT. Imprima, nesta ordem:
    "TTFT: <n> ms", "latencia total (sem streaming): <n> ms",
    "latencia percebida (streaming, ate 1o token): <n> ms",
    "reducao percebida: <1 casa>%" (= (1 - ttft/total)*100).

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/088-latencia-inferencia/solucao_1.saida.txt
"""

ttft_ms = 250
tempo_por_token_ms = 15
tokens_saida = 200

# TODO: calcule a latencia total e a reducao percebida, e imprima no formato pedido.
