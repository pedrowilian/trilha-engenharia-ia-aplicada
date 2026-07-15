"""Licao 013 — Exercicio 2: diagnosticar a taxa de aprendizado.

Tarefa:
- Para L(theta) = (theta - 5)^2, o fator de contracao por passo e |1 - 2*eta|.
- Classifique cada eta em {0.05, 0.5, 1.0}:
    |1 - 2*eta| == 0 -> "passo unico"
    |1 - 2*eta| < 1  -> "converge"
    caso contrario   -> "nao converge"
- Imprima, na ordem dada, `<eta> -> <classificacao>`.

Criterio binario: saida IDENTICA a
trilha/solucoes/013-gradient-descent/solucao_2.saida.txt
"""


def classificar(eta):
    raise NotImplementedError


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
