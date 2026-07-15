"""Exercício 1 — Varredura linear exata.

Setup:
    base = {"doc_a": [2.0, 3.0], "doc_b": [0.0, 1.0],
            "doc_c": [5.0, 4.0], "doc_d": [1.0, 0.0]}
    q = [1.0, 1.0]

Tarefa:
    Implemente l2(u, v), imprima a distância de q a cada documento e o mais
    próximo (desempate por identificador). Esperado: mais proximo: doc_b.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/036-busca-vetorial-knn-exato/solucao_1.saida.txt
"""
import math

base = {
    "doc_a": [2.0, 3.0],
    "doc_b": [0.0, 1.0],
    "doc_c": [5.0, 4.0],
    "doc_d": [1.0, 0.0],
}
q = [1.0, 1.0]

# TODO: implementar l2, imprimir distâncias e o vizinho mais próximo.
