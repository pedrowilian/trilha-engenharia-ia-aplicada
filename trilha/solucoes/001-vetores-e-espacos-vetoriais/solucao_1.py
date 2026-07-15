"""Exercício 1 — Operações com vetores implementadas do zero (sem numpy).

Setup: dois vetores u e v em R^3.
Objetivo: implementar soma de vetores e multiplicação por escalar e usá-las
para calcular u + v, 2*u e a combinação linear u + 2*v.
"""


def soma(u, v):
    """Soma componente a componente; exige vetores de mesma dimensão."""
    return [a + b for a, b in zip(u, v)]


def escala(c, u):
    """Multiplica cada componente do vetor pelo escalar c."""
    return [c * a for a in u]


u = [1.0, 2.0, 3.0]
v = [4.0, 5.0, 6.0]

print("u + v   =", soma(u, v))
print("2 * u   =", escala(2.0, u))
print("u + 2*v =", soma(u, escala(2.0, v)))
