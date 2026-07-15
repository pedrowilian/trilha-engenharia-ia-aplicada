"""Solucao de referencia - Exercicio 3 da Licao 088.

Lei de Little (L = lambda * W): o numero medio de requisicoes simultaneas no
sistema e o produto da taxa de chegada pelo tempo medio de servico. Dele sai a
concorrencia minima (slots) necessaria para atender o trafego sem formar fila.
"""
import math

taxa_chegada = 120.0     # req/s (lambda)
tempo_servico_s = 0.5    # s por requisicao (W)

concorrencia_media = taxa_chegada * tempo_servico_s
slots_necessarios = math.ceil(concorrencia_media)
vazao_por_slot = 1 / tempo_servico_s

print(f"concorrencia media (L = lambda*W): {concorrencia_media:.1f}")
print(f"slots necessarios (teto): {slots_necessarios}")
print(f"vazao por slot: {vazao_por_slot:.2f} req/s")
