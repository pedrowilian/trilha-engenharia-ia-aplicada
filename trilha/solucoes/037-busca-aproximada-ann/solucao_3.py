"""Solução de referência — Exercício 3 da Lição 037.

Varre o parâmetro nprobe do índice IVF e mostra o trade-off fundamental da busca
aproximada: aumentar o esforço (mais clusters examinados) eleva o recall E o
custo (número de comparações, proxy de latência).
"""
import math


def l2(u, v):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(u, v)))


base = {
    "a0": [0.0, 0.0], "a1": [0.5, 0.5], "a2": [1.0, 1.0],
    "b0": [4.0, 4.0], "b1": [3.5, 3.5], "b2": [3.0, 3.0],
    "c0": [0.0, 8.0], "c1": [0.5, 8.0], "c2": [1.0, 8.0],
}
centroides = {"A": [0.5, 0.5], "B": [3.5, 3.5], "C": [0.5, 8.0]}

listas = {c: [] for c in centroides}
for nome, v in base.items():
    c = min(centroides, key=lambda c: (l2(v, centroides[c]), c))
    listas[c].append(nome)


def busca_exata(q, k):
    return [n for n, _ in sorted(((n, l2(q, base[n])) for n in base),
                                 key=lambda kv: (kv[1], kv[0]))[:k]]


def busca_ivf(q, k, nprobe):
    ordem = sorted(centroides, key=lambda c: (l2(q, centroides[c]), c))
    candidatos, comparacoes = [], 0
    for c in ordem[:nprobe]:
        for n in listas[c]:
            comparacoes += 1
            candidatos.append((n, l2(q, base[n])))
    topk = [n for n, _ in sorted(candidatos, key=lambda kv: (kv[1], kv[0]))[:k]]
    return topk, comparacoes


q = [2.0, 2.0]
exato = busca_exata(q, 3)
print("exato top-3:", exato)
for nprobe in (1, 2, 3):
    aprox, comps = busca_ivf(q, 3, nprobe)
    recall = len(set(aprox) & set(exato)) / len(exato)
    print(f"nprobe={nprobe}: comparacoes={comps} recall@3={recall:.4f}")
