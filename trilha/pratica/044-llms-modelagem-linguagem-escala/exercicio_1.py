"""Exercício 1 — Probabilidade de uma sequência pela regra da cadeia.

Setup: matriz de transição P (6x6) sobre o vocabulário abaixo. A sequência a
avaliar é ["<s>", "o", "gato", "foge", "</s>"].

Tarefa:
    Acumule o log-prob pela regra da cadeia P(seq) = prod P(token_t | token_{t-1}),
    imprimindo cada fator condicional, o log P(sequencia) (4 casas) e o
    P(sequencia) (4 casas).

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/044-llms-modelagem-linguagem-escala/solucao_1.saida.txt
"""
import numpy as np

vocab = ["<s>", "o", "gato", "foge", "dorme", "</s>"]
idx = {t: i for i, t in enumerate(vocab)}

P = np.array([
    [0.0, 0.7, 0.2, 0.0, 0.1, 0.0],   # depois de <s>
    [0.0, 0.0, 0.8, 0.0, 0.1, 0.1],   # depois de "o"
    [0.0, 0.1, 0.0, 0.3, 0.5, 0.1],   # depois de "gato"
    [0.0, 0.1, 0.0, 0.0, 0.0, 0.9],   # depois de "foge"
    [0.0, 0.1, 0.0, 0.0, 0.0, 0.9],   # depois de "dorme"
    [0.0, 0.0, 0.0, 0.0, 0.0, 1.0],   # depois de </s>
])

sequencia = ["<s>", "o", "gato", "foge", "</s>"]

# TODO: acumular o log-prob pela regra da cadeia e imprimir os resultados.
