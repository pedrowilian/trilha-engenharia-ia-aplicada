"""Solucao de referencia - Exercicio 2 da Licao 058.

Indice particionado tipo IVF (inverted file): cada vetor e atribuido ao centroide
mais proximo; a busca encontra o centroide mais proximo da consulta e varre APENAS
os pontos daquela particao (nprobe=1). Reduz as comparacoes em troca de busca
aproximada. Aqui o resultado coincide com o flat e custa menos comparacoes.
"""
import numpy as np


base = {
    "v1": [1.0, 1.0], "v2": [2.0, 1.0], "v3": [1.0, 2.0],
    "v4": [5.0, 1.0], "v5": [6.0, 1.0], "v6": [5.0, 2.0],
    "v7": [3.0, 6.0], "v8": [4.0, 6.0], "v9": [3.0, 7.0],
}
centroides = {"c0": [1.0, 1.0], "c1": [5.0, 1.0], "c2": [3.0, 6.0]}
consulta = [4.0, 6.0]


def l2(a, b):
    a, b = np.array(a, float), np.array(b, float)
    return float(np.sqrt(((a - b) ** 2).sum()))


# Atribui cada ponto ao centroide mais proximo (construcao do indice).
clusters = {c: [] for c in centroides}
for vid in sorted(base):
    c = min(sorted(centroides), key=lambda c: (l2(base[vid], centroides[c]), c))
    clusters[c].append(vid)

# Busca IVF: probe so o cluster do centroide mais proximo da consulta.
cprox = min(sorted(centroides), key=lambda c: (l2(consulta, centroides[c]), c))
candidatos = clusters[cprox]
ivf = min(candidatos, key=lambda v: (l2(consulta, base[v]), v))
comp_ivf = len(centroides) + len(candidatos)

# Busca flat: varre tudo (referencia exata).
flat = min(sorted(base), key=lambda v: (l2(consulta, base[v]), v))

print("centroide mais proximo:", cprox)
print(f"ivf top-1: {ivf} dist={l2(consulta, base[ivf]):.4f}")
print(f"flat top-1: {flat} dist={l2(consulta, base[flat]):.4f}")
print(f"comparacoes ivf: {comp_ivf} | flat: {len(base)}")
print("resultados coincidem:", ivf == flat)
