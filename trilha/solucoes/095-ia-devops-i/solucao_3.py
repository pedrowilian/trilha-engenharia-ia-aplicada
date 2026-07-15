"""Solução de referência — Exercício 3 da Lição 095.

Troubleshooting estilo ReAct: o agente observa o estado, escolhe uma ação a
partir da base de conhecimento e age, até convergir para "ok". Determinístico.
"""

base = {
    "fila_cheia": ("escalar_workers", "cpu_alta"),
    "cpu_alta": ("otimizar_query", "ok"),
}


def diagnosticar(sintoma_inicial, max_passos=5):
    estado = sintoma_inicial
    trilha = []
    for _ in range(max_passos):
        if estado == "ok":
            break
        acao, proximo = base[estado]
        trilha.append(f"{estado} -> {acao}")
        estado = proximo
    return trilha, estado


trilha, final = diagnosticar("fila_cheia")
for passo in trilha:
    print(passo)
print("estado final:", final)
