"""Solução de referência — Exercício 3 da Lição 062.

Condição de parada dupla: objetivo atingido OU limite de iterações (guarda
contra laço infinito). A ação fixa soma 2, então objetivos ímpares nunca são
atingidos e o agente para no limite. Determinístico.
"""


def agente(objetivo, max_passos):
    estado, passos = 0, 0
    while estado != objetivo and passos < max_passos:
        estado += 2
        passos += 1
    atingiu = estado == objetivo
    return estado, passos, atingiu


for objetivo in [8, 7]:
    estado, passos, ok = agente(objetivo, max_passos=6)
    status = "sucesso" if ok else "parou no limite"
    print(f"objetivo={objetivo}: estado={estado} passos={passos} -> {status}")
