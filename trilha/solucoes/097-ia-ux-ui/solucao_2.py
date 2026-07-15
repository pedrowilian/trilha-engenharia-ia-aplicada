"""Solução de referência — Exercício 2 da Lição 097.

Prototipação assistida: gera variantes de layout (1, 2 ou 3 colunas) e as pontua
por uma heurística determinística que premia 2 colunas e penaliza muitas linhas.
"""


def variantes(n_componentes):
    saida = []
    for colunas in (1, 2, 3):
        linhas = -(-n_componentes // colunas)  # teto da divisao
        score = 10 - abs(colunas - 2) * 2 - max(0, linhas - 3)
        saida.append((colunas, linhas, score))
    return saida


for colunas, linhas, score in variantes(4):
    print(f"colunas={colunas} linhas={linhas} score={score}")
