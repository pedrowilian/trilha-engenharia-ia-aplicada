"""Solução de referência — Exercício 1 da Lição 098.

Priorização por RICE = (Reach · Impact · Confidence) / Effort. Ordena o backlog
do maior para o menor score. Determinístico.
"""


def rice(reach, impact, confidence, effort):
    return (reach * impact * confidence) / effort


itens = [
    ("relatorios", 6000, 1.5, 0.9, 3.0),
    ("alertas", 4000, 2.0, 0.8, 4.0),
    ("temas", 1000, 0.5, 1.0, 1.0),
]
ranking = sorted(itens, key=lambda it: rice(*it[1:]), reverse=True)
for nome, *args in ranking:
    print(f"{nome}: RICE={rice(*args):.0f}")
