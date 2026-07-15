"""Solucao de referencia — Licao 015, Exercicio 3.

Early stopping com paciencia: para o treino quando a perda de validacao deixa
de melhorar por `paciencia` epocas seguidas, devolvendo o melhor epoch.
"""


def early_stopping(perda_val, paciencia):
    melhor_epoch = 0
    melhor_val = perda_val[0]
    contador = 0
    parou_em = len(perda_val) - 1
    for epoch in range(1, len(perda_val)):
        if perda_val[epoch] < melhor_val:
            melhor_val = perda_val[epoch]
            melhor_epoch = epoch
            contador = 0
        else:
            contador += 1
            if contador >= paciencia:
                parou_em = epoch
                break
    return melhor_epoch, melhor_val, parou_em


def main():
    perda_val = [0.90, 0.70, 0.55, 0.48, 0.45, 0.44, 0.47, 0.50, 0.55, 0.60]
    melhor_epoch, melhor_val, parou_em = early_stopping(perda_val, paciencia=3)
    print(f"melhor epoch: {melhor_epoch} (val={melhor_val:.2f})")
    print(f"parou no epoch: {parou_em}")
    print(f"epochs economizados: {len(perda_val) - 1 - parou_em}")


if __name__ == "__main__":
    main()
