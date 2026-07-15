"""Licao 031 — Exercicio 3: o valor das features pre-treinadas.

Tarefa:
- rng = np.random.default_rng(2), N = 200, y = (rng.uniform(N) < 0.5).
- features uteis = rng.standard_normal((N,8)) + y[:,None]*1.5 (carregam sinal).
- features aleatorias = rng.standard_normal((N,8)) (sem sinal).
- Treine a MESMA cabeca logistica (w=zeros(8), b=0, eta=0.1, 300 passos) sobre
  cada conjunto e reporte a acuracia.
- Imprima a acuracia com features uteis e com features aleatorias (4 casas).

Criterio binario: saida IDENTICA a
trilha/solucoes/031-arquiteturas-profundas-transfer-learning/solucao_3.saida.txt
"""
import numpy as np


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
