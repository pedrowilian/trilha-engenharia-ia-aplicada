"""Exercicio 1 - Decomposicao vies-variancia e complexidade otima.

Setup (dado):
    erros(k) retorna (vies2, variancia, ruido, total) com
        vies2 = 16.0 / k ; variancia = 0.05 * k ; ruido = 0.5 ;
        total = vies2 + variancia + ruido.

Tarefa:
    Imprima, para k em [1, 5, 10, 15, 20],
        "k=<k:2d>: vies2=<2c> var=<2c> ruido=<2c> total=<2c>".
    Depois encontre e imprima a complexidade otima (menor total) em 1..20:
        "complexidade otima (1..20): <k>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/102-entrevistas-fundamentos-ml/solucao_1.saida.txt
"""


def erros(complexidade):
    vies2 = 16.0 / complexidade
    variancia = 0.05 * complexidade
    ruido = 0.5
    return vies2, variancia, ruido, vies2 + variancia + ruido


# TODO: imprima a tabela de erros e a complexidade otima em 1..20.
