"""Solução de referência — Exercício 3 da Lição 093.

Completude de model card: campos obrigatórios não preenchidos impedem a
publicação. Determinístico.
"""
campos_obrigatorios = ["uso_pretendido", "dados_treino", "metricas", "limitacoes", "vieses_conhecidos"]
model_card = {
    "uso_pretendido": "moderacao de comentarios",
    "dados_treino": "50k comentarios rotulados",
    "metricas": "F1=0.91",
    "limitacoes": "baixa cobertura de girias",
    "vieses_conhecidos": "",
}

faltando = [c for c in campos_obrigatorios if not model_card.get(c)]
preenchidos = len(campos_obrigatorios) - len(faltando)
print(f"campos preenchidos: {preenchidos}/{len(campos_obrigatorios)}")
print(f"faltando: {faltando}")
print(f"publicavel: {not faltando}")
