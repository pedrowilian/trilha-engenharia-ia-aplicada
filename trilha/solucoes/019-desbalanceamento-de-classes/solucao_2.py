"""Solucao de referencia — Licao 019, Exercicio 2.

Precision, recall e F1 a partir da matriz de confusao (classe positiva = 1).
"""


def metricas(y_real, y_pred):
    VP = sum(1 for r, p in zip(y_real, y_pred) if r == 1 and p == 1)
    FP = sum(1 for r, p in zip(y_real, y_pred) if r == 0 and p == 1)
    FN = sum(1 for r, p in zip(y_real, y_pred) if r == 1 and p == 0)
    VN = sum(1 for r, p in zip(y_real, y_pred) if r == 0 and p == 0)
    prec = VP / (VP + FP) if (VP + FP) else 0.0
    rec = VP / (VP + FN) if (VP + FN) else 0.0
    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) else 0.0
    return VP, FP, FN, VN, prec, rec, f1


def main():
    y_real = [1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0]
    y_pred = [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0]
    VP, FP, FN, VN, prec, rec, f1 = metricas(y_real, y_pred)
    print(f"VP={VP} FP={FP} FN={FN} VN={VN}")
    print(f"precision: {prec:.4f}")
    print(f"recall:    {rec:.4f}")
    print(f"F1:        {f1:.4f}")


if __name__ == "__main__":
    main()
