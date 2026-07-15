"""Exercício 3 — Critério de decisão.

Setup:
    casos = [
        ("chat suporte", 1, 200, 180, 50, 100),
        ("rag+sumario", 2, 500, 260, 80, 100),
        ("pipeline dados", 3, 900, 400, 250, 100),
    ]
    Campos: (nome, n_competencias, lat_single, lat_multi, custo_extra, orcamento_extra).

Tarefa:
    Implemente `decidir(n_competencias, lat_single, lat_multi, custo_extra,
    orcamento_extra)` que devolve "multi-agente" apenas quando há
    especialização (>= 2), ganho de latência (lat_multi < lat_single) e o
    custo extra cabe no orçamento. Imprima `{nome:>16}: {decisao}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/082-single-vs-multi-agente/solucao_3.saida.txt
"""

casos = [
    ("chat suporte", 1, 200, 180, 50, 100),
    ("rag+sumario", 2, 500, 260, 80, 100),
    ("pipeline dados", 3, 900, 400, 250, 100),
]

# TODO: implemente decidir(...) e imprima a escolha de cada caso.
