"""Solução de referência — Exercício 3 da Lição 070.

Prevenção de loop descontrolado: para por repetição da mesma ação (3x seguidas)
ou por limite de passos. Determinístico.
"""


def executar(acoes, max_passos=5):
    vistos = []
    for i, acao in enumerate(acoes, 1):
        if i > max_passos:
            return f"parou: limite de {max_passos} passos"
        if vistos[-2:] == [acao, acao]:
            return f"parou: acao repetida '{acao}'"
        vistos.append(acao)
    return "concluiu sem incidentes"


print(executar(["a", "b"]))
print(executar(["z", "z", "z"]))
print(executar(["a", "b", "c", "d", "e", "f"]))
