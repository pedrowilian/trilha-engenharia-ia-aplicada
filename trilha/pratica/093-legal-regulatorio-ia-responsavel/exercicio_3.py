"""Exercício 3 — Completude de model card.

Setup (no esqueleto):
    campos_obrigatorios = ["uso_pretendido", "dados_treino", "metricas", "limitacoes", "vieses_conhecidos"]
    model_card = {
        "uso_pretendido": "moderacao de comentarios",
        "dados_treino": "50k comentarios rotulados",
        "metricas": "F1=0.91",
        "limitacoes": "baixa cobertura de girias",
        "vieses_conhecidos": "",
    }

Tarefa:
    Determine os campos `faltando` (vazios ou ausentes) e os `preenchidos`.
    Imprima `"campos preenchidos: {p}/{total}"`, `"faltando: {lista}"` e
    `"publicavel: {True se nada faltando}"`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/093-legal-regulatorio-ia-responsavel/solucao_3.saida.txt
"""

# TODO: detecte campos vazios e decida se o model card é publicável.
