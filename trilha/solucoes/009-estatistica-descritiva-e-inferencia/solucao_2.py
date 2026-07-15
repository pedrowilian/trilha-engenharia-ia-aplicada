"""Solução de referência — Lição 009, Exercício 2.

Inferência: erro padrão da média e intervalo de confiança de 95% (aproximação
normal, z = 1.96) a partir da média amostral, do desvio padrão e do tamanho n.
"""
from math import sqrt


def main() -> None:
    media_amostral = 2.5
    desvio_padrao = 1.2
    n = 64

    erro_padrao = desvio_padrao / sqrt(n)
    z = 1.96
    ic_inf = media_amostral - z * erro_padrao
    ic_sup = media_amostral + z * erro_padrao

    print(f"erro padrao = {erro_padrao:.4f}")
    print(f"IC 95% = [{ic_inf:.4f}, {ic_sup:.4f}]")


if __name__ == "__main__":
    main()
