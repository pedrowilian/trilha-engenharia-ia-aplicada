"""Exercicio 2 - LLM-as-judge com rubrica deterministica.

Setup (dado):
    casos = [
        ("Embeddings mapeiam texto para vetores densos", ["embeddings", "vetores", "densos"]),
        ("Tokenizacao quebra texto em tokens", ["tokenizacao", "tokens"]),
        ("A atencao usa query key value", ["atencao", "query", "key", "value"]),
        ("Dropout e uma forma de regularizacao", ["dropout", "regularizacao", "ruido"]),
    ]
    limiar = 0.75

Tarefa:
    Implemente juiz(resposta, criterios) = fracao de criterios presentes (em
    minusculas) no texto. Imprima "nota=<4 casas> <- <repr da resposta>" por caso
    e, ao final, "media do juiz: <4 casas>" e
    "aprovados (>= <limiar>): <contagem>/<total>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/086-metricas-datasets-avaliacao/solucao_2.saida.txt
"""

casos = [
    ("Embeddings mapeiam texto para vetores densos", ["embeddings", "vetores", "densos"]),
    ("Tokenizacao quebra texto em tokens", ["tokenizacao", "tokens"]),
    ("A atencao usa query key value", ["atencao", "query", "key", "value"]),
    ("Dropout e uma forma de regularizacao", ["dropout", "regularizacao", "ruido"]),
]
limiar = 0.75

# TODO: implemente o juiz por rubrica, imprima as notas e a agregacao.
