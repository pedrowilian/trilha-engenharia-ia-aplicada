"""Solucao de referencia - Exercicio 2 da Licao 087.

Caching: requisicoes repetidas que batem no cache custam ~0. Com uma taxa de
acerto (hit rate) h, o custo efetivo cai por um fator (1 - h). O modelo mostra a
economia direta de um cache semantico/exato sob alto volume.
"""

custo_req = 0.0021
hit_rate = 0.30
req_por_dia = 20_000

custo_sem_cache = custo_req * req_por_dia
custo_com_cache = custo_req * req_por_dia * (1 - hit_rate)
economia = custo_sem_cache - custo_com_cache

print(f"custo/dia sem cache: ${custo_sem_cache:.2f}")
print(f"custo/dia com cache (hit {hit_rate:.0%}): ${custo_com_cache:.2f}")
print(f"economia diaria: ${economia:.2f} ({economia / custo_sem_cache:.0%})")
