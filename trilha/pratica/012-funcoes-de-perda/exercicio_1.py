"""Licao 012 — Exercicio 1: MSE e MAE do zero.

Tarefa:
- Implemente `mse(y_real, y_pred)` e `mae(y_real, y_pred)` (Python puro).
- Compare duas predicoes: `pred_a` (erros pequenos espalhados) e `pred_b`
  (um unico outlier grande) sobre `y_real`.
- Imprima, por linha, `pred_a: MSE=... MAE=...` e `pred_b: MSE=... MAE=...`
  (4 casas) e, por fim, `MSE pune mais o outlier: <bool>`.

Criterio binario: saida IDENTICA a
trilha/solucoes/012-funcoes-de-perda/solucao_1.saida.txt
"""

y_real = [10.0, 12.0, 14.0, 16.0, 18.0]
pred_a = [11.0, 11.0, 15.0, 15.0, 19.0]
pred_b = [10.0, 12.0, 14.0, 16.0, 28.0]


def mse(y_real, y_pred):
    raise NotImplementedError


def mae(y_real, y_pred):
    raise NotImplementedError


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
