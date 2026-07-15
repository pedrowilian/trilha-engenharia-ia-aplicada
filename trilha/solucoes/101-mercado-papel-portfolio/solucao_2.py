"""Solucao de referencia - Exercicio 2 da Licao 101.

Pontua repositorios de portfolio por sinais ponderados (README, testes, CI,
docs, demo). O recrutador le sinais de engenharia, nao conta linhas: um repo
testado e documentado vale mais que dez notebooks soltos.
"""

PESOS = {"readme": 2, "testes": 3, "ci": 2, "docs": 1, "demo": 2}


def pontuar(repo):
    return sum(PESOS[sinal] for sinal, presente in repo.items() if presente)


repos = {
    "pipeline-rag":   {"readme": True,  "testes": True,  "ci": True,  "docs": True,  "demo": False},
    "demo-agente":    {"readme": True,  "testes": False, "ci": False, "docs": False, "demo": True},
    "scripts-soltos": {"readme": False, "testes": False, "ci": False, "docs": False, "demo": False},
}

maximo = sum(PESOS.values())
for nome, repo in sorted(repos.items(), key=lambda kv: pontuar(kv[1]), reverse=True):
    p = pontuar(repo)
    print(f"{nome:>15}: {p:2d}/{maximo} ({100 * p / maximo:.0f}%)")
