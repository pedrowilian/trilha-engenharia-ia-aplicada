"""Solucao de referencia - Exercicio 3 da Licao 058.

Filtragem por metadados + busca vetorial (o modelo do pgvector): cada registro
guarda vetor e metadados; a busca primeiro filtra pelos metadados e so entao
ordena os candidatos por similaridade do cosseno.
"""
import numpy as np


registros = [
    {"id": "r1", "vec": [1.0, 0.0], "meta": {"idioma": "pt", "ano": 2023}},
    {"id": "r2", "vec": [0.9, 0.1], "meta": {"idioma": "en", "ano": 2023}},
    {"id": "r3", "vec": [0.8, 0.2], "meta": {"idioma": "pt", "ano": 2021}},
    {"id": "r4", "vec": [0.0, 1.0], "meta": {"idioma": "pt", "ano": 2023}},
]
consulta = [1.0, 0.0]


def cosseno(a, b):
    a, b = np.array(a, float), np.array(b, float)
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))


def buscar(consulta, filtro, k=3):
    cand = [r for r in registros
            if all(r["meta"].get(c) == v for c, v in filtro.items())]
    rank = sorted(((r["id"], cosseno(consulta, r["vec"])) for r in cand),
                  key=lambda t: (-t[1], t[0]))
    return [vid for vid, _ in rank[:k]]


print("sem filtro:", buscar(consulta, {}, k=3))
print("filtro idioma=pt:", buscar(consulta, {"idioma": "pt"}, k=3))
print("filtro idioma=pt ano=2023:", buscar(consulta, {"idioma": "pt", "ano": 2023}, k=3))
