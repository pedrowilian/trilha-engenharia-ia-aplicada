---
id: licao-066-function-calling-tool-use
ordinal: 66
modulo: M08-agentes-autonomos
titulo: "Function calling / tool use"
slug: function-calling-tool-use
pre_requisitos:
  - licao-054-saidas-estruturadas-json-mode
  - licao-062-arquitetura-de-agentes
tempo_estimado_min: 55
objetivos_de_aprendizagem:
  - "Descrever um esquema de ferramenta (nome, descrição, parâmetros) e serializá-lo"
  - "Despachar uma tool-call para a função registrada correspondente"
  - "Garantir o round-trip tool-call → JSON → tool-call com igualdade exata"
competencias:
  - req-agentes
  - req-verificacao-saidas
classificacao_ementa: "coberto pela ementa"
conceitos_centrais:
  - esquema-de-ferramenta
  - despacho-de-tool-call
  - round-trip-tool-call-json
envolve_parsing_serializacao: true
---

# Lição 066 — Function calling / tool use

> **Módulo:** M08 — Agentes Autônomos · **Ordem de estudo:** 66 · **Tempo:** ~55 min
> **Pré-requisitos:** [054] Saídas estruturadas e JSON mode · [062] Arquitetura de agentes
> **Classificação:** coberto pela ementa

> **Convenção de formatação:** matemática em LaTeX (`$...$` inline, `$$...$$` em
> destaque, render nativo na pré-visualização do VS Code); figuras reprodutíveis
> geradas por `tools/figuras/gerar_figuras_m08.py` e incorporadas por caminho
> relativo `assets/<NNN>-<slug>/<nome>.png`; blocos ```python só para código e
> saída.

## Seção_Teórica

### Motivação

Um agente só é útil quando consegue **agir no mundo**: consultar um banco, chamar
uma API, rodar um cálculo. **Function calling** (ou *tool use*) é o mecanismo que
liga a saída do modelo a funções reais do seu programa. O modelo não executa nada —
ele apenas **descreve**, em formato estruturado, qual função chamar e com quais
argumentos; o seu código é quem **executa** de fato. Para que isso funcione com
segurança, três coisas precisam estar firmes: o modelo precisa conhecer o
**esquema** de cada ferramenta (nome e parâmetros), o seu código precisa
**despachar** a chamada corretamente, e a tool-call precisa **trafegar como JSON**
sem corromper-se. Esta última garantia — o **round-trip** sem perda — é a ponte
direta com a Lição 054 e a base do protocolo MCP (Módulo M09).

### Princípio de funcionamento

O ciclo de function calling tem quatro momentos. (1) **Declaração:** você envia ao
modelo o esquema das ferramentas — para cada uma, `name`, `description` e
`parameters` tipados. (2) **Emissão:** em vez de texto livre, o modelo devolve uma
**tool-call** estruturada, por exemplo $\{\text{name}, \text{arguments}\}$. (3)
**Despacho:** seu código encontra a função pelo `name` e a invoca com `arguments`.
(4) **Retorno:** o resultado volta ao modelo como observação (fechando o laço do
agente, como na Lição 063).

A correção depende de a tool-call sobreviver à serialização. Sendo $S$ a
serialização (`json.dumps`) e $P$ o parsing (`json.loads`), exigimos o **round-trip
exato**:

$$P(S(x)) = x \quad\text{e}\quad S(P(S(x))) = S(x).$$

Com `sort_keys=True`, a string serializada fica **canônica** e pode ser comparada
por igualdade — o que nos permite detectar qualquer divergência (chave perdida,
tipo alterado) imediatamente.

---

### Conceito central 1 — Esquema de ferramenta

A ferramenta é descrita por um dicionário com nome, descrição e parâmetros tipados.
Serializá-lo de forma canônica (`sort_keys=True`) é como ele é anunciado ao modelo.

#### Exemplo_Resolvido 1.1

```python
import json
# Esquema de uma ferramenta: nome, descricao e parametros tipados.
esquema = {
    "name": "soma",
    "description": "Soma dois inteiros",
    "parameters": {"a": "integer", "b": "integer"},
}
print(json.dumps(esquema, ensure_ascii=False, sort_keys=True))
```

**Explicação passo a passo:**
- **Bloco 1 (`esquema`):** descreve a ferramenta `soma` com dois parâmetros inteiros — o contrato que o modelo deve respeitar ao chamá-la.
- **Bloco 2 (`json.dumps`):** com `sort_keys=True`, as chaves saem em ordem alfabética (`description`, `name`, `parameters`), tornando a saída canônica e comparável.

**Saída esperada:**
```
{"description": "Soma dois inteiros", "name": "soma", "parameters": {"a": "integer", "b": "integer"}}
```

---

### Conceito central 2 — Despacho de tool-call

Recebida a tool-call, o agente precisa encontrar a função certa e chamá-la com os
argumentos. Um **registro** (dicionário nome → função) torna o despacho direto e
seguro.

#### Exemplo_Resolvido 2.1

```python
# Despacho: mapeia uma tool-call para a funcao registrada e executa.
registro = {
    "soma": lambda a, b: a + b,
    "maior": lambda a, b: max(a, b),
}

