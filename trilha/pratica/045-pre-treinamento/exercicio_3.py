"""Exercício 3 — Tokens compute-ótimos e FLOPs.

Setup: N parâmetros e a razão alvo tokens_por_param.

Tarefa:
    Calcule D = N * tokens_por_param, o compute C = 6 * N * D e imprima
    `D (tokens)` ({:.3e}), `C = 6*N*D` ({:.3e} seguido de " FLOPs") e a razão
    `tokens/param` (1 casa).

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/045-pre-treinamento/solucao_3.saida.txt
"""
N = 1_300_000_000
tokens_por_param = 20

# TODO: calcular D, C e imprimir os resultados.
