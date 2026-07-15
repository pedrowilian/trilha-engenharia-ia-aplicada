"""Exercício 2 — Sucesso e erro.

Setup:
    - response de sucesso: id = 1, result = {"valor": 42}
    - response de erro:    id = 2, code = -32602, message = "Invalid params"

Tarefa:
    Monte os dois dicionários (`ok` e `erro`). Imprima cada um com
    `json.dumps(..., ensure_ascii=False, sort_keys=True)`. Por fim, imprima
    `exclusivo? {True/False}` checando que `ok` tem `result` (e não `error`) e
    `erro` tem `error` (e não `result`).

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/074-mcp-jsonrpc/solucao_2.saida.txt
"""
import json

# TODO: monte `ok` e `erro`, serialize ambos e imprima a checagem de exclusividade.
