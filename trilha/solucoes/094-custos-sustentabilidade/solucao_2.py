"""Solução de referência — Exercício 2 da Lição 094.

Pegada energética e de carbono: converte tokens em energia (kWh) e energia em
emissão de CO2 a partir da intensidade de carbono da rede. Determinístico.
"""
energia_wh_por_1k = 0.5    # Wh por 1k tokens
tokens_mes = 300_000_000   # tokens por mes
intensidade = 300.0        # g CO2 por kWh

energia_kwh = (tokens_mes / 1000 * energia_wh_por_1k) / 1000
co2_kg = energia_kwh * intensidade / 1000
print(f"energia: {energia_kwh:.1f} kWh/mes")
print(f"emissao: {co2_kg:.1f} kg CO2/mes")
