"""Solução de referência — Exercício 1 da Lição 079.

Cliente SIMULADO (sem rede): faz upload de um JSONL validando que cada linha
tem a chave 'messages' não vazia, e captura o erro de uma linha inválida.
"""
import json


class ClienteSimulado:
    def __init__(self):
        self._seq = 0

    def upload(self, linhas):
        for i, linha in enumerate(linhas, 1):
            obj = json.loads(linha)
            if "messages" not in obj or not obj["messages"]:
                raise ValueError(f"linha {i} invalida: sem 'messages'")
        self._seq += 1
        return {"id": f"file-{self._seq:04d}", "n_exemplos": len(linhas), "status": "processed"}


cli = ClienteSimulado()
bons = [
    json.dumps({"messages": [{"role": "user", "content": "a"}, {"role": "assistant", "content": "b"}]}),
    json.dumps({"messages": [{"role": "user", "content": "c"}, {"role": "assistant", "content": "d"}]}),
    json.dumps({"messages": [{"role": "user", "content": "e"}, {"role": "assistant", "content": "f"}]}),
]
res = cli.upload(bons)
print("upload ok:", res["id"], res["n_exemplos"], res["status"])

ruins = bons + [json.dumps({"texto": "sem campo messages"})]
try:
    cli.upload(ruins)
except ValueError as erro:
    print("erro capturado:", erro)
