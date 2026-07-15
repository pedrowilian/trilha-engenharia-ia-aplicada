"""Exercício 3 — Relatório de backlog por MoSCoW.

Setup:
    backlog = [
        {"titulo": "API", "moscow": "Must", "feito": True},
        {"titulo": "Docs", "moscow": "Should", "feito": True},
        {"titulo": "i18n", "moscow": "Could", "feito": False},
        {"titulo": "SSO", "moscow": "Must", "feito": False},
        {"titulo": "Tema", "moscow": "Could", "feito": False},
    ]

Tarefa:
    Implemente `relatorio(backlog)` que conta itens por classe MoSCoW e calcula
    o percentual concluído. Imprima `Must:`, `Should:`, `Could:` e
    `progresso: {pct:.0f}%`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/098-ia-gestao-projetos/solucao_3.saida.txt.
"""

backlog = [
    {"titulo": "API", "moscow": "Must", "feito": True},
    {"titulo": "Docs", "moscow": "Should", "feito": True},
    {"titulo": "i18n", "moscow": "Could", "feito": False},
    {"titulo": "SSO", "moscow": "Must", "feito": False},
    {"titulo": "Tema", "moscow": "Could", "feito": False},
]

# TODO: implemente relatorio e imprima as contagens e o progresso.
