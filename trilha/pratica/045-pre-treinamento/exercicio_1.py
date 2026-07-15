"""Exercício 1 — Perda de pré-treino sobre um corpus.

Setup: matriz P (3x3) e corpus = "cabbac".

Tarefa:
    Acumule a NLL dos pares (anterior -> próximo) do corpus, calcule a
    cross-entropy média e a perplexidade. Imprima `pares de treino`,
    `cross-entropy media` (4 casas) e `perplexidade` (4 casas).

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/045-pre-treinamento/solucao_1.saida.txt
"""
import numpy as np

vocab = ["a", "b", "c"]
idx = {t: i for i, t in enumerate(vocab)}
P = np.array([
    [0.1, 0.7, 0.2],   # depois de "a"
    [0.2, 0.2, 0.6],   # depois de "b"
    [0.5, 0.3, 0.2],   # depois de "c"
])
corpus = "cabbac"

# TODO: acumular NLL, calcular cross-entropy media e perplexidade; imprimir.
