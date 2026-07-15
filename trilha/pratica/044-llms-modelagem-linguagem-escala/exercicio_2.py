"""Exercício 2 — Cross-entropy e perplexidade de um modelo.

Setup: matriz distribuicoes (3x5) com as previsões do modelo e os alvos.

Tarefa:
    Extraia a probabilidade do token correto em cada passo, calcule a NLL por
    token, a cross-entropy média (nats) e a perplexidade. Imprima cada passo
    (2 casas em p_correto, 4 em -log p), a cross-entropy (4 casas) e a
    perplexidade (4 casas).

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/044-llms-modelagem-linguagem-escala/solucao_2.saida.txt
"""
import numpy as np

distribuicoes = np.array([
    [0.05, 0.05, 0.10, 0.20, 0.60],
    [0.10, 0.20, 0.40, 0.20, 0.10],
    [0.50, 0.20, 0.15, 0.10, 0.05],
])
alvos = [4, 2, 0]

# TODO: calcular p_corretos, nll, cross-entropy e perplexidade; imprimir.
