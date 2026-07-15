"""Solução de referência — Exercício 3 da Lição 079.

Monitora (de forma simulada) a curva de perda por passo de treino, chega ao
status final e usa o modelo ajustado para uma resposta determinística.
"""


def monitorar(passos, perda_inicial=2.0, decaimento=0.8):
    eventos = []
    perda = perda_inicial
    for passo in range(1, passos + 1):
        eventos.append((passo, round(perda, 4)))
        perda *= decaimento
    return eventos, "succeeded", "ft:base-mini:org::abc123"


eventos, status, modelo = monitorar(4)
for passo, perda in eventos:
    print(f"passo {passo}: train_loss={perda}")
print("status final:", status)
print("modelo ajustado:", modelo)


def responder(modelo, pergunta):
    return f"[{modelo}] -> {pergunta.upper()}"


print(responder(modelo, "ola mundo"))
