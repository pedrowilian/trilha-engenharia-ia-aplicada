"""Solucao de referencia — Licao 025, Exercicio 3.

Com a inicializacao de He, a variancia das ativacoes se mantem saudavel ao
atravessar varias camadas ReLU (nem explode nem desaparece).
"""
import numpy as np


def main():
    rng = np.random.default_rng(3)
    n = 256
    a = rng.standard_normal(n)
    stds = []
    for _ in range(5):
        W = rng.standard_normal((n, n)) * np.sqrt(2.0 / n)
        a = np.maximum(0.0, W @ a)
        stds.append(a.std())
    saudavel = all(0.3 < s < 1.0 for s in stds)
    print("std por camada:", np.round(stds, 4))
    print("todas as camadas saudaveis (0.3<std<1.0):", saudavel)


if __name__ == "__main__":
    main()
