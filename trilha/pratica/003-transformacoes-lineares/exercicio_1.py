"""Exercício 1 — Produto matriz-vetor do zero e teste de linearidade.

Setup:
    A = [[2.0, -1.0], [0.0, 3.0]]
    u = [1.0, 2.0]
    v = [3.0, -1.0]
    a, b = 2.0, -1.0

Tarefa:
    1. Implemente `matvec(A, x)` com laços (cada saída é o produto interno de
       uma linha de A por x).
    2. Calcule T(a*u + b*v) e a*T(u) + b*T(v).
    3. Confirme a linearidade com np.allclose e imprima, exatamente:
        T(a*u + b*v): [-7.0, 15.0]
        a*T(u)+b*T(v): [-7.0, 15.0]
        linear? True

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/003-transformacoes-lineares/solucao_1.saida.txt
"""
import numpy as np

A = np.array([[2.0, -1.0],
              [0.0, 3.0]])


def matvec(A, x):
    # TODO: retornar o produto matriz-vetor calculado com laços
    raise NotImplementedError


u = np.array([1.0, 2.0])
v = np.array([3.0, -1.0])
a, b = 2.0, -1.0

# TODO: calcular e imprimir T(a*u + b*v), a*T(u)+b*T(v) e o teste de linearidade.
