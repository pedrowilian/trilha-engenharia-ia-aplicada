"""Solução de referência — Exercício 3 da Lição 074 (round-trip).

Ida-e-volta de uma request: dict -> string JSON -> dict, exigindo IGUALDADE
EXATA entre o dict final e o original (propriedade de corretude R3.6).
"""
import json

request = {
    "jsonrpc": "2.0",
    "id": 3,
    "method": "prompts/get",
    "params": {"name": "resumir", "arguments": {"n": 2}},
}

linha = json.dumps(request, ensure_ascii=False, sort_keys=True)
volta = json.loads(linha)

print("linha:", linha)
print("igual?", volta == request)
print("re-serializa identico?",
      json.dumps(volta, ensure_ascii=False, sort_keys=True) == linha)
