"""Solução de referência — Exercício 2 da Lição 062.

Toolbox (ações nomeadas) + executor que despacha um plano (lista de ações) e
registra cada resultado na memória. Determinístico.
"""

toolbox = {
    "incrementar": lambda x: x + 1,
    "dobrar": lambda x: x * 2,
}


def executor(acao, estado):
    return toolbox[acao](estado)


plano = ["incrementar", "dobrar", "incrementar"]
estado = 2
memory = []

for acao in plano:
    estado = executor(acao, estado)
    memory.append((acao, estado))
    print(f"acao={acao} -> estado={estado}")

print("memoria:", memory)
print("estado final:", estado)
