"""Solucao de referencia - Exercicio 1 da Licao 088.

Decomposicao de latencia: a latencia total e o tempo ate o primeiro token (TTFT)
mais o tempo de gerar os demais tokens. Com streaming, o usuario percebe apenas o
TTFT, o que reduz drasticamente a latencia *percebida*.
"""

ttft_ms = 250
tempo_por_token_ms = 15
tokens_saida = 200

latencia_total = ttft_ms + tokens_saida * tempo_por_token_ms

print(f"TTFT: {ttft_ms} ms")
print(f"latencia total (sem streaming): {latencia_total} ms")
print(f"latencia percebida (streaming, ate 1o token): {ttft_ms} ms")
print(f"reducao percebida: {(1 - ttft_ms / latencia_total) * 100:.1f}%")
