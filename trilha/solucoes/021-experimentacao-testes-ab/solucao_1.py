"""Solucao de referencia — Licao 021, Exercicio 1.

Desenho de um teste A/B: simula controle e tratamento randomizados e calcula
as taxas de conversao e o lift.
"""
import numpy as np


def main():
    rng = np.random.default_rng(7)
    n = 8000
    p_controle, p_tratamento = 0.20, 0.23
    conv_c = (rng.uniform(0, 1, size=n) < p_controle).astype(int)
    conv_t = (rng.uniform(0, 1, size=n) < p_tratamento).astype(int)
    taxa_c, taxa_t = conv_c.mean(), conv_t.mean()
    print(f"conversao controle:   {taxa_c:.4f}")
    print(f"conversao tratamento: {taxa_t:.4f}")
    print(f"lift absoluto: {taxa_t - taxa_c:.4f}")
    print(f"lift relativo: {(taxa_t - taxa_c) / taxa_c:.4f}")
    print("tratamento parece melhor:", taxa_t > taxa_c)


if __name__ == "__main__":
    main()
