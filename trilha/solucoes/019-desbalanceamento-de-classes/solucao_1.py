"""Solucao de referencia — Licao 019, Exercicio 1.

Paradoxo da acuracia: classificador trivial (sempre majoritaria) tem acuracia
alta mas recall zero na classe rara; a acuracia balanceada revela o problema.
"""


def main():
    # 1000 exemplos: 950 negativos, 50 positivos.
    y = [0] * 950 + [1] * 50
    pred = [0] * 1000   # sempre negativo

    acc = sum(1 for r, p in zip(y, pred) if r == p) / len(y)
    # recall por classe
    rec_pos = sum(1 for r, p in zip(y, pred) if r == 1 and p == 1) / y.count(1)
    rec_neg = sum(1 for r, p in zip(y, pred) if r == 0 and p == 0) / y.count(0)
    acc_balanceada = (rec_pos + rec_neg) / 2
    print(f"acuracia: {acc:.4f}")
    print(f"recall positivo: {rec_pos:.4f}")
    print(f"recall negativo: {rec_neg:.4f}")
    print(f"acuracia balanceada: {acc_balanceada:.4f}")
    print("acuracia engana:", acc > 0.9 and acc_balanceada <= 0.5)


if __name__ == "__main__":
    main()
