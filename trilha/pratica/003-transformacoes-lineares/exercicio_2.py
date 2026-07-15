"""Exercício 2 — Rotação de 180° aplicada a um conjunto de pontos.

Setup:
    R = [[-1.0, 0.0], [0.0, -1.0]]   # rotação de 180°
    pts = [[1, 0], [0, 2], [3, -4]]  # cada linha é um ponto

Tarefa:
    1. Aplique a transformação a todos os pontos de uma vez: (R @ pts.T).T.
    2. Confirme com np.allclose que aplicá-la duas vezes volta aos pontos
       originais.
    3. Imprima, exatamente:
        pontos: [[1.0, 0.0], [0.0, 2.0], [3.0, -4.0]]
        rotacionados: [[-1.0, 0.0], [0.0, -2.0], [-3.0, 4.0]]
        dupla rotacao volta ao inicio? True

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/003-transformacoes-lineares/solucao_2.saida.txt
"""
import numpy as np

R = np.array([[-1.0, 0.0],
              [0.0, -1.0]])

pts = np.array([[1.0, 0.0],
                [0.0, 2.0],
                [3.0, -4.0]])

# TODO: aplicar a rotação, imprimir os pontos e os rotacionados, e verificar
# que a dupla rotação retorna ao início.
