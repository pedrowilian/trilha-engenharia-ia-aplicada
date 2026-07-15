"""Solucao de referencia — Licao 031, Exercicio 1.

Conexoes residuais preservam o sinal em redes muito profundas. Empilhar 50
camadas "plain" encolhe o sinal; 50 blocos residuais com F desligado mantem a
entrada intacta (a identidade passa direto).
"""
import numpy as np


def main():
    rng = np.random.default_rng(5)
    x0 = rng.standard_normal(4)

    # rede "plain": 50 camadas y = tanh(0.5*y) -> o sinal encolhe
    y = x0.copy()
    for _ in range(50):
        y = np.tanh(0.5 * y)
    print(f"plain apos 50 camadas, norma: {np.linalg.norm(y):.4f}")

    # rede residual com F desligado: y = y + 0 -> identidade preservada
    y = x0.copy()
    for _ in range(50):
        y = y + 0.0
    print(f"residual (F=0) preserva a entrada: {np.allclose(y, x0)}")
    print(f"norma da entrada: {np.linalg.norm(x0):.4f}")


if __name__ == "__main__":
    main()
