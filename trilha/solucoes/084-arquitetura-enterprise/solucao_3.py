"""Solução de referência — Exercício 3 da Lição 084.

Painel de observabilidade: p50, p95 e taxa de erro de uma janela de requisições.
"""
import numpy as np

latencias = np.array([70, 65, 80, 500, 72, 68, 90, 75, 60, 400])
erros = np.array([0, 0, 0, 1, 0, 0, 0, 0, 0, 1])

p50 = float(np.percentile(latencias, 50))
p95 = float(np.percentile(latencias, 95))
taxa_erro = float(erros.mean())

print(f"p50 = {p50:.1f} ms")
print(f"p95 = {p95:.1f} ms")
print(f"taxa de erro = {taxa_erro:.1%}")
