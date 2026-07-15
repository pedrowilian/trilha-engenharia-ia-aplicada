"""Solução de referência — Exercício 2 da Lição 077.

Estima a memória de treino do fine-tuning COMPLETO: pesos + gradientes +
estados do otimizador Adam (m e v), em bytes por parâmetro.
"""


def memoria_treino_gb(n_params_bilhoes, bytes_param=2, bytes_grad=2, bytes_otimizador=8):
    n = n_params_bilhoes * 1e9
    return n * (bytes_param + bytes_grad + bytes_otimizador) / 1e9


for b in [1, 8, 70]:
    print(f"modelo {b:>3}B  ->  {memoria_treino_gb(b):7.1f} GB")
