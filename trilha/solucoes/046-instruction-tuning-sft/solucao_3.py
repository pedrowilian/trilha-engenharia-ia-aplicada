"""Solução de referência — Exercício 3 da Lição 046.

Compara a perda sem máscara (estilo pré-treino) com a perda mascarada (SFT).
"""
import numpy as np

p_alvo = np.array([0.4, 0.7, 0.3, 0.95, 0.5, 0.6])
mascara = np.array([0, 0, 0, 1, 1, 1])
nll = -np.log(p_alvo)

perda_sem_mascara = nll.mean()
perda_com_mascara = (nll * mascara).sum() / mascara.sum()

print(f"perda sem mascara (pre-treino) = {perda_sem_mascara:.4f}")
print(f"perda com mascara (SFT)        = {perda_com_mascara:.4f}")
print("mascara muda o gradiente:", perda_sem_mascara != perda_com_mascara)
