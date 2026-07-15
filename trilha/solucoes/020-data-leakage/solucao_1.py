"""Solucao de referencia — Licao 020, Exercicio 1.

Target leakage: uma feature derivada do rotulo produz acuracia "boa demais".
Compara um modelo com e sem a feature vazada.
"""
import numpy as np


def acuracia_threshold(x, y):
    return float(((x >= 0).astype(int) == y).mean())


def main():
    rng = np.random.default_rng(10)
    N = 500
    y = (rng.uniform(0, 1, size=N) < 0.5).astype(int)
    x_legit = 0.4 * (2 * y - 1) + rng.normal(0, 1.0, size=N)
    x_leaky = (2 * y - 1) + rng.normal(0, 0.03, size=N)

    acc_legit = acuracia_threshold(x_legit, y)
    acc_leaky = acuracia_threshold(x_leaky, y)
    print(f"acuracia feature legitima: {acc_legit:.3f}")
    print(f"acuracia feature vazada:   {acc_leaky:.3f}")
    print("suspeita de leakage:", acc_leaky > 0.95 and acc_leaky - acc_legit > 0.2)


if __name__ == "__main__":
    main()
