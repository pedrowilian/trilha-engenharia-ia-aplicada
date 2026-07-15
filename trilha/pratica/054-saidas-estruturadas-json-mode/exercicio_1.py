"""Exercício 1 — Parsear uma saída estruturada (JSON).

Setup: a string `saida_modelo` (a resposta "do modelo" em JSON), abaixo.

Tarefa:
    Faça o parsing com `json.loads` e imprima o tipo do objeto resultante
    (`type(dados).__name__`) e os campos `nome`, `idade` e `ativo`. Observe que
    `true` em JSON vira `True` em Python.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/054-saidas-estruturadas-json-mode/solucao_1.saida.txt
"""
import json

saida_modelo = '{"nome": "Ana", "idade": 30, "ativo": true}'

# TODO: parsear com json.loads e imprimir tipo + campos.
