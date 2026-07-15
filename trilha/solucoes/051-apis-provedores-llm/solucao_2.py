"""Solução de referência — Exercício 2 da Lição 051.

Monta os cabeçalhos HTTP de autenticação por *bearer token*, mascarando a chave
de API (mostra apenas os últimos 4 caracteres). Boas práticas: a chave nunca
deve aparecer em logs ou saídas.
"""


def mascarar(chave, visivel=4):
    if len(chave) <= visivel:
        return "*" * len(chave)
    return "*" * (len(chave) - visivel) + chave[-visivel:]


def montar_headers(api_key):
    return {
        "Authorization": f"Bearer {mascarar(api_key)}",
        "Content-Type": "application/json",
    }


chave = "sk-ABCDEF1234567890"
headers = montar_headers(chave)
for k in sorted(headers):
    print(f"{k}: {headers[k]}")
