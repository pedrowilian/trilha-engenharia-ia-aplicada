"""Exercício 1 — Temperatura sobre a softmax.

Setup: os `logits` do próximo token e a lista de temperaturas `T`, abaixo.

Tarefa:
    Implemente uma softmax com temperatura (divide os logits por T, subtrai o
    máximo, exponencia e normaliza). Para cada T, imprima a distribuição (4 casas,
    entre colchetes) e o `max` (4 casas), no formato:
        T=0.5: [0.8420 0.1140 0.0419 0.0021]  max=0.8420

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/049-sampling-decodificacao/solucao_1.saida.txt
"""
import numpy as np

logits = np.array([2.0, 1.0, 0.5, -1.0])
temperaturas = [0.5, 1.0, 2.0]

# TODO: implementar a softmax com temperatura e imprimir cada distribuicao.
