"""Solucao de referencia - Exercicio 3 da Licao 085.

Comparacao pareada de duas versoes (A e B) amostra a amostra e veredito de
regressao. A regressao e declarada quando a media de B fica abaixo da media de A
(delta negativo): e o teste que protege uma versao boa de ser substituida por uma pior.
"""

scores_a = [0.88, 0.72, 0.91, 0.66, 0.80, 0.77]
scores_b = [0.80, 0.70, 0.85, 0.60, 0.82, 0.71]

vitorias = empates = derrotas = 0
for a, b in zip(scores_a, scores_b):
    if b > a:
        vitorias += 1
    elif b < a:
        derrotas += 1
    else:
        empates += 1

media_a = sum(scores_a) / len(scores_a)
media_b = sum(scores_b) / len(scores_b)
delta = media_b - media_a
regrediu = delta < 0

print(f"B vence: {vitorias} | empata: {empates} | perde: {derrotas}")
print(f"media A: {media_a:.4f} | media B: {media_b:.4f}")
print(f"delta (B - A): {delta:+.4f}")
print(f"regressao: {regrediu}")
