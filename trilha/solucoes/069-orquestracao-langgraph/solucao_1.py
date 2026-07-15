"""Solução de referência — Exercício 1 da Lição 069.

Estado compartilhado: um nó é uma função (pura) que recebe o estado e devolve um
novo estado. Determinístico.
"""


def no_dobrar(estado):
    novo = dict(estado)
    novo["valor"] = estado["valor"] * 2
    novo["log"] = estado["log"] + ["dobrou"]
    return novo


estado = {"valor": 3, "log": []}
estado = no_dobrar(estado)
estado = no_dobrar(estado)

print("valor:", estado["valor"])
print("log:", estado["log"])
