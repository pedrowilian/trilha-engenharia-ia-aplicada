"""Solução de referência — Exercício 2 da Lição 043.

Feed-forward de duas camadas com ReLU: expande d_model -> d_ff, zera as ativações
negativas e projeta de volta a d_model.
"""
import numpy as np

np.set_printoptions(precision=4, suppress=True)


def relu(x):
    return np.maximum(0.0, x)


rng = np.random.default_rng(101)
d_model, d_ff = 4, 16
X = rng.normal(0, 1, size=(3, d_model))
W1 = rng.normal(0, 1, size=(d_model, d_ff))
W2 = rng.normal(0, 1, size=(d_ff, d_model))

H = relu(X @ W1)
Y = H @ W2
print("fracao de ativacoes ocultas zeradas (ReLU):", round(float((H == 0).mean()), 4))
print("saida shape:", Y.shape)
print("Y[0] =", np.round(Y[0], 4))
