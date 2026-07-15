"""Exercício 1 — Classificação por risco (estilo AI Act).

Setup: a lista `sistemas`, cada um com as chaves booleanas `proibido`,
`dominio_critico` e `interage_com_usuario`, além de `nome` (no esqueleto):
    - identificacao biometrica em massa: proibido=True,  critico=True,  interage=False
    - diagnostico medico:                proibido=False, critico=True,  interage=True
    - assistente de escrita:             proibido=False, critico=False, interage=True
    - recomendacao de musica:            proibido=False, critico=False, interage=False

Tarefa:
    Implemente `classificar(sistema)` que retorna, na ordem da mais grave para a
    mais branda: "inaceitavel" (proibido), "alto" (dominio_critico), "limitado"
    (interage_com_usuario) ou "minimo". Imprima `"{nome:>34}: {nivel}"` por sistema.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/093-legal-regulatorio-ia-responsavel/solucao_1.saida.txt
"""

# TODO: implemente a classificação por regras e percorra os sistemas.
