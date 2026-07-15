"""Exercicio 1 - Modelo de custo por tokens.

Setup (dado):
    preco_entrada = 1.00 / 1_000_000   # $ por token de entrada
    preco_saida   = 3.00 / 1_000_000   # $ por token de saida
    tokens_entrada = 1200 ; tokens_saida = 300
    req_por_dia = 20_000

Tarefa:
    Calcule custo_req = entrada*preco_entrada + saida*preco_saida e projete o
    custo diario (custo_req * req_por_dia) e mensal (x30). Imprima, nesta ordem:
    "custo por requisicao: $<6 casas>", "custo diario: $<2 casas>",
    "custo mensal (30 dias): $<2 casas>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/087-custo-inferencia/solucao_1.saida.txt
"""

preco_entrada = 1.00 / 1_000_000
preco_saida = 3.00 / 1_000_000
tokens_entrada = 1200
tokens_saida = 300
req_por_dia = 20_000

# TODO: calcule o custo por requisicao e as projecoes, e imprima no formato pedido.
