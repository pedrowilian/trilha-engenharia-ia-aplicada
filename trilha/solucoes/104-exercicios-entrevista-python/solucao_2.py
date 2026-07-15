"""Solucao de referencia - Exercicio 2 da Licao 104.

Two-sum com tabela hash: para cada numero, procura o complemento (alvo - x) ja
visto. Resolve em O(n) com O(n) de memoria - a resposta esperada em entrevista,
melhor que a forca bruta O(n^2).
"""


def two_sum(nums, alvo):
    visto = {}
    for i, x in enumerate(nums):
        comp = alvo - x
        if comp in visto:
            return (visto[comp], i)
        visto[x] = i
    return None


nums = [1, 4, 5, 8, 12]
print(two_sum(nums, 9))
print(two_sum(nums, 20))
print(two_sum(nums, 2))
