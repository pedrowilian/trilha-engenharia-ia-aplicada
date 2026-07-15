"""Exercicio 2 - Economia por caching (hit rate).

Setup (dado):
    custo_req = 0.0021 ; hit_rate = 0.30 ; req_por_dia = 20_000

Tarefa:
    Calcule o custo/dia sem cache (custo_req * req_por_dia) e com cache
    (multiplicado por (1 - hit_rate)), e a economia diaria. Imprima, nesta ordem:
    "custo/dia sem cache: $<2 casas>",
    "custo/dia com cache (hit <hit_rate como %>): $<2 casas>",
    "economia diaria: $<2 casas> (<percentual da economia>)".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/087-custo-inferencia/solucao_2.saida.txt
"""

custo_req = 0.0021
hit_rate = 0.30
req_por_dia = 20_000

# TODO: calcule os custos com/sem cache e a economia, e imprima no formato pedido.
