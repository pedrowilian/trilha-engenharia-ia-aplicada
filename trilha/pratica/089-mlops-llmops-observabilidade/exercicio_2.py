"""Exercicio 2 - Metricas operacionais e verificacao de SLO.

Setup (dado): a lista `requisicoes` (10 itens com "ok" e "latencia_ms") e os SLOs
    slo_erro = 0.10  (taxa de erro maxima)
    slo_p95 = 500    (p95 de latencia maximo, em ms)

Tarefa:
    Calcule a taxa de erro (fracao de "ok"==False) e o p95 de latencia (nearest-rank,
    rank = ceil(0.95*n)). Compare com os SLOs (violacao = metrica estritamente maior
    que o SLO). Imprima, nesta ordem:
    "requisicoes: <n>", "taxa de erro: <4 casas> (SLO <= <2 casas>)",
    "p95 latencia: <n> ms (SLO <= <n> ms)", "viola SLO erro: <bool>",
    "viola SLO p95: <bool>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/089-mlops-llmops-observabilidade/solucao_2.saida.txt
"""
import math

requisicoes = [
    {"ok": True, "latencia_ms": 120},
    {"ok": True, "latencia_ms": 140},
    {"ok": True, "latencia_ms": 130},
    {"ok": True, "latencia_ms": 160},
    {"ok": True, "latencia_ms": 150},
    {"ok": True, "latencia_ms": 135},
    {"ok": False, "latencia_ms": 200},
    {"ok": True, "latencia_ms": 145},
    {"ok": True, "latencia_ms": 155},
    {"ok": True, "latencia_ms": 480},
]
slo_erro = 0.10
slo_p95 = 500

# TODO: calcule taxa de erro e p95, compare com os SLOs e imprima no formato pedido.
