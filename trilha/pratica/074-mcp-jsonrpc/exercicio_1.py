"""Exercício 1 — Montar uma request JSON-RPC.

Setup: uma chamada ao método `tools/call` da tool `multiplicar` com argumentos
    {"a": 6, "b": 7} e id = 10.

Tarefa:
    Monte o dicionário `request` com as chaves `jsonrpc` ("2.0"), `id`, `method`
    e `params` ({"name": ..., "arguments": ...}). Imprima
    `json.dumps(request, ensure_ascii=False, sort_keys=True)`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/074-mcp-jsonrpc/solucao_1.saida.txt
"""
import json

# TODO: monte a request e imprima sua serialização canônica.
