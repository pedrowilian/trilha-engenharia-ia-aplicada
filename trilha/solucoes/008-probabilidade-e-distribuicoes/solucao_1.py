"""Solução de referência — Lição 008, Exercício 1.

Probabilidade clássica (espaço equiprovável): soma de dois dados honestos.
Calcula P(soma == 7) contando casos favoráveis sobre o total.
"""


def main() -> None:
    # Espaço amostral: todos os pares ordenados (dado A, dado B).
    espaco = [(i, j) for i in range(1, 7) for j in range(1, 7)]
    total = len(espaco)

    # Evento de interesse: a soma das duas faces é exatamente 7.
    favoraveis = [(i, j) for (i, j) in espaco if i + j == 7]
    p = len(favoraveis) / total

    print(f"|Omega|              = {total}")
    print(f"favoraveis (soma=7)  = {len(favoraveis)}")
    print(f"P(soma=7)            = {p:.4f}")


if __name__ == "__main__":
    main()
