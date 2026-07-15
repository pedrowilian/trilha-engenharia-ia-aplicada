"""Exercício 2 — Estimar a memória do fine-tuning completo.

Setup: tamanhos de modelo em bilhões de parâmetros: 1, 8 e 70.

Tarefa:
    Implemente `memoria_treino_gb(n_params_bilhoes, bytes_param=2,
    bytes_grad=2, bytes_otimizador=8)` que soma pesos + gradientes + estados do
    Adam por parâmetro e retorna o total em GB (dividindo por 1e9). Para cada
    tamanho, imprima a linha `modelo {b:>3}B  ->  {gb:7.1f} GB`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/077-fine-tuning-completo/solucao_2.saida.txt
"""
tamanhos = [1, 8, 70]

# TODO: implementar memoria_treino_gb(...) e imprimir o relatório por tamanho.
