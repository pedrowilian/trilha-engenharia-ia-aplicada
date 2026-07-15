"""Solucao de referencia — Licao 030, Exercicio 2.

Portao de atualizacao da GRU: h = (1-z)*h_prev + z*h_cand. Com z=0 mantem a
memoria antiga; com z=1 substitui pelo candidato; z intermediario interpola.
"""


def gru_update(z, h_prev, h_cand):
    return (1.0 - z) * h_prev + z * h_cand


def main():
    h_prev, h_cand = 1.0, 0.0
    for z in [0.0, 0.25, 0.5, 1.0]:
        h = gru_update(z, h_prev, h_cand)
        print(f"z={z:.2f}: h={h:.4f}")


if __name__ == "__main__":
    main()
