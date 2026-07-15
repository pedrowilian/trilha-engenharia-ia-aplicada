"""Solução de referência — Exercício 1 da Lição 044.

Probabilidade de uma sequência pela regra da cadeia da probabilidade, usando
uma matriz de transição (modelo de linguagem de 1ª ordem).
"""
import numpy as np

vocab = ["<s>", "o", "gato", "foge", "dorme", "</s>"]
idx = {t: i for i, t in enumerate(vocab)}

# Linha i = P(proximo | token i); cada linha soma 1.
P = np.array([
    [0.0, 0.7, 0.2, 0.0, 0.1, 0.0],   # depois de <s>
    [0.0, 0.0, 0.8, 0.0, 0.1, 0.1],   # depois de "o"
    [0.0, 0.1, 0.0, 0.3, 0.5, 0.1],   # depois de "gato"
    [0.0, 0.1, 0.0, 0.0, 0.0, 0.9],   # depois de "foge"
    [0.0, 0.1, 0.0, 0.0, 0.0, 0.9],   # depois de "dorme"
    [0.0, 0.0, 0.0, 0.0, 0.0, 1.0],   # depois de </s>
])

sequencia = ["<s>", "o", "gato", "foge", "</s>"]

log_prob = 0.0
for ant, prox in zip(sequencia[:-1], sequencia[1:]):
    p = P[idx[ant], idx[prox]]
    log_prob += np.log(p)
    print(f"P({prox:>5} | {ant:>5}) = {p:.3f}")

prob = np.exp(log_prob)
print(f"log P(sequencia) = {log_prob:.4f}")
print(f"P(sequencia)     = {prob:.4f}")
