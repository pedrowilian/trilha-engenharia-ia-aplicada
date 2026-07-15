"""Exercicio 3 - Lei de Little e concorrencia.

Setup (dado):
    taxa_chegada = 120.0   # req/s (lambda)
    tempo_servico_s = 0.5  # s por requisicao (W)

Tarefa:
    Pela Lei de Little, concorrencia_media = taxa_chegada * tempo_servico_s.
    Calcule slots_necessarios = teto(concorrencia_media) e
    vazao_por_slot = 1 / tempo_servico_s. Imprima, nesta ordem:
    "concorrencia media (L = lambda*W): <1 casa>",
    "slots necessarios (teto): <n>", "vazao por slot: <2 casas> req/s".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/088-latencia-inferencia/solucao_3.saida.txt
"""
import math

taxa_chegada = 120.0
tempo_servico_s = 0.5

# TODO: aplique a Lei de Little, calcule slots e vazao por slot, e imprima.
