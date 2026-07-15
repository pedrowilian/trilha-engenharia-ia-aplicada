"""Exercício 1 — Comparação de custo entre níveis de modelo.

Setup: `modelos = {"grande": 0.030, "pequeno": 0.006}` ($ por 1k tokens) e
`tokens_mes = 150_000_000` (no esqueleto).

Tarefa:
    Para cada modelo, calcule o custo mensal (`tokens_mes / 1000 * preco_1k`) e
    imprima `"{nome:>8}: ${custo:,.2f}/mes"`. Calcule e imprima a economia
    relativa de trocar o grande pelo pequeno:
    `"economia ao trocar para o pequeno: {economia:.0%}"`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/094-custos-sustentabilidade/solucao_1.saida.txt
"""

# TODO: calcule o custo mensal de cada modelo e a economia relativa.
