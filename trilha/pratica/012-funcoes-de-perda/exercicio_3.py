"""Licao 012 — Exercicio 3: softmax + cross-entropy multiclasse.

Tarefa:
- Implemente `softmax(z)` (com subtracao do maximo para estabilidade) e
  `cross_entropy(logits, classe_certa)` = -log(softmax(logits)[classe_certa]).
- Compare `logits_confiante` e `logits_indeciso` para a classe certa de indice 0.
- Imprima `cross-entropy (confiante): ...`, `cross-entropy (indeciso): ...`
  (4 casas) e `menor perda = mais confianca na classe certa: <bool>`.

Criterio binario: saida IDENTICA a
trilha/solucoes/012-funcoes-de-perda/solucao_3.saida.txt
"""
import math

logits_confiante = [4.0, 1.0, 0.0]
logits_indeciso = [1.0, 0.9, 0.8]


def softmax(z):
    raise NotImplementedError


def cross_entropy(logits, classe_certa):
    raise NotImplementedError


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
