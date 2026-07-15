"""Solução de referência — Exercício 1 da Lição 080.

Avalia um modelo ajustado num conjunto de teste: acurácia (exact-match) e taxa
de saídas no formato válido (rótulos dentro do conjunto permitido).
"""
gold = ["spam", "ham", "spam", "ham", "spam", "ham"]
predicoes = ["spam", "ham", "spam", "spam", "lixo", "ham"]
rotulos_validos = {"spam", "ham"}

acertos = sum(1 for g, p in zip(gold, predicoes) if g == p)
acuracia = acertos / len(gold)
formato_ok = sum(1 for p in predicoes if p in rotulos_validos) / len(predicoes)

print(f"acertos: {acertos}/{len(gold)}")
print(f"acuracia: {acuracia:.3f}")
print(f"formato valido: {formato_ok:.3f}")
