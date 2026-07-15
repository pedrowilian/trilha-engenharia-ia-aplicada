"""Exercício 3 — Integração fim-a-fim com detecção de ausência.

Setup:
    cenarios = [("com_mcp", True), ("sem_mcp", False)]

Tarefa:
    Implemente `fluxo(acionar_mcp)` que devolve um dict de contadores
    {"rag", "agente", "mcp"}: incrementa `agente` em 1 e `rag` em 1 sempre, e
    `mcp` em 2 apenas quando `acionar_mcp` for True. Implemente `completo(ev)`
    (todos > 0) e `ausentes(ev)` (componentes zerados na ordem rag, agente, mcp).
    Para cada cenário imprima
    `nome: rag={..} agente={..} mcp={..} completo={..} ausentes={..}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/100-capstone-implementacao-fluxo/solucao_3.saida.txt.
"""

cenarios = [("com_mcp", True), ("sem_mcp", False)]

# TODO: implemente fluxo, completo, ausentes e imprima cada cenario.
