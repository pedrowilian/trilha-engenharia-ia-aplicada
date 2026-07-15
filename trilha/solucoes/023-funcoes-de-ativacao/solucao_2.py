"""Solucao de referencia — Licao 023, Exercicio 2.

Aplica ReLU a um vetor e mede a esparsidade resultante: quantos neuronios ficam
ativos (saida > 0) e desligados (saida == 0), e a ativacao media.
"""
import numpy as np


def relu(z):
    return np.maximum(0.0, z)


def main():
    z = np.array([-3.0, -1.0, -0.2, 0.0, 0.7, 1.5, 4.0])
    a = relu(z)
    ativos = int(np.sum(a > 0.0))
    desligados = int(np.sum(a == 0.0))
    print(f"entrada: {z}")
    print(f"relu:    {a}")
    print(f"ativos={ativos} desligados={desligados}")
    print(f"ativacao media: {a.mean():.4f}")


if __name__ == "__main__":
    main()
