"""Solução de referência — Exercício 1 da Lição 052.

Monta um prompt a partir das suas partes anatômicas (sistema, instrução,
contexto, consulta), cada uma rotulada, e conta as linhas resultantes.
"""


def montar_prompt(sistema, instrucao, contexto, consulta):
    partes = [
        f"[SISTEMA] {sistema}",
        f"[INSTRUCAO] {instrucao}",
        f"[CONTEXTO] {contexto}",
        f"[CONSULTA] {consulta}",
    ]
    return "\n".join(partes)


prompt = montar_prompt(
    "Voce e um assistente juridico.",
    "Responda apenas com base no contexto.",
    "O contrato vence em 30 dias.",
    "Quando vence o contrato?",
)
print(prompt)
print("linhas:", len(prompt.splitlines()))
