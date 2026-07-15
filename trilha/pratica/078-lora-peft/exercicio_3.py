"""Exercício 3 — Fator de escala alpha/r na saída adaptada.

Setup: numpy com `rng = np.random.default_rng(3)`, d=5, k=4, r=2 e x = vetor de
uns. Sorteie W0 (d×k), B (d×r), A (r×k) nessa ordem.

Tarefa:
    Imprima a norma da saída base `x @ W0`. Depois, para alpha em [2, 4, 16],
    calcule a escala alpha/r e a saída `x @ (W0 + escala*(B@A))`, imprimindo
    `alpha={alpha:>2}: escala={escala:.1f} ||y||={norma:.4f}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/078-lora-peft/solucao_3.saida.txt
"""
import numpy as np

rng = np.random.default_rng(3)
d, k, r = 5, 4, 2

# TODO: sortear W0, B, A; imprimir a norma base e a de cada alpha.
