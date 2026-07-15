"""Solução de referência — Exercício 2 da Lição 050.

Contagem de tokens por modalidade: texto (uma palavra = um token), imagem
(patches quadrados) e áudio (um token por quadro). Imprime a decomposição e o
total — o "orçamento de tokens" de uma entrada multimodal.
"""


def tokens_texto(texto):
    return len(texto.split())


def tokens_imagem(altura, largura, patch):
    return (altura // patch) * (largura // patch)


def tokens_audio(duracao_s, taxa_quadros):
    return int(duracao_s * taxa_quadros)


texto = "transcreva e resuma este clipe de audio"
n_texto = tokens_texto(texto)
n_imagem = tokens_imagem(256, 256, 16)
n_audio = tokens_audio(3.0, 25)
total = n_texto + n_imagem + n_audio

print(f"tokens texto : {n_texto}")
print(f"tokens imagem: {n_imagem}")
print(f"tokens audio : {n_audio}")
print(f"total        : {total}")
