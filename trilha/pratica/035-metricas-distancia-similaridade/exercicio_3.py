"""Exercício 3 — Normalizar torna dot = cosseno.

Setup:
    pares = [([3.0, 4.0], [4.0, 3.0]),
             ([1.0, 0.0], [0.0, 5.0]),
             ([2.0, 1.0], [4.0, 2.0])]

Tarefa:
    Implemente normalizar(u) (divide pelo comprimento L2). Para cada par,
    compare o produto interno dos vetores NORMALIZADOS com o cosseno dos
    ORIGINAIS (igualdade até 6 casas) e imprima dot_norm, cos e iguais.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/035-metricas-distancia-similaridade/solucao_3.saida.txt
    (toda linha termina com iguais=True).
"""
import math

pares = [([3.0, 4.0], [4.0, 3.0]),
         ([1.0, 0.0], [0.0, 5.0]),
         ([2.0, 1.0], [4.0, 2.0])]

# TODO: implementar normalizar e comparar dot(normalizado) com cos_sim(original).