def despachar(tool_call):
    fn = registro[tool_call["name"]]
    return fn(**tool_call["arguments"])

chamadas = [
    {"name": "soma", "arguments": {"a": 2, "b": 3}},
    {"name": "maior", "arguments": {"a": 7, "b": 4}},
]
for tc in chamadas:
    print(tc["name"], "->", despachar(tc))
```

**Explicação passo a passo:**
- **Bloco 1 (`registro`):** associa cada nome de ferramenta à sua implementação real.
- **Bloco 2 (`despachar`):** busca a função pelo `name` e a invoca expandindo `arguments` como argumentos nomeados (`**`).
- **Bloco 3 (laço):** despacha duas chamadas; os argumentos nomeados casam exatamente com a assinatura das funções.

**Saída esperada:**
```
soma -> 5
maior -> 7
```

---

### Conceito central 3 — Round-trip tool-call → JSON → tool-call

A tool-call trafega como JSON entre o modelo e o seu código. A propriedade de
corretude é o **round-trip exato**: serializar e re-parsear deve devolver uma
estrutura **idêntica** à original — inclusive os tipos (`True` ↔ `true`).

#### Exemplo_Resolvido 3.1

```python
import json
# Round-trip: tool-call dict -> JSON -> dict, com igualdade exata.
tool_call = {
    "name": "buscar",
    "arguments": {"query": "clima", "cidade": "Recife", "limite": 3},
}
ida = json.dumps(tool_call, ensure_ascii=False, sort_keys=True)
volta = json.loads(ida)
print("json:", ida)
print("igual?", volta == tool_call)
print("re-serializa identico?", json.dumps(volta, ensure_ascii=False, sort_keys=True) == ida)
```

**Explicação passo a passo:**
- **Bloco 1 (`tool_call`):** uma chamada com argumentos aninhados de tipos variados (texto e inteiro).
- **Bloco 2 (`ida`/`volta`):** serializa de forma canônica e parseia de volta.
- **Bloco 3 (`print`):** `igual?` é `True` (a estrutura foi preservada) e a re-serialização reproduz a mesma string — o round-trip não perdeu nada.

**Saída esperada:**
```
json: {"arguments": {"cidade": "Recife", "limite": 3, "query": "clima"}, "name": "buscar"}
igual? True
re-serializa identico? True
```

## Seção_Prática

> **Como reproduzir:** execute cada solução de referência com
> `python trilha/solucoes/066-function-calling-tool-use/solucao_<n>.py` e compare
> a saída com o arquivo `.saida.txt` correspondente. Os enunciados/esqueletos
> ficam em `trilha/pratica/066-function-calling-tool-use/exercicio_<n>.py`.

### Exercício 1 — Esquema de ferramenta
- **Entrada inicial / setup:** a ferramenta `multiplicar` (parâmetros `x` e `y`, tipo `number`).
- **Passos de execução:** monte o dicionário `esquema` com `name`, `description` e `parameters`; imprima `json.dumps(esquema, ensure_ascii=False, sort_keys=True)`, depois `nome: {name}` e `parametros: {lista ordenada}`.
- **Critério de conclusão (binário):** a saída é **exatamente** igual a `solucao_1.saida.txt`; qualquer divergência reprova.
- **Solução de referência:** `trilha/solucoes/066-function-calling-tool-use/solucao_1.py`
- **Saída esperada:** `trilha/solucoes/066-function-calling-tool-use/solucao_1.saida.txt`

### Exercício 2 — Despacho de tool-call
- **Entrada inicial / setup:** `registro = {"concat": ..., "repetir": ...}` e a lista `chamadas` com duas tool-calls.
- **Passos de execução:** implemente `despachar(tool_call)` (busca por `name`, chama com `**arguments`); imprima `{name} -> {resultado}` por chamada.
- **Critério de conclusão (binário):** a saída é **exatamente** igual a `solucao_2.saida.txt` (`repetir -> xyxyxy`); qualquer divergência reprova.
- **Solução de referência:** `trilha/solucoes/066-function-calling-tool-use/solucao_2.py`
- **Saída esperada:** `trilha/solucoes/066-function-calling-tool-use/solucao_2.saida.txt`

### Exercício 3 — Round-trip tool-call → JSON → tool-call (ida-e-volta com igualdade exata)
- **Entrada inicial / setup:** a tool-call aninhada `tool_call = {"name": "agendar", "arguments": {"dia": "segunda", "hora": 9, "lembrete": True}}`.
- **Passos de execução:** serialize com `json.dumps(..., ensure_ascii=False, sort_keys=True)`, parseie de volta com `json.loads` e verifique a **igualdade exata** (`volta == tool_call`); imprima `json:`, `igual?` e `re-serializa identico?`.
- **Critério de conclusão (binário):** a saída é **exatamente** igual a `solucao_3.saida.txt` e, em particular, `igual? True` (round-trip sem perda; `True` ↔ `true`); qualquer divergência reprova.
- **Solução de referência:** `trilha/solucoes/066-function-calling-tool-use/solucao_3.py`
- **Saída esperada:** `trilha/solucoes/066-function-calling-tool-use/solucao_3.saida.txt`
