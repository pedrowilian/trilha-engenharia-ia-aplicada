"""Solução de referência — Exercício 2 da Lição 045.

Passos por época e número de épocas completas dado um orçamento de passos.
"""
D = 50_000_000_000        # tokens no dataset
batch_tokens = 500_000    # tokens por passo
passos_disponiveis = 200_000

passos_por_epoca = D // batch_tokens
epocas_completas = passos_disponiveis // passos_por_epoca
tokens_vistos = epocas_completas * D

print(f"passos por epoca = {passos_por_epoca}")
print(f"epocas completas = {epocas_completas}")
print(f"tokens vistos    = {tokens_vistos:.3e}")
