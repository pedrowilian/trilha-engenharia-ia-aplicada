"""Solucao de referencia - Exercicio 3 da Licao 056.

Indice invertido: mapa termo -> lista de chunks que o contem (postings). A busca
por varios termos e a intersecao das postings. E a base da indexacao esparsa.
"""
import re


chunks = {
    "c0": "instalacao do produto em windows",
    "c1": "instalacao do produto em linux",
    "c2": "remocao do produto em windows",
}


def tokenizar(t):
    return re.findall(r"[a-z0-9]+", t.lower())


def construir_indice(chunks):
    indice = {}
    for cid in sorted(chunks):
        for termo in sorted(set(tokenizar(chunks[cid]))):
            indice.setdefault(termo, []).append(cid)
    return indice


def buscar(indice, consulta):
    conjuntos = [set(indice.get(t, [])) for t in set(tokenizar(consulta))]
    if not conjuntos:
        return []
    return sorted(set.intersection(*conjuntos))


indice = construir_indice(chunks)
print("postings 'windows':", indice["windows"])
print("postings 'instalacao':", indice["instalacao"])
print("instalacao windows:", buscar(indice, "instalacao windows"))
