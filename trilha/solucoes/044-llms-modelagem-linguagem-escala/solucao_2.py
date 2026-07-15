"""Solução de referência — Exercício 2 da Lição 044.

Cross-entropy média por token e perplexidade de um modelo de linguagem.
"""
import numpy as np

distribuicoes = np.array([
    [0.05, 0.05, 0.10, 0.20, 0.60],
    [0.10, 0.20, 0.40, 0.20, 0.10],
    [0.50, 0.20, 0.15, 0.10, 0.05],
])
alvos = [4, 2, 0]

p_corretos = distribuicoes[np.arange(len(alvos)), alvos]
nll = -np.log(p_corretos)
ce = nll.mean()
ppl = np.exp(ce)

for t, (p, l) in enumerate(zip(p_corretos, nll)):
    print(f"passo {t}: p_correto={p:.2f}  -log p={l:.4f}")
print(f"cross-entropy (nats) = {ce:.4f}")
print(f"perplexidade         = {ppl:.4f}")
