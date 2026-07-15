"""Solução de referência — Exercício 1 da Lição 093.

Classificação por risco baseada em regras (estilo AI Act): a primeira condição
satisfeita, da mais grave para a mais branda, define o nível. Determinístico.
"""


def classificar(sistema):
    if sistema["proibido"]:
        return "inaceitavel"
    if sistema["dominio_critico"]:
        return "alto"
    if sistema["interage_com_usuario"]:
        return "limitado"
    return "minimo"


sistemas = [
    {"nome": "identificacao biometrica em massa", "proibido": True, "dominio_critico": True, "interage_com_usuario": False},
    {"nome": "diagnostico medico", "proibido": False, "dominio_critico": True, "interage_com_usuario": True},
    {"nome": "assistente de escrita", "proibido": False, "dominio_critico": False, "interage_com_usuario": True},
    {"nome": "recomendacao de musica", "proibido": False, "dominio_critico": False, "interage_com_usuario": False},
]

for s in sistemas:
    print(f"{s['nome']:>34}: {classificar(s)}")
