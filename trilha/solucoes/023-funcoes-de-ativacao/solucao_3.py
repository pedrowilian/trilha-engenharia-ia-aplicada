"""Solucao de referencia — Licao 023, Exercicio 3.

Compara o "neuronio morto" sob ReLU e Leaky ReLU: para entradas negativas, a
ReLU zera o gradiente (neuronio nao aprende mais), enquanto a Leaky ReLU mantem
um gradiente pequeno e diferente de zero.
"""
import numpy as np


def grad_relu(z):
    return np.where(z > 0.0, 1.0, 0.0)


def grad_leaky_relu(z, a=0.01):
    return np.where(z > 0.0, 1.0, a)


def main():
    z = np.array([-2.0, -0.5, 0.3, 1.0])
    g_relu = grad_relu(z)
    g_leaky = grad_leaky_relu(z)
    print(f"grad ReLU:        {g_relu}")
    print(f"grad Leaky ReLU:  {g_leaky}")
    mortos_relu = int(np.sum(g_relu == 0.0))
    mortos_leaky = int(np.sum(g_leaky == 0.0))
    print(f"neuronios sem gradiente (ReLU):       {mortos_relu}")
    print(f"neuronios sem gradiente (Leaky ReLU): {mortos_leaky}")


if __name__ == "__main__":
    main()
