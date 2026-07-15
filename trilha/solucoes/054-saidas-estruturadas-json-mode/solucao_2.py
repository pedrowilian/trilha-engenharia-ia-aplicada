"""Solução de referência — Exercício 2 da Lição 054.

Valida objetos parseados contra um schema simples (chave -> tipo esperado),
acumulando os erros de chave ausente e de tipo inválido.
"""
import json

schema = {"nome": str, "idade": int, "ativo": bool}


def validar(obj, schema):
    erros = []
    for chave, tipo in schema.items():
        if chave not in obj:
            erros.append(f"faltando: {chave}")
        elif not isinstance(obj[chave], tipo):
            erros.append(f"tipo invalido: {chave}")
    return erros


casos = [
    '{"nome": "Ana", "idade": 30, "ativo": true}',
    '{"nome": "Beto", "idade": "trinta"}',
]
for c in casos:
    obj = json.loads(c)
    erros = validar(obj, schema)
    print("ok" if not erros else "erros: " + ", ".join(erros))
