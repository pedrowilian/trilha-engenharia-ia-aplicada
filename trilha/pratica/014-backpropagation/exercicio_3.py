"""Licao 014 — Exercicio 3: gradient checking de w e b.

Tarefa:
- Neuronio sigmoide com BCE. x=-1.0, y=0.0, w=0.8, b=-0.2.
- Gradiente analitico: dL/dw = (p-y)*x, dL/db = (p-y).
- Gradiente numerico por diferencas centrais com h=1e-5 para cada parametro.
- Imprima `w: analitico=... numerico=...` e `b: analitico=... numerico=...`
  (6 casas) e `gradientes conferem: <bool>` (ambas as diferencas < 1e-6).

Criterio binario: saida IDENTICA a
trilha/solucoes/014-backpropagation/solucao_3.saida.txt
"""
import math


def sigmoid(z):
    return 1.0 / (1.0 + math.exp(-z))


def perda(w, b, x, y):
    raise NotImplementedError


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
