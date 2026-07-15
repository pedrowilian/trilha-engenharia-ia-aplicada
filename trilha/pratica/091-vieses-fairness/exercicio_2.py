"""Exercício 2 — Equalized odds (TPR e FPR por grupo).

Setup:
    y    = np.array([1, 1, 1, 0, 0, 1, 1, 0, 0, 0])   # rótulo verdadeiro
    pred = np.array([1, 1, 0, 0, 0, 1, 1, 1, 1, 0])   # predição
    grp  = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])   # grupo protegido

Tarefa:
    Implemente `taxas(yv, pv)` que devolve (TPR, FPR), com
    TPR = TP / (TP + FN) e FPR = FP / (FP + TN). Para cada grupo (A=0, B=1)
    imprima `"grupo {nome}: TPR={tpr:.2f} FPR={fpr:.2f}"`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/091-vieses-fairness/solucao_2.saida.txt
"""
import numpy as np

# TODO: calcule TPR e FPR por grupo a partir das contagens da matriz de confusão.
