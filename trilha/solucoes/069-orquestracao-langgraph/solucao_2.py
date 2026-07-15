"""Solução de referência — Exercício 2 da Lição 069.

Grafo linear: nós nomeados + mapa de arestas; o motor executa do START ao END.
Determinístico.
"""


def no_a(estado):
    estado = dict(estado)
    estado["valor"] += 5
    estado["rota"].append("A")
    return estado


def no_b(estado):
    estado = dict(estado)
    estado["valor"] -= 2
    estado["rota"].append("B")
    return estado


nos = {"A": no_a, "B": no_b}
arestas = {"START": "A", "A": "B", "B": "END"}

estado = {"valor": 10, "rota": []}
atual = arestas["START"]
while atual != "END":
    estado = nos[atual](estado)
    atual = arestas[atual]

print("valor:", estado["valor"])
print("rota:", estado["rota"])
