"""Solução de referência — Exercício 3 da Lição 066 (round-trip).

Ida-e-volta de uma tool-call: dict -> JSON string -> dict, exigindo IGUALDADE
EXATA entre o dict final e o original (propriedade de corretude R3.6).
"""
import json

tool_call = {
    "name": "agendar",
    "arguments": {"dia": "segunda", "hora": 9, "lembrete": True},
}

ida = json.dumps(tool_call, ensure_ascii=False, sort_keys=True)
volta = json.loads(ida)

print("json:", ida)
print("igual?", volta == tool_call)
print("re-serializa identico?",
      json.dumps(volta, ensure_ascii=False, sort_keys=True) == ida)
