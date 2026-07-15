"""Exercício 2 — Rotação de 180° aplicada a um conjunto de pontos.

Setup: matriz de rotação de 180° e três pontos do plano.
Objetivo: aplicar a transformação a todos os pontos de uma vez e confirmar que
aplicá-la duas vezes retorna aos pontos originais.
"""
import numpy as np

# Rotação de 180°: inverte ambos os eixos.
R = np.array([[-1.0, 0.0],
              [0.0, -1.0]])

pts = np.array([[1.0, 0.0],
                [0.0, 2.0],
                [3.0, -4.0]])

rot = (R @ pts.T).T + 0.0          # + 0.0 normaliza eventuais -0.0

print("pontos:", pts.tolist())
print("rotacionados:", rot.tolist())
print("dupla rotacao volta ao inicio?", np.allclose(R @ (R @ pts.T), pts.T))
