"""Solução de referência — Exercício 3 da Lição 035.

Demonstra a identidade prática: em vetores NORMALIZADOS (norma 1), o produto
interno é igual à similaridade do cosseno. Por isso bancos vetoriais normalizam
os embeddings e usam o dot product (mais barato) para ranquear.
"""
import math


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def norm(u):
    return math.sqrt(dot(u, u))


def cos_sim(u, v):
    return dot(u, v) / (norm(u) * norm(v))


def normalizar(u):
    n = norm(u)
    return [x / n for x in u]


pares = [([3.0, 4.0], [4.0, 3.0]), ([1.0, 0.0], [0.0, 5.0]), ([2.0, 1.0], [4.0, 2.0])]
for u, v in pares:
    un, vn = normalizar(u), normalizar(v)
    d = dot(un, vn)
    c = cos_sim(u, v)
    print(f"dot_norm={d:.4f} cos={c:.4f} iguais={round(d, 6) == round(c, 6)}")
