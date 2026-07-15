"""Exercício 1 — Fluxo da requisição pelas camadas.

Setup:
    req = {"token": "ruim", "precisa_contexto": False}
    Três camadas, cada uma anota e devolve uma cópia do dicionário:
      gateway     -> autenticado = (token == "ok")
      orquestracao-> rota = "fluxo_rag" se precisa_contexto, senão "fluxo_direto"
      servicos    -> modelo = "forte" se rota == "fluxo_rag", senão "leve"

Tarefa:
    Aplique as camadas em ordem (gateway -> orquestracao -> servicos) sobre a
    requisição e imprima `autenticado:`, `rota:` e `modelo:`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/084-arquitetura-enterprise/solucao_1.saida.txt
"""

req = {"token": "ruim", "precisa_contexto": False}

# TODO: implemente gateway, orquestracao e servicos e componha o pipeline.
