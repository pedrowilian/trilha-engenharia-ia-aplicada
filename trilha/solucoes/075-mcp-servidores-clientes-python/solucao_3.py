"""Solução de referência — Exercício 3 da Lição 075.

Ciclo completo tools/list (descoberta) seguido de tools/call (execução).
Determinístico (lista de tools ordenada).
"""
def construir_servidor():
    ferramentas = {
        "subtrair": lambda a, b: a - b,
        "dividir": lambda a, b: a / b,
    }
    schemas = {
        "subtrair": {"a": "number", "b": "number"},
        "dividir": {"a": "number", "b": "number"},
    }

    def tratar(req):
        m = req["method"]
        if m == "tools/list":
            res = {"tools": sorted(schemas)}
        elif m == "tools/call":
            nome = req["params"]["name"]
            args = req["params"]["arguments"]
            res = {"valor": ferramentas[nome](**args)}
        return {"jsonrpc": "2.0", "id": req["id"], "result": res}

    return tratar

servidor = construir_servidor()
lista = servidor({"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}})
print("tools:", lista["result"]["tools"])
chamada = servidor({"jsonrpc": "2.0", "id": 2, "method": "tools/call",
                    "params": {"name": "subtrair", "arguments": {"a": 10, "b": 4}}})
print("subtrair(10,4) =", chamada["result"]["valor"])
