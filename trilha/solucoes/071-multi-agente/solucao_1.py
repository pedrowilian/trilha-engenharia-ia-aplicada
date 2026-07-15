"""Solução de referência — Exercício 1 da Lição 071.

Supervisor: roteia cada tarefa para o agente trabalhador adequado. Determinístico.
"""

trabalhadores = {
    "codigo": lambda t: f"implementei {t}",
    "revisao": lambda t: f"revisei {t}",
}


def supervisor(tipo, tarefa):
    agente = trabalhadores[tipo]
    return agente(tarefa)


print(supervisor("codigo", "login"))
print(supervisor("revisao", "PR"))
