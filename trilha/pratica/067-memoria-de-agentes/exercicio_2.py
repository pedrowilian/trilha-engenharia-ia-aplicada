"""Exercício 2 — Memória episódica de longo prazo.

Setup: grave três episódios (texto + embedding):
    ("python e linguagem", [1.0, 0.0, 0.0])
    ("cobra python",        [0.8, 0.2, 0.0])
    ("cafe quente",         [0.0, 0.0, 1.0])

Tarefa:
    Implemente `gravar(texto, vetor)` armazenando um dict {"texto", "vetor"}
    (vetor como np.array de float). Após gravar os três, imprima
    `episodios: {n}` e, para cada um, `{texto} -> {vetor como lista}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/067-memoria-de-agentes/solucao_2.saida.txt
"""
import numpy as np

memoria = []

# TODO: implemente gravar e registre os três episódios.
