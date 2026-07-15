"""Solução de referência — Exercício 3 da Lição 038.

Mostra o papel do parâmetro `ef` (largura da busca em feixe) na qualidade do
HNSW: com ef=1 a busca pode ficar presa num ótimo local; aumentar ef explora
mais candidatos e encontra o vizinho verdadeiro, ao custo de mais comparações.
"""
import math


def dist(u, v):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(u, v)))


coords = {"e": [0.0, 0.0], "A": [1.0, 1.0], "B": [1.0, -1.0],
          "C": [2.0, 2.0], "T": [3.0, 0.0]}
grafo = {"e": ["A", "B"], "A": ["e", "C"], "B": ["e", "T"],
         "C": ["A"], "T": ["B"]}
q = [3.1, 0.0]
exato = min(coords, key=lambda n: (dist(q, coords[n]), n))


def search_layer(q, entrada, ef):
    visitados = {entrada}
    candidatos = [entrada]
    resultado = [entrada]
    comps = 1
    while candidatos:
        c = min(candidatos, key=lambda n: (dist(q, coords[n]), n))
        candidatos.remove(c)
        pior = max(resultado, key=lambda n: (dist(q, coords[n]), n))
        if dist(q, coords[c]) > dist(q, coords[pior]):
            break
        for nb in grafo[c]:
            if nb not in visitados:
                visitados.add(nb)
                comps += 1
                pior = max(resultado, key=lambda n: (dist(q, coords[n]), n))
                if dist(q, coords[nb]) < dist(q, coords[pior]) or len(resultado) < ef:
                    candidatos.append(nb)
                    resultado.append(nb)
                    if len(resultado) > ef:
                        pior = max(resultado, key=lambda n: (dist(q, coords[n]), n))
                        resultado.remove(pior)
    melhor = min(resultado, key=lambda n: (dist(q, coords[n]), n))
    return melhor, comps


print("exato:", exato)
for ef in (1, 2, 3):
    achado, comps = search_layer(q, "e", ef)
    print(f"ef={ef}: achado={achado} comparacoes={comps} acerto={achado == exato}")
