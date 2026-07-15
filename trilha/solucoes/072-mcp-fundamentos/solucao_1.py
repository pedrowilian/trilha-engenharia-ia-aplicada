"""Solução de referência — Exercício 1 da Lição 072.

Economia de conectores: M aplicações x N fontes sob medida (M*N) contra um
protocolo padrão (M+N). Determinístico.
"""
M = 4
N = 6

sem_padrao = M * N
com_mcp = M + N

print("sem padrao:", sem_padrao)
print("com mcp:", com_mcp)
print("reducao:", sem_padrao - com_mcp)
