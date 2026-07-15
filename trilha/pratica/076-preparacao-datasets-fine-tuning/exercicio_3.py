"""Exercício 3 — Round-trip (ida-e-volta) de JSONL.

Setup: a lista `registros` (abaixo) no formato de chat.

Tarefa:
    Implemente `serializar` (uma linha JSON por registro, com
    `ensure_ascii=False, sort_keys=True`) e `parsear` (ignora linhas em
    branco). Aplique o ciclo parse -> serialize -> parse duas vezes e imprima
    `linhas`, se o round-trip é exato e se o resultado iguala o original.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/076-preparacao-datasets-fine-tuning/solucao_3.saida.txt
"""
import json

registros = [
    {"messages": [
        {"role": "system", "content": "Voce e um tutor."},
        {"role": "user", "content": "O que e LoRA?"},
        {"role": "assistant", "content": "Adaptacao de baixo posto."},
    ]},
    {"messages": [
        {"role": "user", "content": "2+2?"},
        {"role": "assistant", "content": "4"},
    ]},
]

# TODO: implementar serializar/parsear e validar a ida-e-volta exata.
