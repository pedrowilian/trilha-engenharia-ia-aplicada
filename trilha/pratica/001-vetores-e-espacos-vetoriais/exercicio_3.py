"""Exercício 3 — Independência linear e coordenadas em uma base.

Setup:
    b1 = [2.0, 0.0]
    b2 = [0.0, 3.0]
    x  = [6.0, 9.0]

Tarefa:
    1. Monte B = [b1 b2] (colunas) e calcule seu determinante.
    2. Decida se {b1, b2} formam base (determinante diferente de zero).
    3. Calcule as coordenadas de x na base resolvendo B @ c = x.
    4. Imprima (determinante e coordenadas arredondados a 4 casas):
        determinante: 6.0
        forma base?  True
        coordenadas: [3.0, 3.0]

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/001-vetores-e-espacos-vetoriais/solucao_3.saida.txt
"""
import numpy as np

b1 = np.array([2.0, 0.0])
b2 = np.array([0.0, 3.0])
x = np.array([6.0, 9.0])

# TODO: calcular determinante, verificar base e resolver as coordenadas.
