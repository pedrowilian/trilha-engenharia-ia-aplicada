"""Solucao de referencia — Licao 020, Exercicio 3.

Leakage temporal numa serie com MUDANCA DE REGIME: o split aleatorio mistura
passado e futuro (vaza) e fica otimista; o split temporal treina so no passado
e precisa extrapolar o regime novo, revelando o erro real (maior).
"""
import numpy as np


def main():
    rng = np.random.default_rng(8)
    T = 220
    t = np.arange(T)
    serie = np.where(t < 110, 0.15 * t, 0.15 * 110 + 1.4 * (t - 110))
    serie = serie + rng.normal(0, 3, size=T)

    def avaliar(idx_tr, idx_te):
        coef = np.polyfit(t[idx_tr], serie[idx_tr], 1)
        pred = np.polyval(coef, t[idx_te])
        return float(np.mean((pred - serie[idx_te]) ** 2))

    perm = rng.permutation(T)
    erro_aleatorio = avaliar(perm[:165], perm[165:])
    erro_temporal = avaliar(np.arange(165), np.arange(165, T))

    print(f"erro split aleatorio (otimista): {erro_aleatorio:.2f}")
    print(f"erro split temporal (honesto):   {erro_temporal:.2f}")
    print("split temporal e mais conservador:", erro_temporal > erro_aleatorio)


if __name__ == "__main__":
    main()
