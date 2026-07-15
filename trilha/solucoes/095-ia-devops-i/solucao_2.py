"""Solução de referência — Exercício 2 da Lição 095.

AIOps: detecção de anomalias por z-score robusto (mediana e MAD), em Python
puro. Determinístico.
"""


def mediana(xs):
    s = sorted(xs)
    n = len(s)
    m = n // 2
    return s[m] if n % 2 else (s[m - 1] + s[m]) / 2.0


def detectar(serie, k=3.5):
    med = mediana(serie)
    mad = mediana([abs(x - med) for x in serie]) * 1.4826
    anomalias = []
    for i, x in enumerate(serie):
        if mad > 0 and abs(x - med) / mad > k:
            anomalias.append(i)
    return anomalias


serie = [50, 52, 51, 49, 50, 51, 120, 50, 49, 51]

print("mediana:", mediana(serie))
print("anomalias:", detectar(serie))
