"""Solucao de referencia — Licao 028, Exercicio 1.

Acumulo de velocidade no momentum: com gradiente constante g=1 e beta=0.9, a
velocidade cresce como uma media movel exponencial rumo ao limite 1/(1-beta).
"""


def main():
    beta = 0.9
    g = 1.0
    v = 0.0
    for t in range(1, 6):
        v = beta * v + g
        print(f"passo {t}: v={v:.4f}")
    print(f"limite teorico 1/(1-beta) = {1.0 / (1.0 - beta):.4f}")


if __name__ == "__main__":
    main()
