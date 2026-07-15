"""Solução de referência — Exercício 3 da Lição 081.

Cobertura da IA sob limiar de confiança, com fallback determinístico.
"""


def predizer(x, conf, limiar):
    if conf >= limiar:
        return ("ia", "positivo" if x >= 0 else "negativo")
    return ("fallback", "positivo" if x >= 0 else "negativo")


entradas = [(0.8, 0.95), (-1.5, 0.60), (2.0, 0.88), (-0.2, 0.50), (0.1, 0.80)]
limiar = 0.75

n_ia = 0
for x, conf in entradas:
    origem, pred = predizer(x, conf, limiar)
    n_ia += origem == "ia"
    print(f"x={x:+.1f} conf={conf:.2f} -> {origem}:{pred}")

print(f"cobertura IA: {n_ia}/{len(entradas)}")
