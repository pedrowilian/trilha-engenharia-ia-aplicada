"""Solucao de referencia - Exercicio 1 da Licao 086.

Precisao, revocacao e F1 a partir do conjunto de itens relevantes (gabarito) e
do conjunto recuperado. As metricas saem de TP/FP/FN, calculados por operacoes
de conjunto.
"""

relevantes = {"d2", "d4", "d6"}
recuperados = {"d1", "d2", "d3", "d4"}

tp = len(relevantes & recuperados)
fp = len(recuperados - relevantes)
fn = len(relevantes - recuperados)

precisao = tp / (tp + fp)
revocacao = tp / (tp + fn)
f1 = 2 * precisao * revocacao / (precisao + revocacao)

print(f"TP={tp} FP={fp} FN={fn}")
print(f"precisao: {precisao:.4f}")
print(f"revocacao: {revocacao:.4f}")
print(f"f1: {f1:.4f}")
