"""Exercício 3 — Política HITL + approval gate.

Setup:
    acoes = [
        ("ler documento", 0.70, False),
        ("excluir base", 0.99, True),
        ("sugerir resposta", 0.91, False),
        ("alterar permissao", 0.40, True),
    ]
    limiar = 0.8
    Campos: (nome, confianca, risco_alto).

Tarefa:
    Implemente `rotear_acao(confianca, risco_alto, limiar)` (risco alto ->
    "aprovacao"; senão confiança >= limiar -> "automatico", senão
    "revisao_humana"). Imprima `{nome:>18}: {via}` e, ao final,
    `contagem: {dict}` com as chaves na ordem automatico, revisao_humana,
    aprovacao.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/083-padroes-design-ia/solucao_3.saida.txt
"""

acoes = [
    ("ler documento", 0.70, False),
    ("excluir base", 0.99, True),
    ("sugerir resposta", 0.91, False),
    ("alterar permissao", 0.40, True),
]
limiar = 0.8

# TODO: implemente rotear_acao(...) e conte os destinos das ações.
