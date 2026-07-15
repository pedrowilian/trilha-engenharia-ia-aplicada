"""Solução de referência — Exercício 1 da Lição 091.

Paridade demográfica: taxa de seleção (predição positiva) por grupo protegido e a
diferença entre elas. Determinístico.
"""
import numpy as np

grupo = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
pred = np.array([1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0])

taxa_a = float(pred[grupo == 0].mean())
taxa_b = float(pred[grupo == 1].mean())
print(f"taxa selecao grupo A: {taxa_a:.2f}")
print(f"taxa selecao grupo B: {taxa_b:.2f}")
print(f"diferenca de paridade: {taxa_a - taxa_b:+.2f}")
