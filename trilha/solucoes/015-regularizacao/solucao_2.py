"""Solucao de referencia — Licao 015, Exercicio 2.

Soft-thresholding (proximal do termo L1): zera coeficientes pequenos e
encolhe os demais em direcao a zero, produzindo um vetor esparso.
"""


def soft_threshold(w, limiar):
    saida = []
    for x in w:
        if x > limiar:
            saida.append(x - limiar)
        elif x < -limiar:
            saida.append(x + limiar)
        else:
            saida.append(0.0)
    return saida


def main():
    w = [1.2, -0.4, 0.9, -0.1, 2.5, 0.2]
    for limiar in [0.0, 0.5, 1.0]:
        s = soft_threshold(w, limiar)
        zeros = sum(1 for v in s if v == 0.0)
        print(f"limiar={limiar}: {[round(v, 2) for v in s]} (zeros={zeros})")
    z0 = sum(1 for v in soft_threshold(w, 0.0) if v == 0.0)
    z1 = sum(1 for v in soft_threshold(w, 1.0) if v == 0.0)
    print("esparsidade aumenta com o limiar:", z1 > z0)


if __name__ == "__main__":
    main()
