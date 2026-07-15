"""Exercício 3 — Recuperação por similaridade do cosseno (top-k).

Setup: a memória com três episódios (texto + embedding) e a consulta
    consulta = np.array([1.0, 0.0, 0.0]).

Tarefa:
    Implemente `cosseno(u, v)`. Ordene a memória por similaridade decrescente
    com a consulta e imprima os 2 episódios mais parecidos no formato
    `{texto}: {similaridade:.3f}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/067-memoria-de-agentes/solucao_3.saida.txt
"""
import numpy as np

memoria = [
    ("python e linguagem", np.array([1.0, 0.0, 0.0])),
    ("cobra python", np.array([0.8, 0.2, 0.0])),
    ("cafe quente", np.array([0.0, 0.0, 1.0])),
]
consulta = np.array([1.0, 0.0, 0.0])

# TODO: implemente cosseno e recupere os top-2 episódios.
