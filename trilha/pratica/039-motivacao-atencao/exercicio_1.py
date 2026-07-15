"""Exercício 1 — Quantificar o decaimento de memória de uma RNN.

Setup:
    Recorrência linear h_t = a*h_{t-1} + x_t, com a = 0.8 e T = 12.

Tarefa:
    A influência de x_0 sobre h_t é a**t. Imprima-a em t = 0, 4, 8, 12 com 6
    casas decimais e reporte o PRIMEIRO t em que a influência cai abaixo de 0.1.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/039-motivacao-atencao/solucao_1.saida.txt
"""
import numpy as np

a = 0.8
T = 12

# TODO: calcular a influência a**t, imprimir em t = 0, 4, 8, 12 e achar o
#       primeiro t com influência < 0.1.
