"""Licao 025 — Exercicio 3: He mantem a variancia saudavel sob ReLU.

Tarefa:
- Use rng = np.random.default_rng(3), n = 256, a = rng.standard_normal(n).
- Por 5 camadas, faca W = rng.standard_normal((n,n))*sqrt(2/n) e
  a = relu(W @ a); guarde a.std() de cada camada.
- Verifique se todas as camadas tem 0.3 < std < 1.0 e imprima os std (4 casas)
  e o booleano.

Criterio binario: saida IDENTICA a
trilha/solucoes/025-treino-redes-profundas-inicializacao/solucao_3.saida.txt
"""
import numpy as np


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
