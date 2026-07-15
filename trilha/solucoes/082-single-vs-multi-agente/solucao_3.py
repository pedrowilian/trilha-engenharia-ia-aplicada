"""Solução de referência — Exercício 3 da Lição 082.

Critério de decisão: multi só vence com especialização E paralelismo E orçamento.
"""


def decidir(n_competencias, lat_single, lat_multi, custo_extra, orcamento_extra):
    paraleliza = lat_multi < lat_single
    especializa = n_competencias >= 2
    cabe_orcamento = custo_extra <= orcamento_extra
    if especializa and paraleliza and cabe_orcamento:
        return "multi-agente"
    return "single-agente"


casos = [
    ("chat suporte", 1, 200, 180, 50, 100),
    ("rag+sumario", 2, 500, 260, 80, 100),
    ("pipeline dados", 3, 900, 400, 250, 100),
]

for nome, comp, ls, lm, ce, orc in casos:
    print(f"{nome:>16}: {decidir(comp, ls, lm, ce, orc)}")
