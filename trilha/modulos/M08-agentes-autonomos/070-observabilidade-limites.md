---
id: licao-070-observabilidade-limites
ordinal: 70
modulo: M08-agentes-autonomos
titulo: "Observabilidade e limites de agentes"
slug: observabilidade-limites
pre_requisitos:
  - licao-069-orquestracao-langgraph
tempo_estimado_min: 50
objetivos_de_aprendizagem:
  - "Instrumentar um agente com um traço de execução para observabilidade"
  - "Aplicar guardrails e human-in-the-loop para conter ações perigosas"
  - "Prevenir laços descontrolados por limite de passos e detecção de repetição"
competencias:
  - req-agentes
  - req-deploy-prod
classificacao_ementa: "complemento de aprofundamento à ementa"
conceitos_centrais:
  - tracing-de-execucao
  - guardrails-e-hitl
  - prevencao-de-loop-descontrolado
envolve_parsing_serializacao: false
---

# Lição 070 — Observabilidade e limites de agentes

> **Módulo:** M08 — Agentes Autônomos · **Ordem de estudo:** 70 · **Tempo:** ~50 min
> **Pré-requisitos:** [069] Orquestração com LangGraph
> **Classificação:** complemento de aprofundamento à ementa

> **Convenção de formatação:** matemática em LaTeX (`$...$` inline, `$$...$$` em
> destaque, render nativo na pré-visualização do VS Code); figuras reprodutíveis
> geradas por `tools/figuras/gerar_figuras_m08.py` e incorporadas por caminho
> relativo `assets/<NNN>-<slug>/<nome>.png`; blocos ```python só para código e
> saída.

## Seção_Teórica

### Motivação

Um agente é, por construção, **não determinístico e autônomo**: ele decide os
próprios passos, chama ferramentas e pode iterar muitas vezes. Isso o torna poderoso
e, ao mesmo tempo, perigoso em produção. Sem visibilidade, quando algo dá errado você
não sabe **o que** o agente fez nem **por quê**. Sem limites, um agente pode entrar em
**laço infinito**, gastar dinheiro chamando APIs sem parar, ou executar uma ação
**destrutiva** (apagar dados, transferir valores). Esta lição cobre as duas defesas
essenciais: **observabilidade** — registrar um traço inspecionável de cada execução —
e **limites/guardrails** — regras que restringem o que o agente pode fazer, quando
pedir aprovação humana (*human-in-the-loop*, HITL) e como **garantir terminação**.
São os requisitos mínimos para colocar um agente diante de usuários reais.

### Princípio de funcionamento

**Observabilidade** começa com um **traço** (*trace*): a cada evento relevante (uma
chamada de ferramenta, uma observação, uma decisão), o agente grava um registro
estruturado com índice e metadados. Esse traço permite reconstruir a execução,
medir custo/latência e depurar falhas.

**Guardrails** são checagens aplicadas **antes** de executar uma ação. A política
mais comum é uma *allowlist*: só ações em um conjunto permitido passam; o resto é
**bloqueado**. Ações **sensíveis** (irreversíveis ou caras) exigem **aprovação
humana** antes de rodar — o ponto de HITL.

Por fim, a **terminação** precisa ser garantida. Como o agente decide seus próprios
passos, somam-se duas salvaguardas: um **limite de passos** $N$ (após $N$ iterações,
para incondicionalmente) e a **detecção de repetição** (se o agente repete a mesma
ação várias vezes seguidas, está preso num laço e deve parar). Juntas, elas evitam o
cenário de *runaway loop*.

---

### Conceito central 1 — Tracing de execução

O traço é o registro estruturado do que o agente fez. Cada evento vira um *span* com
índice, tipo e detalhe — a base para depuração e monitoramento.

#### Exemplo_Resolvido 1.1

```python
# Tracing: registra eventos (spans) da execucao do agente para observabilidade.
trace = []
def registrar(evento, detalhe):
    trace.append({"passo": len(trace) + 1, "evento": evento, "detalhe": detalhe})

registrar("tool_call", "busca")
registrar("observacao", "3 resultados")
registrar("resposta", "final")

for s in trace:
    print(f"[{s['passo']}] {s['evento']}: {s['detalhe']}")
print("total de eventos:", len(trace))
```

**Explicação passo a passo:**
- **Bloco 1 (`registrar`):** acrescenta um span ao traço com índice 1-baseado, tipo do evento e detalhe.
- **Bloco 2 (eventos):** registra três momentos típicos de um passo de agente.
- **Bloco 3 (`print`):** imprime o traço de forma legível e o total de eventos — é isso que se envia a uma ferramenta de observabilidade.

**Saída esperada:**
```
[1] tool_call: busca
[2] observacao: 3 resultados
[3] resposta: final
total de eventos: 3
```

---

### Conceito central 2 — Guardrails e HITL

Antes de executar, o agente passa pela checagem dos guardrails: ações fora da
allowlist são bloqueadas, e ações sensíveis exigem aprovação humana. É a barreira que
impede ações perigosas.

#### Exemplo_Resolvido 2.1

```python
# Guardrails + HITL: bloqueia acoes proibidas e exige aprovacao humana para acoes sensiveis.
permitidas = {"buscar", "calcular", "transferir"}
sensiveis = {"transferir"}

