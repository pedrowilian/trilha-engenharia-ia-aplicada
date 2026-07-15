"""Exercício 1 — Normas do zero e normalização.

Setup:
    w = [1.0, -2.0, 2.0]   # use apenas o módulo math

Tarefa:
    1. Calcule L1 = soma dos |x|, L2 = sqrt(soma dos x^2) e Linf = max |x|.
    2. Normalize w pela norma L2.
    3. Confirme que o vetor normalizado tem norma 1 e imprima, exatamente:
        L1=5.0000 L2=3.0000 Linf=2.0000
        normalizado: [0.3333, -0.6667, 0.6667]
        norma do normalizado: 1.0000
        OK

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/005-normas-produto-interno-distancias/solucao_1.saida.txt
"""
import math

w = [1.0, -2.0, 2.0]

# TODO: calcular L1, L2, Linf; normalizar pela L2; verificar norma 1 e imprimir.
