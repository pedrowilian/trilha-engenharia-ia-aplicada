"""Exercício 1 — Esquema de ferramenta.

Setup: a ferramenta `multiplicar`, que multiplica dois números `x` e `y`.

Tarefa:
    Monte o dicionário `esquema` com as chaves `name`, `description` e
    `parameters` ({"x": "number", "y": "number"}). Imprima a serialização
    canônica `json.dumps(esquema, ensure_ascii=False, sort_keys=True)`, depois
    `nome: {name}` e `parametros: {lista ordenada dos parâmetros}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/066-function-calling-tool-use/solucao_1.saida.txt
"""
import json

# TODO: monte o esquema da ferramenta e serialize-o.
