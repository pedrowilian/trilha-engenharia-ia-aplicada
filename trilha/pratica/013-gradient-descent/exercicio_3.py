"""Licao 013 — Exercicio 3: batch vs mini-batch vs SGD.

Tarefa:
- Dados X = [1,2,3,4,5], Y = [2,4,6,8,10] (relacao y = 2x, modelo w*x),
  w inicial = 0.0, eta = 0.01, 300 epocas.
- Implemente uma funcao de treino parametrizada pelo tamanho do lote (5, 2 e 1)
  que atualiza w por lote e conta as atualizacoes.
- Imprima, por variante, `<nome>: w=<2 casas> atualizacoes=<n>`.

Criterio binario: as tres variantes convergem para o mesmo w (2 casas) e as
atualizacoes sao 300, 900 e 1500; saida IDENTICA a
trilha/solucoes/013-gradient-descent/solucao_3.saida.txt
"""

X = [1.0, 2.0, 3.0, 4.0, 5.0]
Y = [2.0, 4.0, 6.0, 8.0, 10.0]


def grad_subconjunto(w, idxs):
    raise NotImplementedError


def treinar(tamanho_lote, epocas=300, eta=0.01):
    raise NotImplementedError


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
