"""Solução de referência — Exercício 3 da Lição 039.

Profundidade sequencial: a RNN executa T passos em série; a atenção, 1 passo
paralelizável. A razão T // 1 mede a redução na profundidade sequencial.
"""
for T in [8, 32, 128]:
    rnn = T
    att = 1
    print(f"T={T:>3}: rnn={rnn:>3} passos | atencao={att} passo | reducao={rnn // att}x")
