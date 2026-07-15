"""Exercício 3 — Detecção de overfitting e early stopping.

Setup: as listas `treino` e `validacao` (perda por época, abaixo).

Tarefa:
    Encontre a melhor época (índice do mínimo da validação), o gap
    treino-validação nessa época e detecte overfitting (alguma subida da
    validação após o mínimo). Imprima `epocas:`, `melhor epoca (min val):`,
    `val minima: {:.2f}`, `gap treino-val na melhor epoca: {:.2f}`,
    `overfitting detectado:` e `recomendacao: early stopping na epoca {melhor}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/080-avaliacao-modelo-ajustado/solucao_3.saida.txt
"""
treino = [1.00, 0.70, 0.50, 0.38, 0.30, 0.24, 0.20]
validacao = [1.05, 0.80, 0.62, 0.55, 0.57, 0.63, 0.71]

# TODO: achar a melhor epoca, o gap e detectar overfitting; imprimir.
