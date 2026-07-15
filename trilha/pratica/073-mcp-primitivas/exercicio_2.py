"""Exercício 2 — Despachar tools por nome.

Setup: as tools `dobro` (parâmetro `x`) e `concatenar` (parâmetros `a`, `b`).

Tarefa:
    Monte um registro `tools` (nome -> função). Implemente
    `chamar_tool(nome, argumentos)` que despacha pelo nome chamando a função com
    `**argumentos`. Imprima `tools: {lista ordenada}`, `dobro(21) = {...}` e
    `concatenar = {...}` para os argumentos {"a": "mc", "b": "p"}.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/073-mcp-primitivas/solucao_2.saida.txt
"""
def dobro(x):
    return x * 2

def concatenar(a, b):
    return a + b

# TODO: monte o registro `tools`, implemente `chamar_tool` e imprima as linhas.
