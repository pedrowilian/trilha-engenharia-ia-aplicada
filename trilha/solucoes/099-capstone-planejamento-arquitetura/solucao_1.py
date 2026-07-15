"""Solução de referência — Exercício 1 da Lição 099.

Checklist binário de critérios de conclusão por componente. Imprime, para cada
componente, quantos critérios foram atendidos e se está concluído; ao final, se
o capstone inteiro está concluído. Determinístico.
"""

criterios = {
    "RAG": {"recuperacao_relevante": True, "determinismo": True},
    "Agente": {"uso_de_ferramenta": True, "selecao_por_politica": False},
    "MCP": {"descoberta_e_invocacao": True, "erro_em_inexistente": True},
}


def concluido(componente):
    return all(componente.values())


for nome in ("RAG", "Agente", "MCP"):
    itens = criterios[nome]
    atendidos = sum(1 for v in itens.values() if v)
    estado = "ok" if concluido(itens) else "pendente"
    print(f"{nome}: {atendidos}/{len(itens)} -> {estado}")
print(f"capstone concluido: {all(concluido(c) for c in criterios.values())}")
