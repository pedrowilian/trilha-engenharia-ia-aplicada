"""Exercicio 3 - Analise de lacunas (gap analysis) de carreira.

Setup (dado):
    alvo  = {"sistemas_rag": 5, "agentes": 4, "evals": 4, "custo_latencia": 3, "comunicacao": 5}
    atual = {"sistemas_rag": 2, "agentes": 3, "evals": 2, "custo_latencia": 3, "comunicacao": 3}
    PESO  = {"sistemas_rag": 3, "agentes": 2, "evals": 2, "custo_latencia": 1, "comunicacao": 2}

Tarefa:
    Para cada habilidade calcule gap = max(0, alvo - atual) e
    prioridade = gap * PESO. Ordene por (prioridade, gap, nome) decrescente e
    imprima, apenas para gap > 0,
        "<hab:>15>: gap=<gap> peso=<peso> prioridade=<prioridade>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/101-mercado-papel-portfolio/solucao_3.saida.txt
"""

alvo = {"sistemas_rag": 5, "agentes": 4, "evals": 4, "custo_latencia": 3, "comunicacao": 5}
atual = {"sistemas_rag": 2, "agentes": 3, "evals": 2, "custo_latencia": 3, "comunicacao": 3}
PESO = {"sistemas_rag": 3, "agentes": 2, "evals": 2, "custo_latencia": 1, "comunicacao": 2}

# TODO: calcule lacunas ponderadas e imprima as prioridades de estudo (gap > 0).
