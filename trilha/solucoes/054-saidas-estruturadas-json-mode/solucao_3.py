"""Solução de referência — Exercício 3 da Lição 054 (round-trip).

Ida-e-volta (round-trip) de uma saída estruturada: dict -> JSON string -> dict,
exigindo IGUALDADE EXATA entre o dict final e o original. Esta é a propriedade
de corretude de serialização (R3.6).
"""
import json

registro = {
    "nome": "Ana",
    "tags": ["a", "b"],
    "meta": {"idade": 30, "ativo": True},
}

texto = json.dumps(registro, ensure_ascii=False, sort_keys=True)
volta = json.loads(texto)

print("json:", texto)
print("igual?", volta == registro)
print("identico ao re-serializar?",
      json.dumps(volta, ensure_ascii=False, sort_keys=True) == texto)
