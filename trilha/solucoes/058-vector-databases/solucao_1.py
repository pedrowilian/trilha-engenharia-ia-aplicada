"""Solucao de referencia - Exercicio 1 da Licao 058.

Indice flat (busca exata por forca bruta): compara a consulta com TODOS os
vetores e devolve os k mais proximos por distancia euclidiana. E o baseline
exato contra o qual os indices aproximados sao comparados.
"""
import numpy as np


base = {
    "v1": [1.0, 1.0],
    "v2": [4.0, 2.0],
    "v3": [2.0, 5.0],
    "v4": [5.0, 5.0],
}
consulta = [4.0, 4.0]


def l2(a, b):
    a, b = np.array(a, float), np.array(b, float)
    return float(np.sqrt(((a - b) ** 2).sum()))


ranking = sorted(((vid, l2(consulta, base[vid])) for vid in sorted(base)),
                 key=lambda t: (t[1], t[0]))
for vid, d in ranking[:2]:
    print(f"{vid} dist={d:.4f}")
print("comparacoes:", len(base))
