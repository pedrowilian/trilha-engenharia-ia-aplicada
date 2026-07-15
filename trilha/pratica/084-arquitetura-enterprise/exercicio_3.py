"""Exercício 3 — Painel de observabilidade.

Setup:
    latencias = [70, 65, 80, 500, 72, 68, 90, 75, 60, 400]   # ms
    erros = [0, 0, 0, 1, 0, 0, 0, 0, 0, 1]

Tarefa:
    Calcule p50 e p95 com numpy.percentile e taxa_erro como a média de erros.
    Imprima `p50 = {p50:.1f} ms`, `p95 = {p95:.1f} ms` e
    `taxa de erro = {taxa_erro:.1%}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/084-arquitetura-enterprise/solucao_3.saida.txt
"""
import numpy as np

latencias = np.array([70, 65, 80, 500, 72, 68, 90, 75, 60, 400])
erros = np.array([0, 0, 0, 1, 0, 0, 0, 0, 0, 1])

# TODO: agregue p50, p95 e a taxa de erro da janela.
