"""Exercício 1 — Checklist de critérios de conclusão por componente.

Setup:
    criterios = {
        "RAG": {"recuperacao_relevante": True, "determinismo": True},
        "Agente": {"uso_de_ferramenta": True, "selecao_por_politica": False},
        "MCP": {"descoberta_e_invocacao": True, "erro_em_inexistente": True},
    }

Tarefa:
    Defina `concluido(componente)` (True sse todos os critérios são True).
    Para cada componente (na ordem RAG, Agente, MCP) imprima
    `nome: {atendidos}/{total} -> ok|pendente`. Ao final imprima
    `capstone concluido: {True|False}` (concluído sse todos os componentes estão ok).

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/099-capstone-planejamento-arquitetura/solucao_1.saida.txt.
"""

criterios = {
    "RAG": {"recuperacao_relevante": True, "determinismo": True},
    "Agente": {"uso_de_ferramenta": True, "selecao_por_politica": False},
    "MCP": {"descoberta_e_invocacao": True, "erro_em_inexistente": True},
}

# TODO: implemente concluido(componente) e imprima o status por componente + total.
