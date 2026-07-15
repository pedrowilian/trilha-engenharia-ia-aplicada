"""Exercicio 3 - Escolha de arquitetura sob SLA e orcamento.

Setup (dado):
    arquiteturas = {
        "grande":       {"custo_1k": 12.0, "latencia_p95": 2000},
        "grande+cache": {"custo_1k": 7.0,  "latencia_p95": 1200},
        "pequeno+rag":  {"custo_1k": 3.5,  "latencia_p95": 800},
        "cascata":      {"custo_1k": 5.0,  "latencia_p95": 1150},
    }
    SLA_LATENCIA = 1300 ms ; ORCAMENTO_1k = 6.0 $.

Tarefa:
    Uma arquitetura e viavel se latencia_p95 <= SLA_LATENCIA E custo_1k <= ORCAMENTO_1k.
    Imprima, na ordem do dicionario,
        "<nome:>14>: custo=$<1c>/1k p95=<int>ms viavel=<bool>".
    Ao final, imprima a escolhida (menor custo entre as viaveis):
        "escolhida (menor custo entre viaveis): <nome>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/103-entrevistas-sistemas-ia/solucao_3.saida.txt
"""

arquiteturas = {
    "grande":       {"custo_1k": 12.0, "latencia_p95": 2000},
    "grande+cache": {"custo_1k": 7.0,  "latencia_p95": 1200},
    "pequeno+rag":  {"custo_1k": 3.5,  "latencia_p95": 800},
    "cascata":      {"custo_1k": 5.0,  "latencia_p95": 1150},
}
SLA_LATENCIA = 1300
ORCAMENTO_1k = 6.0

# TODO: filtre as arquiteturas viaveis e imprima a tabela e a escolhida.
