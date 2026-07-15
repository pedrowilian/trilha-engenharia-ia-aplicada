"""Exercício 1 — Métricas de avaliação no conjunto de teste.

Setup: as listas `gold` e `predicoes` (abaixo) e o conjunto `rotulos_validos`.

Tarefa:
    Calcule os acertos (exact-match), a acurácia (acertos/total) e a taxa de
    formato válido (fração de predições dentro de `rotulos_validos`). Imprima
    `acertos: {a}/{n}`, `acuracia: {:.3f}` e `formato valido: {:.3f}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/080-avaliacao-modelo-ajustado/solucao_1.saida.txt
"""
gold = ["spam", "ham", "spam", "ham", "spam", "ham"]
predicoes = ["spam", "ham", "spam", "spam", "lixo", "ham"]
rotulos_validos = {"spam", "ham"}

# TODO: calcular acertos, acuracia e taxa de formato valido; imprimir.
