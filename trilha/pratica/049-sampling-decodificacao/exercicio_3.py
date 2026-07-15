"""Exercício 3 — Top-p (nucleus) e amostragem reprodutível.

Setup: os `logits` do próximo token, o alvo de massa `p_alvo = 0.9` e a semente
`np.random.default_rng(0)`, amostrando 1000 tokens.

Tarefa:
    Ordene as probabilidades por valor decrescente, ache o menor núcleo cuja massa
    acumulada >= 0.9, zere a cauda e renormalize. Amostre 1000 tokens da
    distribuição truncada (use rng.choice) e conte as ocorrências por token com
    np.bincount(..., minlength=len(p)). Imprima `tokens no nucleo (p=0.9)`,
    `p top-p` (lista, 4 casas) e `contagens` (lista).

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/049-sampling-decodificacao/solucao_3.saida.txt
"""
import numpy as np

logits = np.array([3.0, 2.0, 1.0, 0.0, -1.0])
p_alvo = 0.9

# TODO: aplicar top-p, renormalizar, amostrar com semente fixa e imprimir.
