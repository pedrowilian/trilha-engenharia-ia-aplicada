"""Licao 027 — Exercicio 2: sigmoid some, ReLU preserva.

Tarefa:
- Propague um gradiente (inicial 1.0) por 10 camadas:
  - sigmoid: comece com a=0.5; a cada camada s=sigmoid(a); grad *= s*(1-s); a=s.
  - ReLU ativa: a cada camada grad *= 1.0.
- Imprima o grad final de cada (formato .3e), e os booleanos
  `sigmoid desapareceu (< 1e-3)` e `ReLU preservou (~1)`.

Criterio binario: saida IDENTICA a
trilha/solucoes/027-vanishing-exploding-gradients/solucao_2.saida.txt
"""
import numpy as np


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
