"""Solução de referência — Exercício 2 da Lição 074.

Response de sucesso (result) e de erro (error), com a regra de exclusividade
(nunca os dois ao mesmo tempo). Determinístico.
"""
import json

ok = {"jsonrpc": "2.0", "id": 1, "result": {"valor": 42}}
erro = {"jsonrpc": "2.0", "id": 2,
        "error": {"code": -32602, "message": "Invalid params"}}

print(json.dumps(ok, ensure_ascii=False, sort_keys=True))
print(json.dumps(erro, ensure_ascii=False, sort_keys=True))
exclusivo = ("result" in ok and "error" not in ok
             and "error" in erro and "result" not in erro)
print("exclusivo?", exclusivo)
