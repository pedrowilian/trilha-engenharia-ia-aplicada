"""Solução de referência — Exercício 2 da Lição 005.

Ranqueia documentos em relação a uma consulta por similaridade do cosseno e
por distância L2, mostrando que os dois critérios podem produzir rankings
diferentes (a magnitude importa para L2, mas não para o cosseno).
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


q = [1.0, 1.0]
docs = {
    "A": [10.0, 10.0],
    "B": [1.0, 0.0],
    "C": [0.0, 2.0],
}

por_cos = sorted(docs, key=lambda k: cos_sim(q, docs[k]), reverse=True)
por_l2 = sorted(docs, key=lambda k: l2(q, docs[k]))

print("cosseno:")
for k in por_cos:
    print(f"  {k}: cos={cos_sim(q, docs[k]):.4f}")
print("L2:")
for k in por_l2:
    print(f"  {k}: L2={l2(q, docs[k]):.4f}")
print(f"top cosseno={por_cos[0]} top L2={por_l2[0]}")
