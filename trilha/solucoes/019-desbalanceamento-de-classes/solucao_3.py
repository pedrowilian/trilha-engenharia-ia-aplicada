"""Solucao de referencia — Licao 019, Exercicio 3.

Ajuste de limiar em dados desbalanceados: encontra o limiar que maximiza o F1,
mostrando que 0.5 raramente e o melhor corte sob desbalanceamento.
"""
import numpy as np


def main():
    rng = np.random.default_rng(5)
    N = 3000
    y = (rng.uniform(0, 1, size=N) < 0.08).astype(int)
    score = np.where(y == 1,
                     rng.normal(0.60, 0.15, size=N),
                     rng.normal(0.35, 0.15, size=N))
    score = np.clip(score, 0, 1)

    def f1_no_limiar(limiar):
        pred = (score >= limiar).astype(int)
        VP = int(((pred == 1) & (y == 1)).sum())
        FP = int(((pred == 1) & (y == 0)).sum())
        FN = int(((pred == 0) & (y == 1)).sum())
        prec = VP / (VP + FP) if (VP + FP) else 0.0
        rec = VP / (VP + FN) if (VP + FN) else 0.0
        return 2 * prec * rec / (prec + rec) if (prec + rec) else 0.0

    melhor_limiar, melhor_f1 = 0.5, 0.0
    for limiar in np.linspace(0.3, 0.8, 26):
        f1 = f1_no_limiar(limiar)
        if f1 > melhor_f1:
            melhor_f1, melhor_limiar = f1, limiar

    print(f"F1 com limiar 0.5: {f1_no_limiar(0.5):.4f}")
    print(f"melhor limiar: {melhor_limiar:.2f}")
    print(f"melhor F1: {melhor_f1:.4f}")
    print("limiar ajustado supera 0.5:", melhor_f1 > f1_no_limiar(0.5))


if __name__ == "__main__":
    main()
