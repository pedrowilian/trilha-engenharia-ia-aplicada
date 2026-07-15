"""Exercício 2 — Contagem de parâmetros do LoRA.

Setup: uma camada com d=k=4096 e postos r em [4, 8, 16, 64].

Tarefa:
    Implemente `economia(d, k, r)` que devolve (completo=d*k, lora=r*(d+k),
    pct=100*lora/completo). Para cada r, imprima
    `r={r:>3}: lora={lora:>8} de {completo:>9} ({pct:5.2f}%)`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/078-lora-peft/solucao_2.saida.txt
"""
d = k = 4096
postos = [4, 8, 16, 64]

# TODO: implementar economia(...) e imprimir uma linha por posto.
