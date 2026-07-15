"""Solucao de referencia — Licao 021, Exercicio 3.

Peeking: espiar o p-valor repetidas vezes e parar no primeiro p<0.05 infla a
taxa de falso-positivo muito acima do alfa nominal (demonstrado em testes A/A).
"""
import math
import numpy as np


def phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def z_test(x1, n1, x2, n2):
    p_pool = (x1 + x2) / (n1 + n2)
    if p_pool in (0.0, 1.0):
        return 1.0
    se = math.sqrt(p_pool * (1 - p_pool) * (1 / n1 + 1 / n2))
    if se == 0:
        return 1.0
    z = (x2 / n2 - x1 / n1) / se
    return 2 * (1 - phi(abs(z)))


def main():
    rng = np.random.default_rng(4)
    p_real = 0.15           # MESMA taxa nos dois grupos (A/A)
    n_experimentos = 1000
    n_max = 2400
    checkpoints = range(300, n_max + 1, 300)

    fp_peeking = 0
    fp_final = 0
    for _ in range(n_experimentos):
        a = (rng.uniform(0, 1, size=n_max) < p_real).astype(int)
        b = (rng.uniform(0, 1, size=n_max) < p_real).astype(int)
        if any(z_test(a[:n].sum(), n, b[:n].sum(), n) < 0.05 for n in checkpoints):
            fp_peeking += 1
        if z_test(a.sum(), n_max, b.sum(), n_max) < 0.05:
            fp_final += 1

    print(f"falso-positivo so no fim:   {fp_final / n_experimentos:.3f}")
    print(f"falso-positivo com peeking: {fp_peeking / n_experimentos:.3f}")
    print("peeking infla o falso-positivo:",
          fp_peeking / n_experimentos > fp_final / n_experimentos)


if __name__ == "__main__":
    main()
