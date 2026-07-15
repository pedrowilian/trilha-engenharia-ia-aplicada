"""Exercício 2 — Validar contra um schema.

Setup: o `schema` (chave -> tipo Python esperado) e a lista `casos` (strings
JSON), abaixo.

Tarefa:
    Implemente `validar(obj, schema)` que percorre o schema e acumula erros:
    `faltando: <chave>` quando a chave não existe e `tipo invalido: <chave>`
    quando o tipo não bate (use isinstance). Para cada caso, parseie com
    `json.loads` e imprima `ok` (sem erros) ou `erros: ` + os erros juntos por
    ", " (na ordem do schema).

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/054-saidas-estruturadas-json-mode/solucao_2.saida.txt
"""
import json

schema = {"nome": str, "idade": int, "ativo": bool}
casos = [
    '{"nome": "Ana", "idade": 30, "ativo": true}',
    '{"nome": "Beto", "idade": "trinta"}',
]

# TODO: implementar validar() e imprimir o resultado de cada caso.
