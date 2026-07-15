"""Exercicio 3 - Softmax estavel, argmax e cosseno.

Setup (dado):
    logits = [1.0, 3.0, 0.0, 2.0]
    vetores para o cosseno: a = [2, 1, 0], b = [1, 2, 0].

Tarefa:
    Implemente softmax(x) subtraindo o maximo antes de exp (estabilidade) e
    normalizando pela soma; implemente cosseno(a, b) = (a.b)/(||a||*||b||).
    Imprima "softmax: <lista com 4 casas>", "classe prevista (argmax): <int>" e
    "cosseno: <4 casas>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/104-exercicios-entrevista-python/solucao_3.saida.txt
"""
import numpy as np

logits = [1.0, 3.0, 0.0, 2.0]

# TODO: implemente softmax(x) e cosseno(a, b) e imprima softmax, argmax e cosseno.
