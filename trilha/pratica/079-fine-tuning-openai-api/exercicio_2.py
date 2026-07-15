"""Exercício 2 — Criar job e estimar passos de treino.

Setup: file_id="file-0001", modelo_base="base-mini", n_exemplos=50,
n_epochs=3, lr_mult=0.2, batch_size=8.

Tarefa:
    Implemente `criar_job(...)` que devolve o dicionário do job com
    `hyperparameters` (n_epochs, learning_rate_multiplier, batch_size),
    `status="validating_files"` e `passos_estimados = n_epochs *
    ceil(n_exemplos / batch_size)`. Imprima o cabeçalho do job, cada
    hiperparâmetro e os passos estimados.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/079-fine-tuning-openai-api/solucao_2.saida.txt
"""
import math

# TODO: implementar criar_job(...) e imprimir job + hiperparâmetros + passos.
