"""Solução de referência — Exercício 3 da Lição 053.

Decomposição de tarefa: uma tarefa complexa é quebrada em subtarefas
independentes (contar, transformar, reordenar) e os resultados são combinados
num relatório.
"""


def n_palavras(texto):
    return len(texto.split())


def maiusculas(texto):
    return texto.upper()


def inverter_ordem(texto):
    return " ".join(reversed(texto.split()))


frase = "engenharia de ia aplicada"
sub = {
    "n_palavras": n_palavras(frase),
    "maiusculas": maiusculas(frase),
    "invertida": inverter_ordem(frase),
}
for chave in ["n_palavras", "maiusculas", "invertida"]:
    print(f"{chave}: {sub[chave]}")
