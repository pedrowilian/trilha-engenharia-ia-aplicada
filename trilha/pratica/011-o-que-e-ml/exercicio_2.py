"""Licao 011 — Exercicio 2: k-means (k=2) do zero, sem rotulos.

Tarefa:
- Agrupe os pontos 1D de `dados` em dois clusters, partindo de `centroides`.
- A cada iteracao: (1) atribua cada ponto ao centroide mais proximo; (2) recalcule
  cada centroide como a media do seu grupo. Pare quando os centroides nao mudarem.
- Imprima: `iteracoes ate convergir: <n>`, `centroides finais: [c0, c1]` (4 casas),
  `grupo 0: [...]` e `grupo 1: [...]`.

Criterio binario: saida IDENTICA a
trilha/solucoes/011-o-que-e-ml/solucao_2.saida.txt
"""

dados = [2.0, 2.5, 3.0, 10.0, 10.5, 11.0, 11.5]
centroides = [0.0, 20.0]


def atribuir(dados, centroides):
    raise NotImplementedError("atribua cada ponto ao centroide mais proximo")


def main():
    raise NotImplementedError("itere k-means ate a convergencia e imprima o resultado")


if __name__ == "__main__":
    main()
