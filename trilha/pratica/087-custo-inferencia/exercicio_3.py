"""Exercicio 3 - Amortizacao de overhead por batching.

Setup (dado):
    custo_variavel = 0.0021     # $ por requisicao (tokens)
    overhead_chamada = 0.0090   # $ fixo por chamada/lote
    lotes = [1, 5, 10, 50]

Tarefa:
    Para cada tamanho de lote, calcule custo_por_req = custo_variavel +
    overhead_chamada / lote e imprima "lote=<lote alinhado em 2>: custo/req=$<6 casas>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/087-custo-inferencia/solucao_3.saida.txt
"""

custo_variavel = 0.0021
overhead_chamada = 0.0090
lotes = [1, 5, 10, 50]

# TODO: itere sobre os lotes, calcule o custo por requisicao e imprima no formato pedido.
