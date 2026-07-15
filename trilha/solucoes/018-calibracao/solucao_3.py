"""Solucao de referencia — Licao 018, Exercicio 3.

Temperature scaling: busca a temperatura T que minimiza o ECE de um modelo
superconfiante, recuperando a calibracao sem alterar a ordem das predicoes.
"""
import numpy as np


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


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
    rng = np.random.default_rng(20)
    N = 8000
    p_verdadeira = rng.uniform(0.02, 0.98, size=N)
    y = (rng.uniform(0, 1, size=N) < p_verdadeira).astype(int)
    logit_cal = np.log(p_verdadeira / (1 - p_verdadeira))
    logits = 3.0 * logit_cal   # superconfiante (fator 3)

    ece_T1 = ece(sigmoid(logits), y, N)
    melhor_T, melhor_ece = 1.0, ece_T1
    for T in np.linspace(1.0, 5.0, 41):
        e = ece(sigmoid(logits / T), y, N)
        if e < melhor_ece:
            melhor_ece, melhor_T = e, T

    print(f"ECE com T=1.0: {ece_T1:.4f}")
    print(f"melhor T: {melhor_T:.1f}")
    print(f"ECE com melhor T: {melhor_ece:.4f}")
    print("temperature scaling melhorou:", melhor_ece < ece_T1)


if __name__ == "__main__":
    main()
