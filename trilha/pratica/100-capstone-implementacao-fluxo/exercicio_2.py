"""Exercício 2 — Seleção de ferramenta pelo agente.

Setup:
    perguntas = [
        "Como redefinir a senha?",
        "Quantos documentos existem?",
        "Onde baixo a fatura?",
    ]

Tarefa:
    Implemente `decidir(pergunta)` que devolve "contar" quando a pergunta contém
    "quantos" ou "quantidade" (case-insensitive) e "buscar" caso contrário.
    A ferramenta `buscar(consulta)` devolve `f"resultado para {consulta!r}"` e
    `contar(consulta)` devolve `"3 documentos na base"`. Para cada pergunta
    imprima `ferramenta={nome} obs={observacao}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/100-capstone-implementacao-fluxo/solucao_2.saida.txt.
"""

perguntas = [
    "Como redefinir a senha?",
    "Quantos documentos existem?",
    "Onde baixo a fatura?",
]

# TODO: implemente buscar, contar, decidir e imprima a ferramenta + observacao.
