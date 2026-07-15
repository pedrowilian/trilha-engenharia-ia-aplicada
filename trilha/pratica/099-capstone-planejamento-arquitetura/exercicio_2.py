"""Exercício 2 — Ordem de montagem e fluxo da requisição.

Setup:
    dependencias = {
        "cliente_mcp": ["servidor_mcp"],
        "servidor_mcp": ["agente"],
        "agente": ["rag"],
        "rag": [],
    }
    (aresta A -> B significa "A depende de B".)

Tarefa:
    Implemente `ordem_de_montagem(deps)` que devolve a ordem em que os
    componentes podem ser montados (dependências primeiro), com desempate
    alfabético. Imprima a ordem numerada e, ao final,
    `fluxo da requisicao: <ordem inversa separada por ' -> '>`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/099-capstone-planejamento-arquitetura/solucao_2.saida.txt.
"""

dependencias = {
    "cliente_mcp": ["servidor_mcp"],
    "servidor_mcp": ["agente"],
    "agente": ["rag"],
    "rag": [],
}

# TODO: implemente ordem_de_montagem(deps) e imprima a ordem + o fluxo invertido.
