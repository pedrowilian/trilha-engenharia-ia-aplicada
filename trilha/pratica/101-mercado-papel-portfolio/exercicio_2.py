"""Exercicio 2 - Pontuar repositorios de portfolio por sinais.

Setup (dado):
    PESOS = {"readme": 2, "testes": 3, "ci": 2, "docs": 1, "demo": 2}
    repos = {
        "pipeline-rag":   {"readme": True,  "testes": True,  "ci": True,  "docs": True,  "demo": False},
        "demo-agente":    {"readme": True,  "testes": False, "ci": False, "docs": False, "demo": True},
        "scripts-soltos": {"readme": False, "testes": False, "ci": False, "docs": False, "demo": False},
    }

Tarefa:
    Implemente pontuar(repo) somando os pesos dos sinais presentes (True).
    Calcule maximo = soma de PESOS. Ordene os repos por pontuacao decrescente
    e imprima "<nome:>15>: <p:2d>/<maximo> (<percentual:0 casas>%)".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/101-mercado-papel-portfolio/solucao_2.saida.txt
"""

PESOS = {"readme": 2, "testes": 3, "ci": 2, "docs": 1, "demo": 2}
repos = {
    "pipeline-rag":   {"readme": True,  "testes": True,  "ci": True,  "docs": True,  "demo": False},
    "demo-agente":    {"readme": True,  "testes": False, "ci": False, "docs": False, "demo": True},
    "scripts-soltos": {"readme": False, "testes": False, "ci": False, "docs": False, "demo": False},
}

# TODO: implemente pontuar(repo) e imprima o ranking ponderado dos repositorios.
