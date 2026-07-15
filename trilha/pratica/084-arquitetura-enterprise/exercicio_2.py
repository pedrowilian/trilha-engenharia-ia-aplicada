"""Exercício 2 — Model tiering por SLA.

Setup:
    tiers = ["leve", "medio", "forte"]
    latencia = [60, 200, 700]   # ms (p95) por tier
    custo = [1, 4, 12]          # custo relativo por tier
    SLAs = [50, 120, 400, 800]

Tarefa:
    Implemente `escolher_tier(sla_ms)` que devolve o tier mais forte com
    latencia <= sla_ms (ou "nenhum"). Imprima
    `SLA={sla:>4}ms -> {t} (custo {c})`, com c = 0 quando nenhum tier cabe.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/084-arquitetura-enterprise/solucao_2.saida.txt
"""
import numpy as np

tiers = ["leve", "medio", "forte"]
latencia = np.array([60, 200, 700])
custo = np.array([1, 4, 12])

# TODO: implemente escolher_tier(...) e imprima a escolha para cada SLA.
