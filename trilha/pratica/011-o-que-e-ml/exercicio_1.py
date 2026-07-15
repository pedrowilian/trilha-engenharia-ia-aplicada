"""Licao 011 — Exercicio 1: classificador supervisionado 1-NN do zero.

Tarefa:
- Dado o conjunto de TREINO rotulado abaixo (peso_g, indice_de_cor) -> rotulo,
  implemente um classificador de vizinho mais proximo (1-NN) usando distancia
  euclidiana.
- Classifique os tres pontos de `novos` e imprima, por linha, `x=<ponto> -> <rotulo>`.
- Ao final, imprima `acertos: <n>/3` comparando com o gabarito ["maca","banana","maca"].

Criterio binario: a saida deve ser IDENTICA a
trilha/solucoes/011-o-que-e-ml/solucao_1.saida.txt
"""

treino = [
    ((150.0, 0.9), "maca"),
    ((160.0, 0.8), "maca"),
    ((140.0, 0.85), "maca"),
    ((120.0, 0.2), "banana"),
    ((130.0, 0.15), "banana"),
    ((118.0, 0.25), "banana"),
]

novos = [(155.0, 0.88), (125.0, 0.18), (145.0, 0.7)]


def distancia(a, b):
    raise NotImplementedError("implemente a distancia euclidiana")


def prever(x):
    raise NotImplementedError("retorne o rotulo do exemplo de treino mais proximo")


def main():
    raise NotImplementedError("classifique `novos` e conte os acertos")


if __name__ == "__main__":
    main()
