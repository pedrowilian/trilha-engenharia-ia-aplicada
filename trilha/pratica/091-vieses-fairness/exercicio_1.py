"""Exercício 1 — Paridade demográfica.

Setup:
    grupo = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
    pred  = np.array([1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0])
(`pred == 1` significa decisão positiva; `grupo` é o atributo protegido).

Tarefa:
    Calcule a taxa de seleção de cada grupo (`pred[grupo == g].mean()`) e a
    diferença A - B. Imprima `"taxa selecao grupo A: {taxa_a:.2f}"`,
    `"taxa selecao grupo B: {taxa_b:.2f}"` e
    `"diferenca de paridade: {taxa_a - taxa_b:+.2f}"`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/091-vieses-fairness/solucao_1.saida.txt
"""
import numpy as np

# TODO: calcule as taxas de seleção por grupo e a diferença de paridade.
