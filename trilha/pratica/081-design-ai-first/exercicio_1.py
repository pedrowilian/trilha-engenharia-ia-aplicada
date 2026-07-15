"""Exercício 1 — Triagem IA vs regras.

Setup:
    problemas = [
        ("checar CEP", True, False, False),
        ("resumir contrato", False, True, True),
        ("traduzir frase", False, True, False),
        ("somar valores", True, False, False),
    ]
    Cada tupla é (nome, regras_cobrem, entrada_ambigua, custo_erro_alto).

Tarefa:
    Implemente `decidir_abordagem(regras_cobrem, entrada_ambigua, custo_erro_alto)`
    seguindo a triagem AI-First (regras -> ia -> ia+humano) e imprima
    `{nome:>18}: {decisao}` para cada problema.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/081-design-ai-first/solucao_1.saida.txt
"""

problemas = [
    ("checar CEP", True, False, False),
    ("resumir contrato", False, True, True),
    ("traduzir frase", False, True, False),
    ("somar valores", True, False, False),
]

# TODO: implemente decidir_abordagem(...) e imprima a decisão de cada problema.
