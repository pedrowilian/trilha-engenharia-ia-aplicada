"""Solucao de referencia - Exercicio 3 da Licao 104.

Softmax numericamente estavel (subtrai o maximo antes de exp), classe prevista
(argmax) e similaridade de cosseno. Sao as primitivas numericas que aparecem em
live coding de ML - a banca avalia se voce evita overflow no exp e normaliza
corretamente.
"""
import numpy as np


def softmax(x):
    x = np.asarray(x, dtype=float)
    z = x - np.max(x)
    e = np.exp(z)
    return e / e.sum()


def cosseno(a, b):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))


logits = [1.0, 3.0, 0.0, 2.0]
p = softmax(logits)
print("softmax:", [f"{v:.4f}" for v in p])
print(f"classe prevista (argmax): {int(np.argmax(p))}")
print(f"cosseno: {cosseno([2, 1, 0], [1, 2, 0]):.4f}")
