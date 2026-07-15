"""Licao 014 — Exercicio 2: um passo de backprop + gradient descent.

Tarefa:
- Neuronio sigmoide com BCE. x=1.5, y=1.0, w=-1.0, b=0.0, eta=0.5.
- Forward: p = sigmoid(w*x+b); L = BCE(y, p).
- Backward: dL/dz = p - y; dL/dw = dL/dz * x; dL/db = dL/dz. De um passo de GD.
- Imprima `perda antes: ...`, `dL/dw=... dL/db=...` (4 casas), `perda depois: ...`
  e `perda diminuiu: <bool>`.

Criterio binario: saida IDENTICA a
trilha/solucoes/014-backpropagation/solucao_2.saida.txt
"""
import math


def sigmoid(z):
    return 1.0 / (1.0 + math.exp(-z))


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
