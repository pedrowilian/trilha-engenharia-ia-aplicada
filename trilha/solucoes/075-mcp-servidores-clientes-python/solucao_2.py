"""Solução de referência — Exercício 2 da Lição 075.

Cliente MCP que numera requests e casa respostas pelo id, conversando com o
servidor por linhas JSON. Determinístico.
"""
import json

class ServidorMCP:
    def __init__(self):
        self.handlers = {}

    def registrar(self, metodo, fn):
        self.handlers[metodo] = fn

    def tratar_linha(self, linha):
        req = json.loads(linha)
        res = self.handlers[req["method"]](req.get("params", {}))
        return json.dumps({"jsonrpc": "2.0", "id": req["id"], "result": res},
                          ensure_ascii=False, sort_keys=True)

class ClienteMCP:
    def __init__(self, servidor):
        self.servidor = servidor
        self.proximo_id = 1

    def chamar(self, metodo, params):
        req = {"jsonrpc": "2.0", "id": self.proximo_id,
               "method": metodo, "params": params}
        self.proximo_id += 1
        linha = json.dumps(req, ensure_ascii=False, sort_keys=True)
        resposta = json.loads(self.servidor.tratar_linha(linha))
        assert resposta["id"] == req["id"]
        return resposta["result"]

srv = ServidorMCP()
srv.registrar("maior", lambda p: {"valor": max(p["a"], p["b"])})
cli = ClienteMCP(srv)
print("1a:", cli.chamar("maior", {"a": 7, "b": 4}))
print("2a:", cli.chamar("maior", {"a": 1, "b": 9}))
print("proximo id:", cli.proximo_id)
