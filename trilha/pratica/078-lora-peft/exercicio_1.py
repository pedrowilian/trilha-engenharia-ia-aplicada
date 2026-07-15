"""Exercício 1 — Atualização de baixo posto ΔW = B·A.

Setup: use numpy com `rng = np.random.default_rng(7)` e d=8, k=5, r=3.

Tarefa:
    Sorteie B (d×r) e A (r×k), forme delta = B@A, sorteie W0 (d×k) e W = W0 +
    delta (na ordem indicada, para a semente bater). Imprima o shape de delta,
    o posto de delta, o posto de W0, e o número de parâmetros de (B,A) e de W0.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/078-lora-peft/solucao_1.saida.txt
"""
import numpy as np

rng = np.random.default_rng(7)
d, k, r = 8, 5, 3

# TODO: sortear B, A (delta=B@A), depois W0; imprimir shapes, postos e tamanhos.
