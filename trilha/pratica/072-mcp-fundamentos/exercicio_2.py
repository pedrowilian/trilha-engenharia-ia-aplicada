"""Exercício 2 — Mapa host → clients.

Setup: o dicionário de conexões abaixo (1 client por servidor).

Tarefa:
    Imprima `num clients: {n}`, depois cada par `  {servidor} -> {client}` em
    ordem alfabética da chave, e por fim `relacao 1:1? {True/False}` comparando o
    número de clients ao de servidores distintos (`set(clients.values())`).

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/072-mcp-fundamentos/solucao_2.saida.txt
"""
clients = {
    "slack": "server-slack",
    "drive": "server-drive",
    "jira": "server-jira",
}

# TODO: imprima o número de clients, os pares ordenados e a checagem 1:1.
