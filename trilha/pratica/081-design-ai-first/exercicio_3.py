"""Exercício 3 — Cobertura com limiar de confiança.

Setup:
    entradas = [(0.8, 0.95), (-1.5, 0.60), (2.0, 0.88), (-0.2, 0.50), (0.1, 0.80)]
    limiar = 0.75
    Cada par é (x, confianca).

Tarefa:
    Implemente `predizer(x, conf, limiar)` que devolve ("ia", ...) quando
    conf >= limiar (o sinal de x decide "positivo"/"negativo") e
    ("fallback", ...) caso contrário. Imprima
    `x={x:+.1f} conf={conf:.2f} -> {origem}:{pred}` e, ao final,
    `cobertura IA: {n_ia}/{total}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/081-design-ai-first/solucao_3.saida.txt
"""

entradas = [(0.8, 0.95), (-1.5, 0.60), (2.0, 0.88), (-0.2, 0.50), (0.1, 0.80)]
limiar = 0.75

# TODO: implemente predizer(...) e calcule a cobertura da IA.
