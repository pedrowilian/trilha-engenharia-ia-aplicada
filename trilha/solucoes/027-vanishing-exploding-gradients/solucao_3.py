"""Solucao de referencia — Licao 027, Exercicio 3.

Gradient clipping por norma: so reescala quando a norma ultrapassa o teto.
Mostra um caso dentro do limite (sem clip) e um acima (com clip).
"""
import numpy as np


def clip_por_norma(g, max_norma):
    g = np.array(g, dtype=float)
    norma = np.linalg.norm(g)
    clipado = norma > max_norma
    if clipado:
        g = g * (max_norma / norma)
    return g, norma, clipado


def main():
    teto = 5.0
    for g in [[0.3, 0.4], [6.0, 8.0]]:
        g_out, norma, clipado = clip_por_norma(g, teto)
        print(f"g={g} norma={norma:.4f} clipado={clipado} "
              f"norma_final={np.linalg.norm(g_out):.4f}")


if __name__ == "__main__":
    main()
