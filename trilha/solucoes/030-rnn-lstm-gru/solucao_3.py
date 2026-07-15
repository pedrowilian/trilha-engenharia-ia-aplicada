"""Solucao de referencia — Licao 030, Exercicio 3.

Portao de forget preserva a memoria: com o input fechado, c <- f*c a cada passo.
Um forget alto (0.95) retem a memoria por muitos passos; um baixo (0.5) a apaga.
"""


def main():
    for f in [0.5, 0.95]:
        c = 1.0
        for _ in range(10):
            c = f * c + 0.0       # input gate fechado
        print(f"forget={f}: c apos 10 passos = {c:.4f}")


if __name__ == "__main__":
    main()
