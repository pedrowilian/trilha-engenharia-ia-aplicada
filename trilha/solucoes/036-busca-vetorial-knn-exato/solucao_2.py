"""Solução de referência — Exercício 2 da Lição 036.

k-NN exato: retorna os k vizinhos mais próximos da consulta, ordenados por
distância crescente (desempate pelo identificador).
"""
import math


def l2(u, v):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(u, v)))


def knn(q, base, k):
    dists = sorted(((d, l2(q, base[d])) for d in base),
                   key=lambda kv: (kv[1], kv[0]))
    return dists[:k]


base = {
    "doc_a": [2.0, 3.0],
    "doc_b": [0.0, 1.0],
    "doc_c": [5.0, 4.0],
    "doc_d": [1.0, 0.0],
    "doc_e": [2.0, 1.0],
}
q = [1.0, 1.0]

print(f"top-3 vizinhos de {q}:")
for nome, dist in knn(q, base, 3):
    print(f"{nome}: {dist:.4f}")
