"""Solução de referência — Exercício 1 da Lição 094.

Comparação de custo mensal entre dois níveis de modelo e a economia relativa de
trocar o maior pelo menor. Determinístico.
"""
modelos = {"grande": 0.030, "pequeno": 0.006}   # $ por 1k tokens
tokens_mes = 150_000_000                          # tokens por mes

for nome, preco_1k in modelos.items():
    custo = tokens_mes / 1000 * preco_1k
    print(f"{nome:>8}: ${custo:,.2f}/mes")

economia = (modelos["grande"] - modelos["pequeno"]) / modelos["grande"]
print(f"economia ao trocar para o pequeno: {economia:.0%}")
