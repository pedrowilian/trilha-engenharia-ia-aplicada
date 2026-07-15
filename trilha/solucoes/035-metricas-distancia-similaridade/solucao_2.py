"""Solução de referência — Exercício 2 da Lição 035.

Mostra que o ranking por similaridade do cosseno pode DISCORDAR do ranking por
distância euclidiana, porque a L2 sofre influência da magnitude e o cosseno só
da direção.
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
    "A": [8.0, 8.0],   # mesma direção de q, magnitude grande
    "B": [1.0, 0.0],   # perto em L2, direção diferente
    "C": [0.0, 3.0],
}
rank_cos = sorted(docs, key=lambda d: (-cos_sim(q, docs[d]), d))
rank_l2 = sorted(docs, key=lambda d: (l2(q, docs[d]), d))
print("ranking cosseno:", rank_cos)
print("ranking L2:     ", rank_l2)
print(f"top cosseno={rank_cos[0]} top L2={rank_l2[0]}")
print("os rankings discordam:", rank_cos != rank_l2)
