"""Exercício 3 — Alavancas de otimização acumuladas.

Setup: `base = 4500.0` e
`alavancas = [("cache 30%", 0.70), ("modelo menor", 0.50), ("batching", 0.90)]`
(no esqueleto).

Tarefa:
    Comece em `custo = base`, imprima `"baseline: ${custo:,.2f}"` e, para cada
    alavanca, multiplique o custo pelo fator e imprima
    `"+ {nome:>13}: ${custo:,.2f}"`. Ao final, imprima
    `"reducao total: {(1 - custo / base):.0%}"`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/094-custos-sustentabilidade/solucao_3.saida.txt
"""

# TODO: aplique as alavancas multiplicativas e calcule a redução total.
