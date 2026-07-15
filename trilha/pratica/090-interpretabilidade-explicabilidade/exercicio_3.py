"""Exercício 3 — Explicação global vs local.

Setup (use exatamente estas sementes/parâmetros para reproduzir a saída):
    rng = np.random.default_rng(3)
    w = np.array([1.0, -2.0, 0.5])
    X = rng.uniform(0.0, 1.0, size=(400, 3))

Tarefa:
    Calcule a atribuição local `attrib = X * w`, a importância global
    `np.mean(np.abs(attrib), axis=0)` e a explicação da instância 0 (`attrib[0]`).
    Para cada feature em ["f0", "f1", "f2"] imprima
    `"{nome}: global={g:.3f} local[0]={l:+.3f}"` e, ao final,
    `"feature mais importante (global): {nome do maior global}"`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/090-interpretabilidade-explicabilidade/solucao_3.saida.txt
"""
import numpy as np

# TODO: calcule atribuição local, importância global e a feature dominante.
