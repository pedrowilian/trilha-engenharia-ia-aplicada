"""Licao 020 — Exercicio 2: leakage de pre-processamento.

Tarefa:
- Use np.random.default_rng(3), dados = N(100, 20) com 25 amostras;
  treino = dados[:18], teste = dados[18:].
- Padronize o teste de DUAS formas: (errado) com media/desvio de TODOS os dados;
  (certo) com media/desvio so do treino.
- Imprima `media (errado, todos os dados): ...`, `media (certo, so treino): ...`,
  `teste[0] errado: ...`, `teste[0] certo: ...` (4 casas) e
  `houve vazamento nas estatisticas: <bool>`.

Criterio binario: saida IDENTICA a
trilha/solucoes/020-data-leakage/solucao_2.saida.txt
"""
import numpy as np


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
