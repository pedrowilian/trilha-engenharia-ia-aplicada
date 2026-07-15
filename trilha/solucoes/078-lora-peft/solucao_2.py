"""Solução de referência — Exercício 2 da Lição 078.

Conta os parâmetros treináveis do LoRA, r·(d+k), versus a matriz cheia, d·k,
para uma camada de atenção d=k=4096 e vários postos r.
"""


def economia(d, k, r):
    completo = d * k
    lora = r * (d + k)
    return completo, lora, 100.0 * lora / completo


d = k = 4096
for r in [4, 8, 16, 64]:
    completo, lora, pct = economia(d, k, r)
    print(f"r={r:>3}: lora={lora:>8} de {completo:>9} ({pct:5.2f}%)")
