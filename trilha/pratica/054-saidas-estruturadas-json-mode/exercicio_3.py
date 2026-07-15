"""Exercício 3 — Round-trip dict -> JSON -> dict (igualdade exata).

Setup: o dicionário `registro` (aninhado), abaixo.

Tarefa (ida-e-volta / round-trip):
    Serialize com `json.dumps(registro, ensure_ascii=False, sort_keys=True)`,
    parseie de volta com `json.loads` e verifique a IGUALDADE EXATA entre o
    dict final e o original. Imprima a string JSON (`json:`), `igual?` com o
    resultado de `volta == registro` e `identico ao re-serializar?` comparando
    `json.dumps(volta, ...)` com a string original.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/054-saidas-estruturadas-json-mode/solucao_3.saida.txt
    (em particular, `igual? True`).
"""
import json

registro = {
    "nome": "Ana",
    "tags": ["a", "b"],
    "meta": {"idade": 30, "ativo": True},
}

# TODO: serializar (sort_keys=True), parsear de volta e checar igualdade exata.
