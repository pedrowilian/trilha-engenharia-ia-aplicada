"""Solução de referência — Exercício 2 da Lição 039.

Comprimento do caminho de informação entre posições: a RNN percorre passo a
passo (|i-j|); a atenção liga qualquer par diretamente (1).
"""
n = 10


def caminho_rnn(i, j):
    return abs(i - j)


def caminho_atencao(i, j):
    return 1


for i, j in [(0, 9), (1, 8), (4, 6)]:
    print(f"({i},{j}) rnn={caminho_rnn(i, j)} atencao={caminho_atencao(i, j)}")

print("maior caminho rnn:", max(caminho_rnn(0, k) for k in range(n)))
print("maior caminho atencao:", 1)
