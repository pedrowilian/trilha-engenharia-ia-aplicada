"""Solucao de referencia — Licao 028, Exercicio 2.

RMSProp normaliza o tamanho do passo: no primeiro passo, o passo efetivo e
~eta/sqrt(1-beta) independentemente da MAGNITUDE do gradiente. Dois gradientes
com escalas muito diferentes recebem passos quase identicos.
"""
import numpy as np


def main():
    eta = 0.01
    beta = 0.9
    eps = 1e-8
    g = np.array([100.0, 0.01])     # escalas diferindo por 10^4
    s = beta * 0.0 + (1.0 - beta) * g * g
    passo = eta * g / (np.sqrt(s) + eps)
    print(f"gradiente:     {g}")
    print(f"passo efetivo: {np.round(passo, 6)}")
    print(f"passos quase iguais: {np.isclose(passo[0], passo[1], atol=1e-4)}")


if __name__ == "__main__":
    main()
