"""Solução de referência — Exercício 3 da Lição 098.

Requirements copilot + relatório: agrega o backlog por classe MoSCoW e calcula o
progresso (% de itens concluídos). Determinístico.
"""

backlog = [
    {"titulo": "API", "moscow": "Must", "feito": True},
    {"titulo": "Docs", "moscow": "Should", "feito": True},
    {"titulo": "i18n", "moscow": "Could", "feito": False},
    {"titulo": "SSO", "moscow": "Must", "feito": False},
    {"titulo": "Tema", "moscow": "Could", "feito": False},
]


def relatorio(backlog):
    por_classe = {}
    for item in backlog:
        por_classe[item["moscow"]] = por_classe.get(item["moscow"], 0) + 1
    feitos = sum(1 for i in backlog if i["feito"])
    pct = 100.0 * feitos / len(backlog)
    return por_classe, pct


classes, pct = relatorio(backlog)
for classe in ("Must", "Should", "Could"):
    print(f"{classe}: {classes.get(classe, 0)}")
print(f"progresso: {pct:.0f}%")
