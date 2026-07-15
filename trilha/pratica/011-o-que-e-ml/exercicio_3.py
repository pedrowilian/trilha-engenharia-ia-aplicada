"""Licao 011 — Exercicio 3: bandit epsilon-greedy (aprendizado por reforco).

Tarefa:
- Use `random.seed(7)`. Ha 4 bracos com probabilidades reais [0.1, 0.3, 0.6, 0.9].
- Por 3000 passos, com epsilon=0.1: explore (braco aleatorio) com prob. epsilon,
  senao explote (braco de maior Q). Atualize Q pela media incremental
  Q[a] += (r - Q[a]) / contagem[a].
- Imprima `Q estimado: [...]` (3 casas), `braco escolhido: <i>` e `correto: <bool>`
  (correto sse o braco escolhido for o de indice 3).

Criterio binario: saida IDENTICA a
trilha/solucoes/011-o-que-e-ml/solucao_3.saida.txt
"""
import random


def main():
    random.seed(7)
    raise NotImplementedError("implemente o bandit epsilon-greedy")


if __name__ == "__main__":
    main()
