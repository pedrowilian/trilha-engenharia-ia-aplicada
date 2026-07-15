"""Solução de referência — Exercício 1 da Lição 005.

Implementa as normas L1, L2 e L-infinito do zero, normaliza um vetor pela
norma L2 e confirma que o vetor resultante tem norma 1.
"""
import math

w = [1.0, -2.0, 2.0]

l1 = sum(abs(x) for x in w)
l2 = math.sqrt(sum(x * x for x in w))
linf = max(abs(x) for x in w)
print(f"L1={l1:.4f} L2={l2:.4f} Linf={linf:.4f}")

u = [x / l2 for x in w]
print(f"normalizado: {[round(x, 4) for x in u]}")

norma_u = math.sqrt(sum(x * x for x in u))
print(f"norma do normalizado: {norma_u:.4f}")
print("OK" if abs(norma_u - 1.0) < 1e-9 else "FALHOU")
