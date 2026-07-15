"""Solucao de referencia - Exercicio 3 da Licao 101.

Analise de lacunas (gap analysis): compara o perfil atual com o exigido pelo
nivel-alvo e ordena o que estudar por prioridade = lacuna x peso. E o plano de
carreira reduzido a uma conta: ataque primeiro a maior lacuna ponderada.
"""

alvo = {"sistemas_rag": 5, "agentes": 4, "evals": 4, "custo_latencia": 3, "comunicacao": 5}
atual = {"sistemas_rag": 2, "agentes": 3, "evals": 2, "custo_latencia": 3, "comunicacao": 3}
PESO = {"sistemas_rag": 3, "agentes": 2, "evals": 2, "custo_latencia": 1, "comunicacao": 2}

prioridades = []
for hab in alvo:
    gap = max(0, alvo[hab] - atual[hab])
    prioridades.append((gap * PESO[hab], gap, hab))

for score, gap, hab in sorted(prioridades, reverse=True):
    if gap > 0:
        print(f"{hab:>15}: gap={gap} peso={PESO[hab]} prioridade={score}")
