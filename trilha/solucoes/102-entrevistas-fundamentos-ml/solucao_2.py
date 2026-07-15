"""Solucao de referencia - Exercicio 2 da Licao 102.

Expected Calibration Error (ECE): agrupa as previsoes em bins de confianca e
soma |acuracia - confianca_media| ponderado pela fracao de exemplos no bin. ECE
alto = o modelo nao "sabe o quanto sabe".
"""


def ece(confiancas, acertos, n_bins=5):
    n = len(confiancas)
    total = 0.0
    for b in range(n_bins):
        lo, hi = b / n_bins, (b + 1) / n_bins
        idx = [i for i in range(n) if (lo < confiancas[i] <= hi) or (b == 0 and confiancas[i] <= hi)]
        if not idx:
            continue
        conf_media = sum(confiancas[i] for i in idx) / len(idx)
        acc = sum(acertos[i] for i in idx) / len(idx)
        peso = len(idx) / n
        contrib = peso * abs(acc - conf_media)
        total += contrib
        print(f"bin {b} ({lo:.1f}-{hi:.1f}]: n={len(idx)} conf={conf_media:.3f} acc={acc:.3f} contrib={contrib:.4f}")
    return total


confiancas = [0.45, 0.58, 0.61, 0.66, 0.72, 0.83, 0.87, 0.91, 0.93, 0.97]
acertos    = [0,    1,    0,    1,    1,    1,    0,    1,    1,    1]
valor = ece(confiancas, acertos, n_bins=5)
print(f"ECE = {valor:.4f}")
