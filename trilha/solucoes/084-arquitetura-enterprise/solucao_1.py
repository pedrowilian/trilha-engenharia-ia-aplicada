"""Solução de referência — Exercício 1 da Lição 084.

Fluxo da requisição pela pilha enterprise (gateway -> orquestração -> serviços).
"""


def gateway(req):
    req = dict(req)
    req["autenticado"] = req.get("token") == "ok"
    return req


def orquestracao(req):
    req = dict(req)
    req["rota"] = "fluxo_rag" if req.get("precisa_contexto") else "fluxo_direto"
    return req


def servicos(req):
    req = dict(req)
    req["modelo"] = "forte" if req["rota"] == "fluxo_rag" else "leve"
    return req


camadas = [gateway, orquestracao, servicos]
req = {"token": "ruim", "precisa_contexto": False}
for camada in camadas:
    req = camada(req)

print("autenticado:", req["autenticado"])
print("rota:", req["rota"])
print("modelo:", req["modelo"])
