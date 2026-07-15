"""Solução de referência — Exercício 3 da Lição 091.

Disparate impact: razão entre a taxa de seleção do grupo desfavorecido e a do
favorecido; a regra dos 80% reprova razões abaixo de 0.8. Determinístico.
"""
taxa_a = 0.50
taxa_b = 0.45

favorecida = max(taxa_a, taxa_b)
desfavorecida = min(taxa_a, taxa_b)
ratio = desfavorecida / favorecida
passa = ratio >= 0.8
print(f"razao de impacto: {ratio:.2f}")
print(f"regra dos 80%: {'passa' if passa else 'reprova'}")
