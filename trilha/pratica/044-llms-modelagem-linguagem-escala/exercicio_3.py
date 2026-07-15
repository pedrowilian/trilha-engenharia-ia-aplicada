"""Exercício 3 — Inverter a lei de escala.

Setup: parâmetros E, A, alpha e a perda-alvo L_alvo.

Tarefa:
    Isole N em L = E + A * N^(-alpha), obtendo N = (A / (L - E))^(1/alpha).
    Imprima o N necessario em notação científica ({N:.3e}) e verifique
    recomputando a perda nesse N (4 casas).

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/044-llms-modelagem-linguagem-escala/solucao_3.saida.txt
"""
E, A, alpha = 1.6, 2100.0, 0.34
L_alvo = 2.0

# TODO: isolar N, imprimir N necessario e a perda recomputada.
