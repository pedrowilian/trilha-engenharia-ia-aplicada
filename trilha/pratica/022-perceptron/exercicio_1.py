"""Licao 022 — Exercicio 1: treinar um perceptron para a porta OR.

Tarefa:
- Use X = [[0,0],[0,1],[1,0],[1,1]] e y = [0,1,1,1] (porta OR).
- Inicialize w = zeros(2), b = 0.0, eta = 1.0.
- Aplique a regra de aprendizado do perceptron por ate 20 epocas; pare quando
  uma epoca inteira passar sem erros e registre a epoca de convergencia.
- Imprima a epoca de convergencia, w, b, as predicoes, o alvo e se todos
  os exemplos foram classificados corretamente.

Criterio binario: saida IDENTICA a
trilha/solucoes/022-perceptron/solucao_1.saida.txt
"""
import numpy as np


def degrau(z):
    return 1 if z >= 0.0 else 0


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
