"""Solucao de referencia - Exercicio 1 da Licao 101.

Classifica perfis em niveis de senioridade (Junior -> Principal) a partir de um
vetor de competencias (autonomia, escopo, impacto), cada dimensao de 1 a 5. O
nivel sai do score medio: senioridade e sobre autonomia/escopo/impacto, nao
sobre quantidade de codigo.
"""


def nivel_por_score(score):
    if score < 1.5:
        return "Junior"
    elif score < 2.5:
        return "Pleno"
    elif score < 3.5:
        return "Senior"
    elif score < 4.5:
        return "Staff"
    return "Principal"


perfis = {
    "Eva":   (2, 1, 1),
    "Felix": (3, 3, 2),
    "Gina":  (4, 4, 4),
    "Hugo":  (5, 5, 4),
}

for nome, dims in perfis.items():
    score = sum(dims) / len(dims)
    print(f"{nome}: dims={dims} score={score:.2f} -> {nivel_por_score(score)}")
