"""Exercício 3 — Invariância do cosseno à escala.

Setup:
    ref = [1.0, 2.0]
    x   = [2.0, 1.0]
    5x  = [10.0, 5.0]   # x multiplicado por 5

Tarefa:
    1. Implemente dot, cos_sim e l2.
    2. Calcule cos(ref, x), cos(ref, 5x), dot e L2 para os dois.
    3. Verifique que o cosseno NÃO muda com a escala e imprima, exatamente:
        cos(ref, x)  = 0.8000
        cos(ref, 5x) = 0.8000
        dot(ref, x)  = 4.0000
        dot(ref, 5x) = 20.0000
        L2(ref, x)   = 1.4142
        L2(ref, 5x)  = 9.4868
        cosseno invariante a escala

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/005-normas-produto-interno-distancias/solucao_3.saida.txt
"""
import math

ref = [1.0, 2.0]
x = [2.0, 1.0]
x5 = [5.0 * c for c in x]

# TODO: implementar dot, cos_sim e l2; calcular e imprimir conforme o formato.
