"""Exercício 3 — Forward pass de uma rede neural de 2 camadas.

Setup:
    x = [1.0, 2.0]
    W1 (3x2), b1, W2 (2x3), b2  (valores fixos abaixo)

Tarefa:
    1. Implemente relu(z) = max(0, z) (elemento a elemento).
    2. Calcule h = ReLU(W1 @ x + b1) e y = W2 @ h + b2.
    3. Imprima, exatamente:
        h (camada oculta): [0.0, 2.0, 2.0]
        y (saida): [-2.0, 2.0]

Cada camada é uma transformação linear (matriz) seguida de viés e não-linearidade.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/003-transformacoes-lineares/solucao_3.saida.txt
"""
import numpy as np

x = np.array([1.0, 2.0])

W1 = np.array([[0.5, -0.5],
               [1.0,  0.0],
               [-1.0, 2.0]])
b1 = np.array([0.0, 1.0, -1.0])

W2 = np.array([[1.0, 0.0, -1.0],
               [0.5, 0.5, 0.5]])
b2 = np.array([0.0, 0.0])


def relu(z):
    # TODO: aplicar max(0, z) elemento a elemento
    raise NotImplementedError


# TODO: calcular h e y e imprimir conforme o formato especificado.
