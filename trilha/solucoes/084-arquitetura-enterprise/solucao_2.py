"""Solução de referência — Exercício 2 da Lição 084.

Model tiering: escolhe o tier mais forte cuja latência cabe no SLA.
"""
import numpy as np

tiers = ["leve", "medio", "forte"]
latencia = np.array([60, 200, 700])
custo = np.array([1, 4, 12])


def escolher_tier(sla_ms):
    viaveis = np.where(latencia <= sla_ms)[0]
    if len(viaveis) == 0:
        return "nenhum"
    return tiers[int(viaveis.max())]


for sla in [50, 120, 400, 800]:
    t = escolher_tier(sla)
    c = int(custo[tiers.index(t)]) if t != "nenhum" else 0
    print(f"SLA={sla:>4}ms -> {t} (custo {c})")
