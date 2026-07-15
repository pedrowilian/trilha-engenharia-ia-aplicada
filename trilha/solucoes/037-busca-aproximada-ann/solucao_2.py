"""Solução de referência — Exercício 2 da Lição 037.

Índice ANN didático no estilo IVF (inverted file): agrupa a base por centróides
e, na consulta, examina apenas o(s) cluster(s) mais próximo(s). Compara a busca
aproximada (nprobe=1) com o k-NN exato e mede o recall.
"""
import math


def l2(u, v):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(u, v)))


base = {
    "a0": [0.0, 0.0], "a1": [0.5, 0.5], "a2": [1.0, 1.0],
    "b0": [4.0, 4.0], "b1": [3.5, 3.5], "b2": [3.0, 3.0],
}
centroides = {"A": [0.5, 0.5], "B": [3.5, 3.5]}

# Inverted file: lista de pontos por cluster (centróide mais próximo).
listas = {c: [] for c in centroides}
for nome, v in base.items():
    c = min(centroides, key=lambda c: (l2(v, centroides[c]), c))
    listas[c].append(nome)


def busca_exata(q, k):
    return [n for n, _ in sorted(((n, l2(q, base[n])) for n in base),
                                 key=lambda kv: (kv[1], kv[0]))[:k]]


def busca_ivf(q, k, nprobe):
    ordem = sorted(centroides, key=lambda c: (l2(q, centroides[c]), c))
    candidatos = []
    for c in ordem[:nprobe]:
        for n in listas[c]:
            candidatos.append((n, l2(q, base[n])))
    return [n for n, _ in sorted(candidatos, key=lambda kv: (kv[1], kv[0]))[:k]]


q = [2.0, 2.0]
exato = busca_exata(q, 3)
aprox = busca_ivf(q, 3, nprobe=1)
recall = len(set(aprox) & set(exato)) / len(exato)
print("exato top-3:", exato)
print("aprox top-3 (nprobe=1):", aprox)
print(f"recall@3 = {recall:.4f}")
