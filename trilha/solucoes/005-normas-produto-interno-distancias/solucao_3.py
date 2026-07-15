"""Solução de referência — Exercício 3 da Lição 005.

Mostra que a similaridade do cosseno é invariante à escala: multiplicar um
vetor por uma constante positiva não altera o cosseno em relação a uma
referência, embora o produto interno e a distância L2 mudem.
"""
import math


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def norm(u):
    return math.sqrt(dot(u, u))


def cos_sim(u, v):
    return dot(u, v) / (norm(u) * norm(v))


def l2(u, v):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(u, v)))


ref = [1.0, 2.0]
x = [2.0, 1.0]
x5 = [5.0 * c for c in x]

print(f"cos(ref, x)  = {cos_sim(ref, x):.4f}")
print(f"cos(ref, 5x) = {cos_sim(ref, x5):.4f}")
print(f"dot(ref, x)  = {dot(ref, x):.4f}")
print(f"dot(ref, 5x) = {dot(ref, x5):.4f}")
print(f"L2(ref, x)   = {l2(ref, x):.4f}")
print(f"L2(ref, 5x)  = {l2(ref, x5):.4f}")
invariante = abs(cos_sim(ref, x) - cos_sim(ref, x5)) < 1e-9
print("cosseno invariante a escala" if invariante else "FALHOU")
