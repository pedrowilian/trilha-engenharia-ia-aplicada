"""Solucao de referencia — Licao 028, Exercicio 3.

Correcao de bias do Adam: como m e v comecam em zero, os primeiros passos sao
subestimados. Os fatores 1/(1-b1^t) e 1/(1-b2^t) corrigem isso e tendem a 1.
"""


def main():
    b1, b2 = 0.9, 0.999
    for t in range(1, 4):
        c1 = 1.0 / (1.0 - b1 ** t)
        c2 = 1.0 / (1.0 - b2 ** t)
        print(f"t={t}: correcao 1o momento={c1:.4f}  correcao 2o momento={c2:.4f}")


if __name__ == "__main__":
    main()
