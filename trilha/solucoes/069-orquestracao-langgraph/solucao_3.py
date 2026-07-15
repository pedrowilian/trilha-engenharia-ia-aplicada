"""Solução de referência — Exercício 3 da Lição 069.

Arestas condicionais: uma função de roteamento decide o próximo nó. O agente
chama a ferramenta até coletar 3 itens; a ferramenta sempre volta ao agente.
Determinístico.
"""


def agente(estado):
    estado = dict(estado)
    estado["passos"] += 1
    estado["rota"] = estado["rota"] + ["agente"]
    return estado


def ferramenta(estado):
    estado = dict(estado)
    estado["coletado"] += 1
    estado["rota"] = estado["rota"] + ["ferramenta"]
    return estado


def rotear(estado):
    return "ferramenta" if estado["coletado"] < 3 else "END"


nos = {"agente": agente, "ferramenta": ferramenta}
estado = {"passos": 0, "coletado": 0, "rota": []}
atual = "agente"
while atual != "END":
    estado = nos[atual](estado)
    atual = rotear(estado) if atual == "agente" else "agente"

print("rota:", estado["rota"])
print("passos do agente:", estado["passos"])
