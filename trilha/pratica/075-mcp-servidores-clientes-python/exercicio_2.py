"""Exercício 2 — Cliente que casa por id.

Setup: o `ServidorMCP` (que fala por linhas JSON) e o `ClienteMCP` (com contador
    de id) dos exemplos da lição.

Tarefa:
    Registre a tool `maior`, cujo handler devolve {"valor": max(p["a"], p["b"])}.
    Faça duas chamadas a `maior` ({"a": 7, "b": 4} e {"a": 1, "b": 9}). Imprima
    `1a: {result}`, `2a: {result}` e `proximo id: {n}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/075-mcp-servidores-clientes-python/solucao_2.saida.txt
    (em particular, `proximo id: 3`).
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

# TODO: implemente o ClienteMCP (contador de id), registre `maior` e faça as chamadas.
