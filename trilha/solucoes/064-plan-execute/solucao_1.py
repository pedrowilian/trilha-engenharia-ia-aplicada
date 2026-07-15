"""Solução de referência — Exercício 1 da Lição 064.

Planner estático: gera um plano ordenado (lista de passos) a partir do objetivo.
Determinístico.
"""


def planejar(objetivo):
    planos = {
        "relatorio": ["coletar_dados", "analisar", "escrever", "revisar"],
        "deploy": ["testar", "build", "publicar"],
    }
    return planos.get(objetivo, [])


plano = planejar("deploy")
for i, passo in enumerate(plano, 1):
    print(f"{i}. {passo}")
print("total de passos:", len(plano))
