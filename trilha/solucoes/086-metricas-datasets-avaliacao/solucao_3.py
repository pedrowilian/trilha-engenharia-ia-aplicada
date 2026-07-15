"""Solucao de referencia - Exercicio 3 da Licao 086.

Metrica offline (accuracy num dataset rotulado) versus metrica online (taxa de
satisfacao de usuarios reais). A lacuna entre as duas mede o quanto o eval de
laboratorio super- ou subestima a experiencia em producao.
"""

offline_total = 10
offline_acertos = 9
offline_acc = offline_acertos / offline_total

online_total = 500
online_positivos = 310
online_sat = online_positivos / online_total

print(f"offline accuracy: {offline_acc:.4f} ({offline_acertos}/{offline_total})")
print(f"online satisfacao: {online_sat:.4f} ({online_positivos}/{online_total})")
lacuna = offline_acc - online_sat
print(f"lacuna offline-online: {lacuna:+.4f}")
