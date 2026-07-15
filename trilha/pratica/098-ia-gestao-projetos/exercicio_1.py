"""Exercício 1 — Priorização de backlog por RICE.

Setup:
    itens = [
        ("relatorios", 6000, 1.5, 0.9, 3.0),
        ("alertas", 4000, 2.0, 0.8, 4.0),
        ("temas", 1000, 0.5, 1.0, 1.0),
    ]

Tarefa:
    Implemente `rice(reach, impact, confidence, effort)` = (R*I*C)/E e ordene os
    itens por score decrescente. Imprima `nome: RICE={score:.0f}` para cada item.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/098-ia-gestao-projetos/solucao_1.saida.txt.
"""

itens = [
    ("relatorios", 6000, 1.5, 0.9, 3.0),
    ("alertas", 4000, 2.0, 0.8, 4.0),
    ("temas", 1000, 0.5, 1.0, 1.0),
]

# TODO: implemente rice, ordene por score decrescente e imprima cada item.
