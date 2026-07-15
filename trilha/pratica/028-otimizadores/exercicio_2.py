"""Licao 028 — Exercicio 2: RMSProp normaliza o tamanho do passo.

Tarefa:
- Use eta=0.01, beta=0.9, eps=1e-8 e g = [100.0, 0.01].
- Calcule o primeiro passo de RMSProp: s = (1-beta)*g*g; passo = eta*g/(sqrt(s)+eps).
- Imprima o gradiente, o passo efetivo (6 casas) e se os dois passos sao quase
  iguais (np.isclose, atol=1e-4).

Criterio binario: saida IDENTICA a
trilha/solucoes/028-otimizadores/solucao_2.saida.txt
"""
import numpy as np


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
