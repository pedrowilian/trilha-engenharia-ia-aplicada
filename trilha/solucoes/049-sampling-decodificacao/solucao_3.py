"""Solução de referência — Exercício 3 da Lição 049.

Filtragem top-p (nucleus) e amostragem determinística (semente fixa) do núcleo.
"""
import numpy as np


def softmax(logits):
    z = logits - logits.max()
    e = np.exp(z)
    return e / e.sum()


logits = np.array([3.0, 2.0, 1.0, 0.0, -1.0])
p = softmax(logits)

ordem = np.argsort(-p)
acum = np.cumsum(p[ordem])
corte = int(np.searchsorted(acum, 0.9)) + 1
manter = ordem[:corte]
p_top = np.zeros_like(p)
p_top[manter] = p[manter]
p_top = p_top / p_top.sum()

# Amostragem reprodutível a partir da distribuição truncada.
rng = np.random.default_rng(0)
amostras = rng.choice(len(p), size=1000, p=p_top)
contagens = np.bincount(amostras, minlength=len(p))

print(f"tokens no nucleo (p=0.9): {corte}")
print("p top-p   :", np.round(p_top, 4).tolist())
print("contagens :", contagens.tolist())
