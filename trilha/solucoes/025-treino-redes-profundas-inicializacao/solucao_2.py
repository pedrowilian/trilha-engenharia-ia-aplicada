"""Solucao de referencia — Licao 025, Exercicio 2.

Calcula o desvio-padrao teorico das inicializacoes de Xavier (1/sqrt(n_in)) e
de He (sqrt(2/n_in)) para diferentes tamanhos de fan-in.
"""
import numpy as np


def main():
    for n_in in [16, 256, 1024]:
        xavier = 1.0 / np.sqrt(n_in)
        he = np.sqrt(2.0 / n_in)
        print(f"n_in={n_in:5d}: Xavier std={xavier:.4f} He std={he:.4f}")


if __name__ == "__main__":
    main()
