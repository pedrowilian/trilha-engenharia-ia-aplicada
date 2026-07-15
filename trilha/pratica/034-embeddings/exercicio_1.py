"""Exercício 1 — Vizinho mais próximo numa tabela de embeddings.

Setup:
    emb = {
        "gato":     [0.9, 0.1, 0.0],
        "cachorro": [0.8, 0.2, 0.1],
        "felino":   [0.85, 0.15, 0.0],
        "carro":    [0.0, 0.1, 0.9],
    }
    consulta = "gato"

Tarefa:
    Implemente cos_sim(u, v) e ordene as demais palavras por similaridade
    decrescente (desempate alfabético). Imprima o ranking e o vizinho mais
    próximo da consulta.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/034-embeddings/solucao_1.saida.txt
"""
import math

emb = {
    "gato":     [0.9, 0.1, 0.0],
    "cachorro": [0.8, 0.2, 0.1],
    "felino":   [0.85, 0.15, 0.0],
    "carro":    [0.0, 0.1, 0.9],
}
consulta = "gato"

# TODO: implementar cos_sim, ranquear vizinhos e imprimir o mais próximo.
