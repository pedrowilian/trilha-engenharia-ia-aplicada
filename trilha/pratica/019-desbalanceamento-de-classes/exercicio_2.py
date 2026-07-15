"""Licao 019 — Exercicio 2: precision, recall e F1.

Tarefa:
- Implemente `metricas(y_real, y_pred)` que devolve VP, FP, FN, VN, precision,
  recall e F1 (classe positiva = 1).
- Use os vetores dados e imprima `VP=.. FP=.. FN=.. VN=..`, `precision:`,
  `recall:` e `F1:` (4 casas).

Criterio binario: saida IDENTICA a
trilha/solucoes/019-desbalanceamento-de-classes/solucao_2.saida.txt
"""

y_real = [1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0]
y_pred = [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0]


def metricas(y_real, y_pred):
    raise NotImplementedError


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
