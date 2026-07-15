"""Solução de referência — Exercício 1 da Lição 036.

Busca vetorial exata por varredura linear (brute force): compara a consulta com
TODOS os vetores da base e retorna o mais próximo pela distância euclidiana.
"""
import math


def l2(u, v):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(u, v)))


base = {
    "doc_a": [2.0, 3.0],
    "doc_b": [0.0, 1.0],
    "doc_c": [5.0, 4.0],
    "doc_d": [1.0, 0.0],
}
q = [1.0, 1.0]

mais_proximo = min(base, key=lambda d: (l2(q, base[d]), d))
print("consulta:", q)
for d in base:
    print(f"{d}: dist={l2(q, base[d]):.4f}")
print("mais proximo:", mais_proximo)
