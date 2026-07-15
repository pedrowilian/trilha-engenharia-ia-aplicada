"""Licao 015 — Exercicio 2: soft-thresholding (L1) e esparsidade.

Tarefa:
- Implemente `soft_threshold(w, limiar)`: subtrai o limiar de coeficientes
  positivos, soma em negativos, e zera os de modulo <= limiar.
- Para `w` dado, imprima, para limiar em [0.0, 0.5, 1.0]:
  `limiar=...: [...] (zeros=n)` (valores com 2 casas via round).
- Ao final, imprima `esparsidade aumenta com o limiar: <bool>`.

Criterio binario: saida IDENTICA a
trilha/solucoes/015-regularizacao/solucao_2.saida.txt
"""

w = [1.2, -0.4, 0.9, -0.1, 2.5, 0.2]


def soft_threshold(w, limiar):
    raise NotImplementedError


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
