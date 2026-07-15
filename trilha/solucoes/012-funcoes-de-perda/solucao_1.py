"""Solucao de referencia — Licao 012, Exercicio 1.

MSE e MAE do zero para um problema de regressao, comparando duas predicoes.
"""


def mse(y_real, y_pred):
    n = len(y_real)
    return sum((yr - yp) ** 2 for yr, yp in zip(y_real, y_pred)) / n


def mae(y_real, y_pred):
    n = len(y_real)
    return sum(abs(yr - yp) for yr, yp in zip(y_real, y_pred)) / n


def main():
    y_real = [10.0, 12.0, 14.0, 16.0, 18.0]
    pred_a = [11.0, 11.0, 15.0, 15.0, 19.0]   # erros pequenos espalhados
    pred_b = [10.0, 12.0, 14.0, 16.0, 28.0]   # um unico erro grande (outlier)
    print(f"pred_a: MSE={mse(y_real, pred_a):.4f} MAE={mae(y_real, pred_a):.4f}")
    print(f"pred_b: MSE={mse(y_real, pred_b):.4f} MAE={mae(y_real, pred_b):.4f}")
    print("MSE pune mais o outlier:", mse(y_real, pred_b) > mse(y_real, pred_a))


if __name__ == "__main__":
    main()
