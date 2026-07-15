"""Solução de referência — Exercício 1 da Lição 066.

Esquema de ferramenta (nome, descrição, parâmetros tipados) serializado de forma
canônica com sort_keys. Determinístico.
"""
import json

esquema = {
    "name": "multiplicar",
    "description": "Multiplica dois numeros",
    "parameters": {"x": "number", "y": "number"},
}

print(json.dumps(esquema, ensure_ascii=False, sort_keys=True))
print("nome:", esquema["name"])
print("parametros:", sorted(esquema["parameters"]))
