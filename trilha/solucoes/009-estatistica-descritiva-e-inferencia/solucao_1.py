"""Solução de referência — Lição 009, Exercício 1.

Estatística descritiva: medidas de tendência central e de dispersão sobre uma
amostra, distinguindo variância populacional (divisor n) de amostral (n-1).
"""
import statistics as st


def main() -> None:
    dados = [2, 4, 4, 4, 5, 5, 7, 9]

    media = sum(dados) / len(dados)
    mediana = st.median(dados)
    var_populacional = st.pvariance(dados)   # divisor n
    var_amostral = st.variance(dados)         # divisor n-1
    desvio_amostral = st.stdev(dados)

    print(f"media               = {media:.4f}")
    print(f"mediana             = {mediana:.4f}")
    print(f"var (populacional)  = {var_populacional:.4f}")
    print(f"var (amostral)      = {var_amostral:.4f}")
    print(f"desvio (amostral)   = {desvio_amostral:.4f}")


if __name__ == "__main__":
    main()
