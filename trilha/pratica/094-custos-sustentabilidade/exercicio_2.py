"""Exercício 2 — Pegada energética e de carbono.

Setup: `energia_wh_por_1k = 0.5` (Wh por 1k tokens), `tokens_mes = 300_000_000`,
`intensidade = 300.0` (g CO2 por kWh) (no esqueleto).

Tarefa:
    Calcule `energia_kwh = (tokens_mes / 1000 * energia_wh_por_1k) / 1000` e
    `co2_kg = energia_kwh * intensidade / 1000`. Imprima
    `"energia: {energia_kwh:.1f} kWh/mes"` e `"emissao: {co2_kg:.1f} kg CO2/mes"`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/094-custos-sustentabilidade/solucao_2.saida.txt
"""

# TODO: converta tokens em energia (kWh) e energia em emissão de CO2 (kg).
