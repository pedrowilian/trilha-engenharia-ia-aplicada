"""Solução de referência — Exercício 3 da Lição 065.

Critério de aceitação: encerra quando a nota atinge o limiar OU quando o número
máximo de revisões é atingido. Determinístico.
"""


def avaliar(versao):
    return 3 + 3 * versao


limiar = 9
max_revisoes = 5
versao = 0
while True:
    nota = avaliar(versao)
    print(f"versao {versao}: nota={nota}")
    if nota >= limiar:
        print("aceito por qualidade")
        break
    if versao >= max_revisoes:
        print("parou no limite de revisoes")
        break
    versao += 1
