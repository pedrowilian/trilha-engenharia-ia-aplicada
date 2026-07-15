"""Exercício 2 — Orçamento de tokens multimodal.

Setup: uma entrada com texto, uma imagem 256x256 (patches 16x16) e 3.0 s de
áudio a 25 quadros/s.

Tarefa:
    Implemente `tokens_texto` (uma palavra = um token), `tokens_imagem`
    (patches quadrados: (altura // patch) * (largura // patch)) e
    `tokens_audio` (um token por quadro: int(duracao_s * taxa_quadros)).
    Calcule e imprima a decomposição e o total, no formato:
        tokens texto : 7
        tokens imagem: 256
        tokens audio : 75
        total        : 338

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/050-genai-multimodais/solucao_2.saida.txt
"""

texto = "transcreva e resuma este clipe de audio"

# TODO: implementar as tres funcoes e imprimir a decomposicao.
