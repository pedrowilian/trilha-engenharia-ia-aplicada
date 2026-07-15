"""Exercicio 3 - Decisao de rollout canary.

Setup (dado):
    baseline = {"taxa_erro": 0.03, "p95_ms": 500}
    canary   = {"taxa_erro": 0.02, "p95_ms": 510}
    margem_erro = 0.01 ; margem_p95 = 50

Tarefa:
    Promova o canary apenas se a taxa de erro <= baseline + margem_erro E o p95 <=
    baseline + margem_p95; caso contrario, rollback. Imprima, nesta ordem:
    "erro: baseline=<2 casas> canary=<2 casas> ok=<bool>",
    "p95: baseline=<n> canary=<n> ok=<bool>",
    "decisao: <promover|rollback>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/089-mlops-llmops-observabilidade/solucao_3.saida.txt
"""

baseline = {"taxa_erro": 0.03, "p95_ms": 500}
canary = {"taxa_erro": 0.02, "p95_ms": 510}
margem_erro = 0.01
margem_p95 = 50

# TODO: avalie os dois criterios, decida promover/rollback e imprima no formato pedido.
