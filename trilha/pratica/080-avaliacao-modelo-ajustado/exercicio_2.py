"""Exercício 2 — Teste A/B: base vs ajustado.

Setup: as listas `gold`, `base` e `ajustado` (abaixo).

Tarefa:
    Implemente `acuracia(gold, pred)`. Calcule a acurácia de base e ajustado,
    o lift absoluto (ajustado - base) e o relativo (100*lift/acc_base) e o
    vencedor. Imprima nas linhas `acuracia base    :`, `acuracia ajustado:`,
    `lift absoluto    : {:+.3f}`, `lift relativo    : {:+.1f}%` e `vencedor:`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/080-avaliacao-modelo-ajustado/solucao_2.saida.txt
"""
gold = ["x", "y", "z", "x", "y", "z", "x", "y"]
base = ["x", "y", "x", "x", "z", "z", "x", "x"]
ajustado = ["x", "y", "z", "x", "y", "z", "x", "y"]

# TODO: implementar acuracia(...), calcular lifts e o vencedor; imprimir.
