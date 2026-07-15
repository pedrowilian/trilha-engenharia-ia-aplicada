"""Solução de referência — Exercício 3 da Lição 064.

Replanejamento: quando um passo falha, o agente substitui esse passo pelo plano
alternativo e retoma a execução. Determinístico.
"""


def executar(passo):
    # Falha simulada e determinística apenas para o passo "pagamento".
    return passo != "pagamento"


plano = ["login", "pagamento", "recibo"]
alternativo = {"pagamento": ["pagamento_2fa"]}

i = 0
historico = []
while i < len(plano):
    passo = plano[i]
    ok = executar(passo)
    historico.append((passo, "ok" if ok else "falhou"))
    if not ok:
        plano = plano[:i] + alternativo[passo] + plano[i + 1:]
        continue
    i += 1

for passo, status in historico:
    print(f"{passo}: {status}")
print("plano final:", plano)
