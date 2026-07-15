"""Solução de referência — Exercício 1 da Lição 075.

Servidor MCP mínimo: registro method -> handler e despacho. Determinístico.
"""
class ServidorMCP:
    def __init__(self):
        self.handlers = {}

    def registrar(self, metodo, fn):
        self.handlers[metodo] = fn

    def tratar(self, request):
        fn = self.handlers[request["method"]]
        resultado = fn(request.get("params", {}))
        return {"jsonrpc": "2.0", "id": request["id"], "result": resultado}

srv = ServidorMCP()
srv.registrar("eco", lambda p: {"texto": p["msg"]})
resp = srv.tratar({"jsonrpc": "2.0", "id": 5, "method": "eco", "params": {"msg": "oi"}})
print("metodos:", sorted(srv.handlers))
print("resposta:", resp)
