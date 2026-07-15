"""Solução de referência — Exercício 3 da Lição 083.

Política HITL + approval gate: risco tem prioridade; senão, a confiança decide.
"""


def rotear_acao(confianca, risco_alto, limiar):
    if risco_alto:
        return "aprovacao"
    if confianca >= limiar:
        return "automatico"
    return "revisao_humana"


acoes = [
    ("ler documento", 0.70, False),
    ("excluir base", 0.99, True),
    ("sugerir resposta", 0.91, False),
    ("alterar permissao", 0.40, True),
]
limiar = 0.8

contagem = {"automatico": 0, "revisao_humana": 0, "aprovacao": 0}
for nome, conf, risco in acoes:
    via = rotear_acao(conf, risco, limiar)
    contagem[via] += 1
    print(f"{nome:>18}: {via}")

print("contagem:", contagem)
