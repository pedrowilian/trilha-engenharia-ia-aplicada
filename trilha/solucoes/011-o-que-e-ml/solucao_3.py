"""Solucao de referencia — Licao 011, Exercicio 3.

Aprendizado por reforco: bandit de 4 bracos com epsilon-greedy e semente fixa.
O agente deve convergir para escolher o braco de maior probabilidade real.
"""
import random


def main():
    random.seed(7)
    probabilidades_reais = [0.1, 0.3, 0.6, 0.9]   # braco 3 e o melhor
    n = len(probabilidades_reais)
    Q = [0.0] * n
    contagem = [0] * n
    epsilon = 0.1

    def puxar(braco):
        return 1.0 if random.random() < probabilidades_reais[braco] else 0.0

    for _ in range(3000):
        if random.random() < epsilon:
            a = random.randrange(n)
        else:
            a = max(range(n), key=lambda i: Q[i])
        r = puxar(a)
        contagem[a] += 1
        Q[a] += (r - Q[a]) / contagem[a]

    melhor = max(range(n), key=lambda i: Q[i])
    print("Q estimado:", [round(q, 3) for q in Q])
    print("braco escolhido:", melhor)
    print("correto:", melhor == 3)


if __name__ == "__main__":
    main()
