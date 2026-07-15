"""Exercício 3 — Propriedade de deslocamento relativo.

Setup (dado):
    pe = positional_encoding(12, 16)

Tarefa:
    - imprima PE[0]·PE[k] para k = 0..5 (4 casas), no formato
        k=0: PE[0]·PE[0] = 8.0000
    - verifique (booleano) que PE[2]·PE[5] == PE[4]·PE[7] (mesmo deslocamento k=3),
      imprimindo:
        PE[2]·PE[5] == PE[4]·PE[7] (k=3): True

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/041-positional-encoding/solucao_3.saida.txt
"""
import numpy as np

# TODO: implementar positional_encoding(12, 16) e checar a propriedade de deslocamento.
