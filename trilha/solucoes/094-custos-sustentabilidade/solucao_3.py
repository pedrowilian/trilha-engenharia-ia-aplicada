"""Solução de referência — Exercício 3 da Lição 094.

Alavancas de otimização acumuladas: cada alavanca multiplica o custo mensal por
um fator; a redução total é o efeito combinado. Determinístico.
"""
base = 4500.0
alavancas = [("cache 30%", 0.70), ("modelo menor", 0.50), ("batching", 0.90)]

custo = base
print(f"baseline: ${custo:,.2f}")
for nome, fator in alavancas:
    custo *= fator
    print(f"+ {nome:>13}: ${custo:,.2f}")
print(f"reducao total: {(1 - custo / base):.0%}")
