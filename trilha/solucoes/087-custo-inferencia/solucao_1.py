"""Solucao de referencia - Exercicio 1 da Licao 087.

Modelo de custo por tokens: o custo de uma requisicao e a soma do custo dos
tokens de entrada e de saida, cada um a seu preco. A partir do custo unitario,
projeta-se o custo diario e mensal sob um volume fixo.
"""

preco_entrada = 1.00 / 1_000_000   # $ por token de entrada
preco_saida = 3.00 / 1_000_000     # $ por token de saida (geralmente mais caro)
tokens_entrada = 1200
tokens_saida = 300

custo_req = tokens_entrada * preco_entrada + tokens_saida * preco_saida
req_por_dia = 20_000
custo_mensal = custo_req * req_por_dia * 30

print(f"custo por requisicao: ${custo_req:.6f}")
print(f"custo diario: ${custo_req * req_por_dia:.2f}")
print(f"custo mensal (30 dias): ${custo_mensal:.2f}")
