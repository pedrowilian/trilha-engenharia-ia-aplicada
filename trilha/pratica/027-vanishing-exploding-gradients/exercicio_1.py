"""Licao 027 — Exercicio 1: destino do gradiente em rede profunda.

Tarefa:
- Para L = 30 camadas e fator em [0.5, 1.0, 1.5], calcule grad = fator**L.
- Classifique: grad < 1e-3 -> "vanishing"; grad > 1e3 -> "exploding";
  caso contrario -> "estavel".
- Imprima por linha `fator=...: grad=... -> classe`.

Criterio binario: saida IDENTICA a
trilha/solucoes/027-vanishing-exploding-gradients/solucao_1.saida.txt
"""


def classificar(grad):
    raise NotImplementedError


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
