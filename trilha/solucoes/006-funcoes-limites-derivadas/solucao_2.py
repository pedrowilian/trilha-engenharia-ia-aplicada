"""Solução de referência — Exercício 2 (Lição 006).

Derivada numérica de f(x) = x^3 em x = 1, comparada à derivada exata 3x^2.
"""


def f(x):
    return x ** 3


def derivada_exata(x):
    return 3.0 * x ** 2


x = 1.0
h = 1e-5
derivada_aprox = (f(x + h) - f(x)) / h

print(f"derivada aproximada = {derivada_aprox:.2f}")
print(f"derivada exata = {derivada_exata(x):.2f}")
