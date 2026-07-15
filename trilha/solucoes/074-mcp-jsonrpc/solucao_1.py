"""Solução de referência — Exercício 1 da Lição 074.

Monta uma request JSON-RPC 2.0 (tools/call) e a serializa de forma canônica
(sort_keys=True). Determinístico.
"""
import json

request = {
    "jsonrpc": "2.0",
    "id": 10,
    "method": "tools/call",
    "params": {"name": "multiplicar", "arguments": {"a": 6, "b": 7}},
}

print(json.dumps(request, ensure_ascii=False, sort_keys=True))
