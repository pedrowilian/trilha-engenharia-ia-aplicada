"""Solucao de referencia — Licao 017, Exercicio 1.

Diagnostico de underfitting / overfitting / bom ajuste a partir dos erros de
treino e validacao.
"""


def diagnosticar(erro_treino, erro_val, limiar_alto=0.20, folga_max=0.10):
    if erro_treino > limiar_alto and erro_val > limiar_alto:
        return "underfitting"
    if erro_val - erro_treino > folga_max:
        return "overfitting"
    return "bom ajuste"


def main():
    casos = [
        ("A", 0.40, 0.42),
        ("B", 0.03, 0.25),
        ("C", 0.07, 0.10),
        ("D", 0.30, 0.31),
    ]
    for nome, tr, val in casos:
        print(f"{nome}: treino={tr:.2f} val={val:.2f} -> {diagnosticar(tr, val)}")


if __name__ == "__main__":
    main()
