# Capstone — Micro-SaaS de Suporte (RAG + Agente + MCP)

Projeto integrador do Módulo M15. É um **Micro-SaaS de suporte** determinístico
e **offline** (sem rede e sem LLM real) que integra, num único fluxo ponta a
ponta, os três componentes centrais da trilha:

- **RAG** — recuperação em memória sobre um corpus minúsculo de documentos de suporte;
- **Agente** — laço de decisão que escolhe e invoca ferramentas (uma delas consulta o RAG);
- **MCP** — servidor/cliente no estilo Model Context Protocol que expõe a capacidade do agente como ferramenta.

O objetivo do capstone é **consolidar**: cada componente já foi estudado
isoladamente; aqui eles cooperam e cada execução **emite evidência observável**
que permite verificar, de forma binária, que o componente participou.

## Como executar

```bash
# Fluxo completo, imprime a evidência de cada componente e sai com código 0:
python3 trilha/capstone/src/main.py

# Teste de integração (RAG + agente + MCP, com detecção de componente ausente):
python3 -m pytest trilha/capstone/tests/
```

## Arquitetura (fluxo de dados)

```
pergunta
   │
   ▼
ClienteMcp ──tools/list──▶ ServidorMcp        (descoberta de ferramentas)
   │                          │
   └────tools/call───────────▶│
                              ▼
                           Agente ──escolhe ferramenta──▶ buscar_documentos
                              │                                  │
                              │                                  ▼
                              │                            RagEmMemoria.recuperar
                              ▼                                  │
                           resposta ◀──────observação───────────┘
```

O `MicroSaaS` (em `src/pipeline.py`) compõe os quatro objetos e devolve, além
da resposta, uma `EvidenciaFluxo` com os contadores de cada componente.

## Estrutura

| Arquivo | Componente | Responsabilidade |
|---|---|---|
| `src/rag.py` | RAG | índice em memória + recuperação por cosseno (determinística) |
| `src/agent.py` | Agente | laço ReAct + registro/uso de ferramentas |
| `src/mcp_server.py` | MCP | registro e despacho de ferramentas (JSON-RPC simplificado) |
| `src/mcp_client.py` | MCP | descoberta (`tools/list`) e invocação (`tools/call`) |
| `src/pipeline.py` | Integração | compõe os três componentes e agrega evidência |
| `src/main.py` | Entrada | executa o fluxo e imprime a evidência |
| `tests/test_integracao.py` | Verificação | exercita os três componentes + detecção de ausência |

## Critérios de conclusão (verificáveis por componente)

Cada critério tem um **resultado esperado observável** e um **método de
verificação** explícito. O capstone só é considerado concluído quando **todos**
os critérios passam.

### Componente RAG

- **C-RAG-1 — Recuperação relevante.**
  - *Resultado esperado:* para a pergunta "Como redefinir minha senha?", o
    documento top-1 é `doc-senha` com score > 0.
  - *Verificação:* `main.py` imprime `[RAG] consultas=1 top=doc-senha score=0.4364`;
    o teste `test_evidencia_rag_recuperou_documento_relevante` asserta `top_id == "doc-senha"`
    e `score > 0`.
- **C-RAG-2 — Determinismo.**
  - *Resultado esperado:* a mesma pergunta produz sempre o mesmo top-1 e o mesmo score.
  - *Verificação:* duas execuções de `main.py` produzem saída idêntica (sem RNG/rede).

### Componente Agente

- **C-AGT-1 — Uso de ferramenta.**
  - *Resultado esperado:* o agente executa ≥ 1 passo e usa a ferramenta `buscar_documentos`.
  - *Verificação:* `main.py` imprime `[AGENTE] passos=1 ferramentas=buscar_documentos`;
    o teste `test_evidencia_agente_usou_ferramenta` asserta `passos >= 1` e o uso da ferramenta.
- **C-AGT-2 — Seleção de ferramenta por política.**
  - *Resultado esperado:* perguntas com "quantos" selecionam `contar_documentos`.
  - *Verificação:* `test_evidencia_agente_seleciona_ferramenta_de_contagem`
    asserta `ferramentas_usadas == ["contar_documentos"]`.

### Componente MCP

- **C-MCP-1 — Descoberta e invocação.**
  - *Resultado esperado:* o servidor registra ≥ 1 ferramenta e atende ≥ 2 chamadas
    (uma `tools/list` + uma `tools/call`), terminando em `tools/call`.
  - *Verificação:* `main.py` imprime `[MCP] ferramentas_registradas=1 chamadas=2 metodo=tools/call`;
    o teste `test_evidencia_mcp_lista_e_invoca_ferramenta` asserta esses contadores.
- **C-MCP-2 — Erro em ferramenta inexistente.**
  - *Resultado esperado:* invocar uma ferramenta não registrada levanta erro explícito.
  - *Verificação:* `test_detecta_chamada_a_ferramenta_inexistente` espera `RuntimeError`.

### Integração

- **C-INT-1 — Fluxo completo.**
  - *Resultado esperado:* os três componentes executam (`completo() == True`).
  - *Verificação:* `main.py` imprime `RESULTADO: fluxo completo` e sai com código 0;
    `test_fluxo_completo_executa_os_tres_componentes` asserta
    `componentes_executados() == {"rag": True, "agente": True, "mcp": True}`.
- **C-INT-2 — Detecção de componente ausente.**
  - *Resultado esperado:* se o MCP não for acionado, o fluxo é detectado incompleto.
  - *Verificação:* `test_detecta_componente_mcp_ausente` asserta `completo() == False`
    com `mcp_chamadas = 0`.
