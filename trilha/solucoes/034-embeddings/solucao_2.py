"""Solução de referência — Exercício 2 da Lição 034.

Resolve a analogia vetorial "a está para b assim como c está para ?" via
aritmética de embeddings: alvo = b - a + c, e busca o vizinho mais próximo
(excluindo as palavras da consulta) por similaridade do cosseno.
"""
import math

emb = {
    "franca": [1.0, 0.0],
    "paris":  [1.0, 1.0],
    "italia": [0.0, 1.0],
    "roma":   [0.0, 2.0],
    "carro":  [-1.0, -1.0],
}


def cos_sim(u, v):
    dot = sum(x * y for x, y in zip(u, v))
    nu = math.sqrt(sum(x * x for x in u))
    nv = math.sqrt(sum(y * y for y in v))
    return dot / (nu * nv)


def analogia(a, b, c, emb):
    alvo = [bb - aa + cc for aa, bb, cc in zip(emb[a], emb[b], emb[c])]
    candidatos = [p for p in emb if p not in (a, b, c)]
    ranking = sorted(candidatos, key=lambda p: (-cos_sim(alvo, emb[p]), p))
    return alvo, ranking[0]


alvo, resposta = analogia("franca", "paris", "italia", emb)
print("paris esta para franca assim como ? esta para italia")
print("vetor alvo:", alvo)
print("resposta:", resposta)
