"""Solucao de referencia - Exercicio 3 da Licao 087.

Batching: um overhead fixo por chamada (infra, rede, agendamento) e diluido
entre as requisicoes do lote. O custo por requisicao tende ao custo variavel
conforme o lote cresce - amortizacao classica de overhead.
"""

custo_variavel = 0.0021     # $ por requisicao (tokens)
overhead_chamada = 0.0090   # $ fixo por chamada/lote

for lote in [1, 5, 10, 50]:
    custo_por_req = custo_variavel + overhead_chamada / lote
    print(f"lote={lote:>2}: custo/req=${custo_por_req:.6f}")
