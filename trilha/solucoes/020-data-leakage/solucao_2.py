"""Solucao de referencia — Licao 020, Exercicio 2.

Leakage de pre-processamento: padronizar usando estatisticas de TODOS os dados
(treino + teste) vaza informacao. O correto e ajustar o scaler so no treino.
"""
import numpy as np


def main():
    rng = np.random.default_rng(3)
    dados = rng.normal(100, 20, size=25)
    treino, teste = dados[:18], dados[18:]

    mu_todos, sd_todos = dados.mean(), dados.std()
    mu_tr, sd_tr = treino.mean(), treino.std()

    teste_errado = (teste - mu_todos) / sd_todos
    teste_certo = (teste - mu_tr) / sd_tr

    print(f"media (errado, todos os dados): {mu_todos:.4f}")
    print(f"media (certo, so treino):       {mu_tr:.4f}")
    print(f"teste[0] errado: {teste_errado[0]:.4f}")
    print(f"teste[0] certo:  {teste_certo[0]:.4f}")
    print("houve vazamento nas estatisticas:", abs(mu_todos - mu_tr) > 1e-9)


if __name__ == "__main__":
    main()
