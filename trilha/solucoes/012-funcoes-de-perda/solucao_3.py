"""Solucao de referencia — Licao 012, Exercicio 3.

Softmax + entropia cruzada multiclasse do zero. Mostra que minimizar a
cross-entropy equivale a maximizar a probabilidade atribuida a classe correta.
"""
import math


def softmax(z):
    m = max(z)
    exps = [math.exp(v - m) for v in z]
    s = sum(exps)
    return [e / s for e in exps]


def cross_entropy(logits, classe_certa):
    p = softmax(logits)
    return -math.log(p[classe_certa])


def main():
    # Dois conjuntos de logits para a mesma classe certa (indice 0).
    logits_confiante = [4.0, 1.0, 0.0]   # ja aposta forte na classe certa
    logits_indeciso = [1.0, 0.9, 0.8]    # quase uniforme
    lc = cross_entropy(logits_confiante, 0)
    li = cross_entropy(logits_indeciso, 0)
    print(f"cross-entropy (confiante): {lc:.4f}")
    print(f"cross-entropy (indeciso):  {li:.4f}")
    print("menor perda = mais confianca na classe certa:", lc < li)


if __name__ == "__main__":
    main()
