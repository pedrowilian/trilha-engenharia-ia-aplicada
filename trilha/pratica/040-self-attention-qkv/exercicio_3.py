"""Exercício 3 — Saída é combinação convexa dos Values.

Setup:
    V = [[0,10],[2,8],[5,5],[9,1]] ; pesos = [0.1, 0.2, 0.3, 0.4]

Tarefa:
    Calcule saida = pesos @ V. Imprima a soma dos pesos (4 casas), a saída
    arredondada (4 casas) e um booleano indicando se a saída cai dentro do
    envoltório convexo de V (entre min e max de cada coluna).

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/040-self-attention-qkv/solucao_3.saida.txt
"""
import numpy as np

V = np.array([[0.0, 10.0], [2.0, 8.0], [5.0, 5.0], [9.0, 1.0]])
pesos = np.array([0.1, 0.2, 0.3, 0.4])

# TODO: media ponderada, soma dos pesos e verificacao do envoltorio convexo.
