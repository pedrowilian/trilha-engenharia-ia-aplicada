"""Exercicio 1 - Tracing de prompts e agregacao do trace.

Setup (dado):
    trace = [
        {"span": "embed",    "latencia_ms": 50,  "custo": 0.0001},
        {"span": "search",   "latencia_ms": 30,  "custo": 0.0000},
        {"span": "generate", "latencia_ms": 420, "custo": 0.0021},
        {"span": "guard",    "latencia_ms": 25,  "custo": 0.0003},
    ]

Tarefa:
    Some latencia e custo de todos os spans. Imprima uma linha por span no formato
    "<span alinhado a direita em 9>: <latencia em 4> ms  $<custo 4 casas>", depois
    a linha "TOTAL" no mesmo formato, e por fim "gargalo: <span> (<latencia> ms)"
    (o span de maior latencia).

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/089-mlops-llmops-observabilidade/solucao_1.saida.txt
"""

trace = [
    {"span": "embed", "latencia_ms": 50, "custo": 0.0001},
    {"span": "search", "latencia_ms": 30, "custo": 0.0000},
    {"span": "generate", "latencia_ms": 420, "custo": 0.0021},
    {"span": "guard", "latencia_ms": 25, "custo": 0.0003},
]

# TODO: agregue latencia/custo, imprima cada span, o TOTAL e o gargalo.
