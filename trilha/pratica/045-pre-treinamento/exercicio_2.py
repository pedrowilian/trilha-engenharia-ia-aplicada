"""Exercício 2 — Passos de treino e número de épocas.

Setup: D tokens no dataset, batch_tokens por passo, passos_disponiveis.

Tarefa:
    Calcule os passos por época (D // batch_tokens) e quantas épocas completas
    cabem em passos_disponiveis (divisão inteira). Imprima `passos por epoca`,
    `epocas completas` e os `tokens vistos` totais ({:.3e}).

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/045-pre-treinamento/solucao_2.saida.txt
"""
D = 50_000_000_000
batch_tokens = 500_000
passos_disponiveis = 200_000

# TODO: calcular passos por epoca, epocas completas e tokens vistos; imprimir.
