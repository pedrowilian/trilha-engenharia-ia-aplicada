"""Exercício 2 — Recuperar os top-3.

Setup:
    base = {"doc_a": [2.0, 3.0], "doc_b": [0.0, 1.0], "doc_c": [5.0, 4.0],
            "doc_d": [1.0, 0.0], "doc_e": [2.0, 1.0]}
    q = [1.0, 1.0]

Tarefa:
    Implemente knn(q, base, k) que ordena por distância (desempate por id) e
    devolve os k primeiros. Imprima os 3 mais próximos com distância (4 casas).

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/036-busca-vetorial-knn-exato/solucao_2.saida.txt
"""
import math

base = {
    "doc_a": [2.0, 3.0],
    "doc_b": [0.0, 1.0],
    "doc_c": [5.0, 4.0],
    "doc_d": [1.0, 0.0],
    "doc_e": [2.0, 1.0],
}
q = [1.0, 1.0]

# TODO: implementar l2 e knn(q, base, k); imprimir o top-3.
