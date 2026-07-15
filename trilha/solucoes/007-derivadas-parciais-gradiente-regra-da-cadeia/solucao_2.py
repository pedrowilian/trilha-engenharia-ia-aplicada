"""Solução de referência — Exercício 2 (Lição 007).

Gradiente de f(x, y) = x^2 + y^2 no ponto (3, 4) e sua norma.
grad f = [2x, 2y]
"""
import math


def grad(x, y):
    return [2.0 * x, 2.0 * y]


x, y = 3.0, 4.0
g = grad(x, y)
norma = math.sqrt(g[0] ** 2 + g[1] ** 2)

print(f"gradiente = {g}")
print(f"norma = {norma}")
