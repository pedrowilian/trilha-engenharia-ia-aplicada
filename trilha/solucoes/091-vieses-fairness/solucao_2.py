"""Solução de referência — Exercício 2 da Lição 091.

Equalized odds: taxa de verdadeiros positivos (TPR) e de falsos positivos (FPR)
por grupo. A equidade exige TPR e FPR próximos entre os grupos. Determinístico.
"""
import numpy as np

y = np.array([1, 1, 1, 0, 0, 1, 1, 0, 0, 0])
pred = np.array([1, 1, 0, 0, 0, 1, 1, 1, 1, 0])
grp = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])


def taxas(yv, pv):
    tp = int(((pv == 1) & (yv == 1)).sum())
    fn = int(((pv == 0) & (yv == 1)).sum())
    fp = int(((pv == 1) & (yv == 0)).sum())
    tn = int(((pv == 0) & (yv == 0)).sum())
    tpr = tp / (tp + fn) if (tp + fn) else 0.0
    fpr = fp / (fp + tn) if (fp + tn) else 0.0
    return tpr, fpr


for g, nome in [(0, "A"), (1, "B")]:
    tpr, fpr = taxas(y[grp == g], pred[grp == g])
    print(f"grupo {nome}: TPR={tpr:.2f} FPR={fpr:.2f}")
