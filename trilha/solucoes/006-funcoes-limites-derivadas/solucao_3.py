"""Solução de referência — Exercício 3 (Lição 006).

Otimização por varredura: encontra o ponto que minimiza f(x) = (x - 2)^2 + 1
e confirma que a derivada f'(x) = 2(x - 2) é zero nesse ponto.
"""


def f(x):
    return (x - 2.0) ** 2 + 1.0


def df(x):
    return 2.0 * (x - 2.0)


melhor_x = None
melhor_valor = None
x = -1.0
while x <= 5.0:
    if melhor_valor is None or f(x) < melhor_valor:
        melhor_valor = f(x)
        melhor_x = x
    x += 0.5

print(f"x otimo = {melhor_x}")
print(f"f(x otimo) = {melhor_valor}")
print(f"derivada no otimo = {df(melhor_x)}")
