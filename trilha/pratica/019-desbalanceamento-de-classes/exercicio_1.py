"""Licao 019 — Exercicio 1: paradoxo da acuracia.

Tarefa:
- y = 950 negativos + 50 positivos; classificador trivial preve sempre 0.
- Calcule acuracia, recall positivo, recall negativo e acuracia balanceada
  (media dos dois recalls).
- Imprima `acuracia`, `recall positivo`, `recall negativo`,
  `acuracia balanceada` (4 casas) e `acuracia engana: <bool>`
  (acc > 0.9 e acc_balanceada <= 0.5).

Criterio binario: saida IDENTICA a
trilha/solucoes/019-desbalanceamento-de-classes/solucao_1.saida.txt
"""


def main():
    y = [0] * 950 + [1] * 50
    pred = [0] * 1000
    raise NotImplementedError


if __name__ == "__main__":
    main()
