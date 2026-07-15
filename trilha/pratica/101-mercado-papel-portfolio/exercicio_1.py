"""Exercicio 1 - Classificar perfis em niveis de senioridade.

Setup (dado):
    perfis = {
        "Eva":   (2, 1, 1),
        "Felix": (3, 3, 2),
        "Gina":  (4, 4, 4),
        "Hugo":  (5, 5, 4),
    }
    Cada tupla e (autonomia, escopo, impacto), de 1 a 5.

Tarefa:
    Implemente nivel_por_score(score) com os cortes:
        score < 1.5 -> "Junior"; < 2.5 -> "Pleno"; < 3.5 -> "Senior";
        < 4.5 -> "Staff"; caso contrario -> "Principal".
    Para cada perfil calcule o score medio das tres dimensoes e imprima
        "<nome>: dims=<tupla> score=<2 casas> -> <nivel>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/101-mercado-papel-portfolio/solucao_1.saida.txt
"""

perfis = {
    "Eva":   (2, 1, 1),
    "Felix": (3, 3, 2),
    "Gina":  (4, 4, 4),
    "Hugo":  (5, 5, 4),
}

# TODO: implemente nivel_por_score(score) e imprima a classificacao de cada perfil.
