"""Solucao de referencia - Exercicio 2 da Licao 085.

Agregacao de scores continuos: calcula a media e a taxa de aprovacao em relacao
a um limiar fixo. A taxa de aprovacao (pass rate) e mais acionavel que a media
quando o que importa e "quantas amostras passaram no criterio".
"""

scores = [0.91, 0.74, 0.55, 0.69, 0.83, 0.78, 0.45]
limiar = 0.70

media = sum(scores) / len(scores)
aprovados = sum(1 for s in scores if s >= limiar)
taxa = aprovados / len(scores)

print(f"n amostras: {len(scores)}")
print(f"media: {media:.4f}")
print(f"aprovados (>= {limiar}): {aprovados}")
print(f"taxa de aprovacao: {taxa:.4f}")
