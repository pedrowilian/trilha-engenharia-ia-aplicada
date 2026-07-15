"""Exercicio 1 - Harness de eval com exact match.

Setup (dado):
    dataset = [
        ("2 + 2", "4"),
        ("3 * 3", "9"),
        ("10 - 4", "6"),
        ("5 / 2", "2.5"),
        ("7 + 8", "15"),
    ]
    sistema(expr) consulta uma tabela fixa (com um bug em "5 / 2" -> "2").

Tarefa:
    Implemente normalizar(s), exact_match(previsto, esperado) e rode o harness
    sobre o dataset. Para cada item imprima
    "<expr>: previsto=<repr> esperado=<repr> ok=<bool>" e, ao final,
    "accuracy: <4 casas> (<acertos>/<total>)".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/085-evals-metodologia/solucao_1.saida.txt
"""

dataset = [
    ("2 + 2", "4"),
    ("3 * 3", "9"),
    ("10 - 4", "6"),
    ("5 / 2", "2.5"),
    ("7 + 8", "15"),
]


def sistema(expr):
    tabela = {"2 + 2": "4", "3 * 3": "9", "10 - 4": "6", "5 / 2": "2", "7 + 8": "15"}
    return tabela.get(expr.strip(), "?")


# TODO: implemente normalizar/exact_match e rode o harness imprimindo a accuracy.
