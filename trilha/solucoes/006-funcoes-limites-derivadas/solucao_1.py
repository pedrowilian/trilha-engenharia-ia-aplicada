"""Solução de referência — Exercício 1 (Lição 006).

Taxa de variação média da função linear f(x) = 3x + 2 no intervalo [2, 5].
"""


def f(x):
    return 3.0 * x + 2.0


a, b = 2.0, 5.0
taxa_media = (f(b) - f(a)) / (b - a)

print(f"taxa media = {taxa_media}")
