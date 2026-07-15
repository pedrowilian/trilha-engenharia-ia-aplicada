"""Solução de referência — Exercício 3 da Lição 045.

Tokens compute-ótimos (regra ~20 tokens/parâmetro) e FLOPs de pré-treino.
"""
N = 1_300_000_000          # parametros
tokens_por_param = 20

D = N * tokens_por_param
C = 6 * N * D

print(f"D (tokens)     = {D:.3e}")
print(f"C = 6*N*D      = {C:.3e} FLOPs")
print(f"tokens/param   = {D / N:.1f}")
