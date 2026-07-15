"""Solucao de referencia — Licao 018, Exercicio 2.

Calcula o Expected Calibration Error (ECE) e confirma que um modelo calibrado
tem ECE menor que um superconfiante.
"""
import numpy as np


def ece(p_pred, y, N, n_bins=10):
    bins = np.linspace(0, 1, n_bins + 1)
    idx = np.clip(np.digitize(p_pred, bins) - 1, 0, n_bins - 1)
    total = 0.0
    for b in range(n_bins):
        sel = idx == b
        if sel.sum() == 0:
            continue
        total += (sel.sum() / N) * abs(p_pred[sel].mean() - y[sel].mean())
    return total


def main():
    rng = np.random.default_rng(11)
    N = 6000
    p_verdadeira = rng.uniform(0.02, 0.98, size=N)
    y = (rng.uniform(0, 1, size=N) < p_verdadeira).astype(int)
    logit_cal = np.log(p_verdadeira / (1 - p_verdadeira))

    p_calibrado = p_verdadeira
    p_super = 1.0 / (1.0 + np.exp(-2.5 * logit_cal))
    ece_cal = ece(p_calibrado, y, N)
    ece_sup = ece(p_super, y, N)
    print(f"ECE calibrado:      {ece_cal:.4f}")
    print(f"ECE superconfiante: {ece_sup:.4f}")
    print("calibrado tem ECE menor:", ece_cal < ece_sup)


if __name__ == "__main__":
    main()
