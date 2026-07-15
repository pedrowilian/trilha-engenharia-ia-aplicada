"""Exercicio 2 - Expected Calibration Error (ECE).

Setup (dado):
    confiancas = [0.45, 0.58, 0.61, 0.66, 0.72, 0.83, 0.87, 0.91, 0.93, 0.97]
    acertos    = [0,    1,    0,    1,    1,    1,    0,    1,    1,    1]
    n_bins = 5 (largura 0.2 cada).

Tarefa:
    Para cada bin b com algum exemplo, atribua o exemplo i ao bin se
        (b/n_bins < conf_i <= (b+1)/n_bins) ou (b == 0 e conf_i <= 1/n_bins).
    Imprima "bin <b> (<lo:.1f>-<hi:.1f>]: n=<n> conf=<3c> acc=<3c> contrib=<4c>"
    onde contrib = (n_bin / n) * |acc - conf_media|. Some as contribuicoes e
    imprima "ECE = <4 casas>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/102-entrevistas-fundamentos-ml/solucao_2.saida.txt
"""

confiancas = [0.45, 0.58, 0.61, 0.66, 0.72, 0.83, 0.87, 0.91, 0.93, 0.97]
acertos    = [0,    1,    0,    1,    1,    1,    0,    1,    1,    1]

# TODO: implemente ece(confiancas, acertos, n_bins=5) e imprima os bins e o ECE.
