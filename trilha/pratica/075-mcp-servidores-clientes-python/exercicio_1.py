"""Exercício 1 — Servidor que despacha por método.

Setup: um `ServidorMCP` com registro method -> handler.

Tarefa:
    Implemente o `ServidorMCP` (métodos `registrar` e `tratar`). Registre `eco`,
    cujo handler devolve `{"texto": params["msg"]}`. Trate a request
    {"jsonrpc": "2.0", "id": 5, "method": "eco", "params": {"msg": "oi"}} e
    imprima `metodos: {lista ordenada}` e `resposta: {response}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/075-mcp-servidores-clientes-python/solucao_1.saida.txt
"""
class ServidorMCP:
    def __init__(self):
        self.handlers = {}

    # TODO: implemente `registrar` e `tratar`.

# TODO: registre `eco`, trate a request e imprima as duas linhas.
