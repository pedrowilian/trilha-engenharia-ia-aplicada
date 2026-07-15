"""Solução de referência — Exercício 2 da Lição 072.

Mapa host -> clients (1 client por servidor). Confirma a relação 1:1.
Determinístico (ordem alfabética da chave).
"""
clients = {
    "slack": "server-slack",
    "drive": "server-drive",
    "jira": "server-jira",
}

print("num clients:", len(clients))
for servidor, client in sorted(clients.items()):
    print(f"  {servidor} -> {client}")
print("relacao 1:1?", len(clients) == len(set(clients.values())))
