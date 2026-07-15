"""Solucao de referencia — Licao 018, Exercicio 1.

Tabela de confiabilidade (reliability) de um modelo SUPERCONFIANTE: em faixas de
alta confianca, a frequencia observada fica ABAIXO da probabilidade prevista.
"""
import numpy as np


def main():
    rng = np.random.default_rng(3)
    N = 6000
    p_verdadeira = rng.uniform(0.02, 0.98, size=N)
    y = (rng.uniform(0, 1, size=N) < p_verdadeira).astype(int)

    # modelo superconfiante: logits 2x o calibrado
    logit_cal = np.log(p_verdadeira / (1 - p_verdadeira))
    p_pred = 1.0 / (1.0 + np.exp(-2.0 * logit_cal))

    bins = np.linspace(0, 1, 6)
    idx = np.clip(np.digitize(p_pred, bins) - 1, 0, 4)
    print("faixa | prob_media | freq_positivos")
    for b in range(5):
        sel = idx == b
        if sel.sum() == 0:
            continue
        print(f"  {b}   |   {p_pred[sel].mean():.3f}   |   {y[sel].mean():.3f}")


if __name__ == "__main__":
    main()
