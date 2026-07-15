"""Solucao de referencia - Exercicio 1 da Licao 089.

Tracing de prompts: um trace e uma lista de spans (etapas), cada uma com latencia
e custo. Agregar o trace da a latencia e o custo totais da requisicao e identifica
o gargalo - a base da observabilidade de um pipeline LLM.
"""

trace = [
    {"span": "embed", "latencia_ms": 50, "custo": 0.0001},
    {"span": "search", "latencia_ms": 30, "custo": 0.0000},
    {"span": "generate", "latencia_ms": 420, "custo": 0.0021},
    {"span": "guard", "latencia_ms": 25, "custo": 0.0003},
]

lat_total = sum(s["latencia_ms"] for s in trace)
custo_total = sum(s["custo"] for s in trace)
for s in trace:
    print(f"{s['span']:>9}: {s['latencia_ms']:>4} ms  ${s['custo']:.4f}")
print(f"{'TOTAL':>9}: {lat_total:>4} ms  ${custo_total:.4f}")

gargalo = max(trace, key=lambda s: s["latencia_ms"])
print(f"gargalo: {gargalo['span']} ({gargalo['latencia_ms']} ms)")
