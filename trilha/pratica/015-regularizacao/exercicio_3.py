"""Licao 015 — Exercicio 3: early stopping com paciencia.

Tarefa:
- Implemente `early_stopping(perda_val, paciencia)` que percorre as epocas,
  guarda o melhor epoch (menor val), e para quando a val nao melhora por
  `paciencia` epocas seguidas. Retorne (melhor_epoch, melhor_val, parou_em).
- Use `perda_val` dado e `paciencia=3`. Imprima `melhor epoch: <e> (val=...)`,
  `parou no epoch: <p>` e `epochs economizados: <n>`.

Criterio binario: saida IDENTICA a
trilha/solucoes/015-regularizacao/solucao_3.saida.txt
"""

perda_val = [0.90, 0.70, 0.55, 0.48, 0.45, 0.44, 0.47, 0.50, 0.55, 0.60]


def early_stopping(perda_val, paciencia):
    raise NotImplementedError


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
