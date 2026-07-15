"""Solucao de referencia - Exercicio 2 da Licao 086.

LLM-as-judge simulado por uma rubrica deterministica: a nota de cada resposta e
a fracao de criterios da rubrica presentes no texto. Agrega por media e por taxa
de aprovacao num limiar. A rubrica fixa torna o juiz reprodutivel.
"""


def juiz(resposta, criterios):
    presentes = sum(1 for c in criterios if c in resposta.lower())
    return presentes / len(criterios)


casos = [
    ("Embeddings mapeiam texto para vetores densos", ["embeddings", "vetores", "densos"]),
    ("Tokenizacao quebra texto em tokens", ["tokenizacao", "tokens"]),
    ("A atencao usa query key value", ["atencao", "query", "key", "value"]),
    ("Dropout e uma forma de regularizacao", ["dropout", "regularizacao", "ruido"]),
]

notas = []
for resp, crit in casos:
    n = juiz(resp, crit)
    notas.append(n)
    print(f"nota={n:.4f} <- {resp!r}")

media = sum(notas) / len(notas)
limiar = 0.75
aprovados = sum(1 for n in notas if n >= limiar)
print(f"media do juiz: {media:.4f}")
print(f"aprovados (>= {limiar}): {aprovados}/{len(notas)}")
