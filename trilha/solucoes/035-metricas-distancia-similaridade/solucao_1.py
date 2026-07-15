"""Solução de referência — Exercício 1 da Lição 035.

Implementa, do zero, as três medidas usadas em busca vetorial — produto interno
(dot), distância euclidiana (L2) e similaridade do cosseno — e as aplica a um par
de vetores.
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


u = [1.0, 2.0, 2.0]
v = [2.0, 3.0, 6.0]
print(f"dot = {dot(u, v):.4f}")
print(f"L2  = {l2(u, v):.4f}")
print(f"cos = {cos_sim(u, v):.4f}")
