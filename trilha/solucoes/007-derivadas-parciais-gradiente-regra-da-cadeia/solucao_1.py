"""Solução de referência — Exercício 1 (Lição 007).

Derivadas parciais de f(x, y) = x^2 * y + y^3 no ponto (2, 1).
df/dx = 2xy ; df/dy = x^2 + 3y^2
"""


def parcial_x(x, y):
    return 2.0 * x * y


def parcial_y(x, y):
    return x ** 2 + 3.0 * y ** 2


x, y = 2.0, 1.0

print(f"df/dx = {parcial_x(x, y)}")
print(f"df/dy = {parcial_y(x, y)}")
