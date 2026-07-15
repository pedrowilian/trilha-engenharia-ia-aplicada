"""Solucao de referencia - Exercicio 3 da Licao 103.

System design sob restricoes: dada uma SLA de latencia e um orcamento de custo,
filtra as arquiteturas viaveis e escolhe a mais barata entre elas. E a forma
honesta de responder "qual arquitetura voce usaria?": com numeros e trade-offs.
"""

arquiteturas = {
    "grande":       {"custo_1k": 12.0, "latencia_p95": 2000},
    "grande+cache": {"custo_1k": 7.0,  "latencia_p95": 1200},
    "pequeno+rag":  {"custo_1k": 3.5,  "latencia_p95": 800},
    "cascata":      {"custo_1k": 5.0,  "latencia_p95": 1150},
}
SLA_LATENCIA = 1300   # ms
ORCAMENTO_1k = 6.0    # $

viaveis = {nome: a for nome, a in arquiteturas.items()
           if a["latencia_p95"] <= SLA_LATENCIA and a["custo_1k"] <= ORCAMENTO_1k}
for nome, a in arquiteturas.items():
    ok = nome in viaveis
    print(f"{nome:>14}: custo=${a['custo_1k']:.1f}/1k p95={a['latencia_p95']}ms viavel={ok}")
escolhida = min(viaveis, key=lambda n: viaveis[n]["custo_1k"])
print(f"escolhida (menor custo entre viaveis): {escolhida}")
