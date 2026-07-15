"""Solução de referência — Exercício 1 da Lição 046.

Constrói a máscara de perda do SFT: 0 nos tokens do prompt (até <|assistant|>
inclusive) e 1 nos tokens da resposta.
"""
tokens = ["<|user|>", "Some", "2", "e", "3", "<|assistant|>", "5", "<|end|>"]

mascara = []
em_resposta = False
for tok in tokens:
    if em_resposta:
        mascara.append(1)
    else:
        mascara.append(0)
    if tok == "<|assistant|>":
        em_resposta = True

print("tokens:", tokens)
print("mascara:", mascara)
print("tokens de resposta:", sum(mascara))
