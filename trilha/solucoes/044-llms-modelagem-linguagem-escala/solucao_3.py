"""Solução de referência — Exercício 3 da Lição 044.

Inverte a lei de escala L(N) = E + A * N^(-alpha) para achar o N necessário
para atingir uma perda-alvo.
"""
E, A, alpha = 1.6, 2100.0, 0.34
L_alvo = 2.0

# L = E + A * N^(-alpha)  =>  N = (A / (L - E))^(1/alpha)
N = (A / (L_alvo - E)) ** (1.0 / alpha)
perda_recomputada = E + A * N ** (-alpha)

print(f"N necessario      = {N:.3e}")
print(f"perda recomputada = {perda_recomputada:.4f}")
