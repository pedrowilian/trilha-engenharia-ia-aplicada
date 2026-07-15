"""Solucao de referencia - Exercicio 2 da Licao 089.

Metricas operacionais agregadas sobre uma janela de requisicoes: taxa de erro e
p95 de latencia, confrontadas com os SLOs. A verificacao de SLO e o gatilho de
alertas/rollback em producao.
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

total = len(requisicoes)
erros = sum(1 for r in requisicoes if not r["ok"])
taxa_erro = erros / total

lat = sorted(r["latencia_ms"] for r in requisicoes)
rank = math.ceil(0.95 * total)
p95 = lat[max(1, min(rank, total)) - 1]

slo_erro = 0.10
slo_p95 = 500
viola_erro = taxa_erro > slo_erro
viola_p95 = p95 > slo_p95

print(f"requisicoes: {total}")
print(f"taxa de erro: {taxa_erro:.4f} (SLO <= {slo_erro:.2f})")
print(f"p95 latencia: {p95} ms (SLO <= {slo_p95} ms)")
print(f"viola SLO erro: {viola_erro}")
print(f"viola SLO p95: {viola_p95}")
