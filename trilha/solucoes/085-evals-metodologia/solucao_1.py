"""Solucao de referencia - Exercicio 1 da Licao 085.

Harness de eval com metrica de exact match: roda o sistema sob teste sobre um
dataset rotulado e reporta a accuracy. O sistema-stub tem um bug proposital
(divisao inteira) que o eval expoe de forma reprodutivel.
"""


def normalizar(s):
    return s.strip().lower()


dataset = [
    ("2 + 2", "4"),
    ("3 * 3", "9"),
    ("10 - 4", "6"),
    ("5 / 2", "2.5"),
    ("7 + 8", "15"),
]


def sistema(expr):
    # avaliador-stub deterministico; "5 / 2" retorna "2" (bug de divisao inteira).
    tabela = {"2 + 2": "4", "3 * 3": "9", "10 - 4": "6", "5 / 2": "2", "7 + 8": "15"}
    return tabela.get(expr.strip(), "?")


def exact_match(previsto, esperado):
    return normalizar(previsto) == normalizar(esperado)


acertos = 0
for expr, esperado in dataset:
    previsto = sistema(expr)
    ok = exact_match(previsto, esperado)
    acertos += int(ok)
    print(f"{expr}: previsto={previsto!r} esperado={esperado!r} ok={ok}")

acc = acertos / len(dataset)
print(f"accuracy: {acc:.4f} ({acertos}/{len(dataset)})")
