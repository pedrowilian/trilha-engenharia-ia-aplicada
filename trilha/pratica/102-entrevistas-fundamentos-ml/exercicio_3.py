"""Exercicio 3 - Gradient descent 1D (fundamentos de otimizacao).

Setup (dado):
    L(theta) = (theta - 7)^2 ; gradiente = 2*(theta - 7) ;
    theta inicial = 0.0 ; eta = 0.1 ; 60 passos.

Tarefa:
    Imprima "theta inicial: <4c> perda inicial: <4c>".
    Rode 60 passos de theta <- theta - eta * gradiente(theta); nos passos
    1, 10, 30 e 60 imprima "passo <p:2d>: theta=<4c> perda=<4c>".
    Ao final imprima "theta final: <4c> perda final: <4c>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/102-entrevistas-fundamentos-ml/solucao_3.saida.txt
"""


def perda(theta):
    return (theta - 7.0) ** 2


def gradiente(theta):
    return 2.0 * (theta - 7.0)


# TODO: rode o gradient descent e imprima os marcos de convergencia.
