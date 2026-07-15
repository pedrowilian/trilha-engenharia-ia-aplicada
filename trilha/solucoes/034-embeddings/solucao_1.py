"""Solução de referência — Exercício 1 da Lição 034.

Dada uma tabela de embeddings (lookup), encontra o vizinho mais próximo de uma
palavra-consulta por similaridade do cosseno e imprime o ranking completo.
"""
import math

emb = {
    "gato":     [0.9, 0.1, 0.0],
    "cachorro": [0.8, 0.2, 0.1],
    "felino":   [0.85, 0.15, 0.0],
    "carro":    [0.0, 0.1, 0.9],
}


def cos_sim(u, v):
    dot = sum(a * b for a, b in zip(u, v))
    nu = math.sqrt(sum(a * a for a in u))
    nv = math.sqrt(sum(b * b for b in v))
    return dot / (nu * nv)


consulta = "gato"
ranking = sorted(
    ((p, cos_sim(emb[consulta], emb[p])) for p in emb if p != consulta),
    key=lambda kv: (-kv[1], kv[0]),
)
for palavra, sim in ranking:
    print(f"{palavra:>9}: {sim:.4f}")
print("mais proximo de", consulta, "->", ranking[0][0])