def aprovacao_humana(acao):
    return True

def verificar(acao):
    if acao not in permitidas:
        return "bloqueada"
    if acao in sensiveis:
        return "aprovada" if aprovacao_humana(acao) else "negada"
    return "liberada"

for acao in ["buscar", "transferir", "deletar"]:
    print(f"{acao}: {verificar(acao)}")
```

**Explicação passo a passo:**
- **Bloco 1 (`permitidas`/`sensiveis`):** a allowlist e o subconjunto de ações que exigem HITL.
- **Bloco 2 (`verificar`):** bloqueia o que não está na allowlist; submete ações sensíveis à aprovação humana; libera o restante.
- **Bloco 3 (laço):** `buscar` é liberada, `transferir` passa por aprovação (aprovada) e `deletar` (fora da allowlist) é bloqueada.

**Saída esperada:**
```
buscar: liberada
transferir: aprovada
deletar: bloqueada
```

---

### Conceito central 3 — Prevenção de loop descontrolado

A terminação não pode depender só do "bom senso" do agente. Combinamos um limite de
passos com a detecção de ações repetidas para garantir que o agente sempre para.

#### Exemplo_Resolvido 3.1

```python
# Prevencao de loop descontrolado: para por repeticao de acao ou por limite de passos.
def executar(acoes, max_passos=10):
    vistos = []
    for i, acao in enumerate(acoes, 1):
        if i > max_passos:
            return f"parou: limite de {max_passos} passos"
        if vistos[-2:] == [acao, acao]:    # mesma acao 3x seguidas
            return f"parou: acao repetida '{acao}'"
        vistos.append(acao)
    return "concluiu sem incidentes"

print(executar(["a", "b", "c"]))
print(executar(["x", "x", "x", "y"]))
```

**Explicação passo a passo:**
- **Bloco 1 (limite de passos):** se o índice ultrapassa `max_passos`, para incondicionalmente — a salvaguarda de orçamento.
- **Bloco 2 (detecção de repetição):** se as duas ações anteriores forem iguais à atual (três seguidas), declara laço e para.
- **Bloco 3 (testes):** a sequência sem repetição conclui normalmente; a que repete `x` três vezes é interrompida pela detecção de repetição.

**Saída esperada:**
```
concluiu sem incidentes
parou: acao repetida 'x'
```

## Seção_Prática

> **Como reproduzir:** execute cada solução de referência com
> `python trilha/solucoes/070-observabilidade-limites/solucao_<n>.py` e compare a
> saída com o arquivo `.saida.txt` correspondente. Os enunciados/esqueletos ficam
> em `trilha/pratica/070-observabilidade-limites/exercicio_<n>.py`.

### Exercício 1 — Tracing de execução
- **Entrada inicial / setup:** eventos `("inicio", "tarefa")`, `("tool_call", "calc")`, `("fim", "ok")`.
- **Passos de execução:** implemente `registrar(evento, detalhe)` (span com `passo` 1-indexado); imprima cada span como `[{passo}] {evento}: {detalhe}` e `total de eventos: {n}`.
- **Critério de conclusão (binário):** a saída é **exatamente** igual a `solucao_1.saida.txt` (`total de eventos: 3`); qualquer divergência reprova.
- **Solução de referência:** `trilha/solucoes/070-observabilidade-limites/solucao_1.py`
- **Saída esperada:** `trilha/solucoes/070-observabilidade-limites/solucao_1.saida.txt`

### Exercício 2 — Guardrails e HITL
- **Entrada inicial / setup:** `permitidas = {"ler", "escrever", "apagar"}`; `sensiveis = {"apagar"}`; `aprovacao_humana` retorna `True`; ações `["ler", "apagar", "enviar"]`.
- **Passos de execução:** implemente `verificar(acao)` (bloqueada / aprovada-negada / liberada); imprima `{acao}: {resultado}`.
- **Critério de conclusão (binário):** a saída é **exatamente** igual a `solucao_2.saida.txt` (`enviar: bloqueada`); qualquer divergência reprova.
- **Solução de referência:** `trilha/solucoes/070-observabilidade-limites/solucao_2.py`
- **Saída esperada:** `trilha/solucoes/070-observabilidade-limites/solucao_2.saida.txt`

### Exercício 3 — Prevenção de loop descontrolado
- **Entrada inicial / setup:** `executar(acoes, max_passos=5)`; casos `["a", "b"]`, `["z", "z", "z"]`, `["a", "b", "c", "d", "e", "f"]`.
- **Passos de execução:** cheque o limite de passos antes da repetição (3 ações iguais seguidas); retorne a mensagem adequada; imprima o retorno de cada caso.
- **Critério de conclusão (binário):** a saída é **exatamente** igual a `solucao_3.saida.txt` (inclui `parou: acao repetida 'z'` e `parou: limite de 5 passos`); qualquer divergência reprova.
- **Solução de referência:** `trilha/solucoes/070-observabilidade-limites/solucao_3.py`
- **Saída esperada:** `trilha/solucoes/070-observabilidade-limites/solucao_3.saida.txt`
