---
id: licao-063-react
ordinal: 63
modulo: M08-agentes-autonomos
titulo: "Padrão ReAct (reason + act)"
slug: react
pre_requisitos:
  - licao-062-arquitetura-de-agentes
tempo_estimado_min: 50
objetivos_de_aprendizagem:
  - "Explicar o padrão ReAct e o ciclo Thought → Action → Observation"
  - "Parsear a ação emitida por um agente no formato ferramenta[args]"
  - "Implementar um laço ReAct determinístico que termina em uma resposta final"
competencias:
  - req-agentes
classificacao_ementa: "coberto pela ementa"
conceitos_centrais:
  - traco-thought-action-observation
  - parsing-da-acao
  - laco-react-ate-resposta-final
envolve_parsing_serializacao: false
---

# Lição 063 — Padrão ReAct (reason + act)

> **Módulo:** M08 — Agentes Autônomos · **Ordem de estudo:** 63 · **Tempo:** ~50 min
> **Pré-requisitos:** [062] Arquitetura de agentes
> **Classificação:** coberto pela ementa

> **Convenção de formatação:** matemática em LaTeX (`$...$` inline, `$$...$$` em
> destaque, render nativo na pré-visualização do VS Code); figuras reprodutíveis
> geradas por `tools/figuras/gerar_figuras_m08.py` e incorporadas por caminho
> relativo `assets/<NNN>-<slug>/<nome>.png`; blocos ```python só para código e
> saída.

## Seção_Teórica

### Motivação

Na Lição 062 vimos o esqueleto do laço de um agente, mas o *planner* era uma regra
fixa em Python. Em um agente real, quem decide a próxima ação é o **modelo de
linguagem** — e ele decide gerando **texto**. Surge então um problema concreto: como
transformar o texto livre do modelo em uma ação executável, e como dar ao modelo o
**resultado** dessa ação para que ele continue raciocinando? O padrão **ReAct**
(*Reasoning + Acting*) responde a isso com um protocolo simples e robusto: o modelo
**alterna** passos de raciocínio (`Thought`) e passos de ação (`Action`), e o
ambiente devolve uma **observação** (`Observation`) após cada ação. Esse
entrelaçamento de pensar e agir é a base prática da maioria dos agentes de
ferramentas hoje em dia.

### Princípio de funcionamento

O ReAct estrutura a saída do modelo numa sequência repetida de três campos:

$$\underbrace{\text{Thought}}_{\text{raciocínio}} \rightarrow \underbrace{\text{Action}}_{\text{chamada de ferramenta}} \rightarrow \underbrace{\text{Observation}}_{\text{resultado}} \rightarrow \cdots \rightarrow \text{Final Answer}$$

A cada iteração, o **Thought** explicita o raciocínio (o que fazer e por quê); a
**Action** nomeia uma ferramenta e seus argumentos (por exemplo, `soma[2, 3]`); a
**Observation** é o que o sistema devolve depois de executar a ferramenta. Esse
resultado é **concatenado de volta ao contexto**, de modo que o próximo Thought
"enxerga" tudo que já aconteceu. O laço termina quando o modelo, em vez de uma
Action, emite uma **Final Answer**. O sistema que roda o agente precisa de duas
peças: um **parser** que extrai a ferramenta e os argumentos do texto da Action, e
um **dispatcher** (executor) que chama a ferramenta correspondente — exatamente os
componentes da lição anterior, agora guiados pelo texto do modelo.

---

### Conceito central 1 — Traço Thought / Action / Observation

O **traço** é o registro estruturado do que o agente pensou, fez e observou. Mantê-lo
explícito é essencial para depurar o agente e para alimentar o próximo passo de
raciocínio. Aqui representamos cada passo como um dicionário.

#### Exemplo_Resolvido 1.1

```python
# Um passo ReAct: Thought -> Action -> Observation, registrado num traco.
traco = [
    {"thought": "Preciso somar 2 e 3", "action": "soma[2,3]", "observation": "5"},
    {"thought": "Agora multiplico por 4", "action": "produto[5,4]", "observation": "20"},
]
for i, passo in enumerate(traco, 1):
    print(f"Passo {i}")
    print(f"  Thought: {passo['thought']}")
    print(f"  Action: {passo['action']}")
    print(f"  Observation: {passo['observation']}")
```

**Explicação passo a passo:**
- **Bloco 1 (`traco`):** lista de passos; cada passo guarda o pensamento, a ação textual e a observação devolvida.
- **Bloco 2 (laço de impressão):** percorre o traço numerando os passos e exibe os três campos do protocolo ReAct de forma legível.

**Saída esperada:**
```
Passo 1
  Thought: Preciso somar 2 e 3
  Action: soma[2,3]
  Observation: 5
Passo 2
  Thought: Agora multiplico por 4
  Action: produto[5,4]
  Observation: 20
```

---

### Conceito central 2 — Parsing da ação

O modelo escreve a ação como **texto** (`soma[2, 3]`). O sistema precisa
**parsear** esse texto para descobrir qual ferramenta chamar e com quais
argumentos. Uma expressão regular simples resolve o formato `ferramenta[args]`, e
entradas fora do formato devem ser tratadas (aqui, retornando `None`).

#### Exemplo_Resolvido 2.1

```python
import re

def parse_acao(texto):
    m = re.match(r"(\w+)\[(.*)\]$", texto.strip())
    if not m:
        return None
    nome = m.group(1)
    args = [a.strip() for a in m.group(2).split(",") if a.strip()]
    return nome, args

for s in ["soma[2, 3]", "busca[clima, recife]", "invalido"]:
    print(s, "->", parse_acao(s))
```

**Explicação passo a passo:**
- **Bloco 1 (`parse_acao`):** a regex captura o nome (`\w+`) e o conteúdo entre colchetes; se não casar, devolve `None` (ação malformada).
- **Bloco 2 (split dos argumentos):** separa por vírgula e remove espaços, descartando argumentos vazios.
- **Bloco 3 (laço de teste):** mostra duas ações válidas (com 2 argumentos cada) e uma inválida (`invalido`), que vira `None`.

**Saída esperada:**
```
soma[2, 3] -> ('soma', ['2', '3'])
busca[clima, recife] -> ('busca', ['clima', 'recife'])
invalido -> None
```

---

### Conceito central 3 — Laço ReAct até a resposta final

Juntando tudo: um laço que, a cada passo, obtém um Thought e uma Action do "modelo"
(aqui, uma política determinística), executa a ferramenta, registra a Observation e
realimenta a memória — até o modelo emitir `Final Answer`.

#### Exemplo_Resolvido 3.1

```python
# Laco ReAct: alterna raciocinio e acao ate emitir "Final Answer".
ferramentas = {
    "soma": lambda a, b: a + b,
    "produto": lambda a, b: a * b,
}

def politica(passo, memoria):
    if passo == 0:
        return ("Preciso somar 2 e 3", "soma", (2, 3))
    if passo == 1:
        parcial = memoria[-1]
        return ("Multiplico o resultado por 4", "produto", (parcial, 4))
    return ("Tenho a resposta", "final", (memoria[-1],))

memoria = []
passo = 0
while True:
    pensamento, acao, args = politica(passo, memoria)
    print(f"Thought: {pensamento}")
    if acao == "final":
        print(f"Final Answer: {args[0]}")
        break
    obs = ferramentas[acao](*args)
    memoria.append(obs)
    print(f"Action: {acao}{args}")
    print(f"Observation: {obs}")
    passo += 1
```

**Explicação passo a passo:**
- **Bloco 1 (`ferramentas`):** a toolbox de cálculo, indexada por nome.
- **Bloco 2 (`politica`):** o "modelo" determinístico que, em cada passo, devolve um pensamento, uma ação e seus argumentos — usando a memória para encadear resultados.
- **Bloco 3 (laço):** imprime o Thought; se a ação é `final`, emite a Final Answer e para; caso contrário, executa a ferramenta, guarda a observação na memória e a imprime, fechando o ciclo ReAct.

**Saída esperada:**
```
Thought: Preciso somar 2 e 3
Action: soma(2, 3)
Observation: 5
Thought: Multiplico o resultado por 4
Action: produto(5, 4)
Observation: 20
Thought: Tenho a resposta
Final Answer: 20
```

## Seção_Prática

> **Como reproduzir:** execute cada solução de referência com
> `python trilha/solucoes/063-react/solucao_<n>.py` e compare a saída com o
> arquivo `.saida.txt` correspondente. Os enunciados/esqueletos ficam em
> `trilha/pratica/063-react/exercicio_<n>.py`.

### Exercício 1 — Formatar um traço ReAct
- **Entrada inicial / setup:** a lista `traco` com três passos (chaves `thought`, `action`, `observation`).
- **Passos de execução:** para cada passo numerado a partir de 1, imprima `{i}. Thought: {thought} | Action: {action} | Observation: {observation}`; ao final, imprima `total de passos: {n}`.
- **Critério de conclusão (binário):** a saída é **exatamente** igual a `solucao_1.saida.txt` (`total de passos: 3`); qualquer divergência reprova.
- **Solução de referência:** `trilha/solucoes/063-react/solucao_1.py`
- **Saída esperada:** `trilha/solucoes/063-react/solucao_1.saida.txt`

### Exercício 2 — Parsear a ação
- **Entrada inicial / setup:** ações no formato `ferramenta[arg1, arg2, ...]`; casos `["soma[1, 2, 3]", "kb[capital]", "ruim"]`.
- **Passos de execução:** implemente `parse_acao(texto)` devolvendo `(nome, args)` (lista de argumentos sem espaços) ou `("?", [])` para texto fora do formato; imprima `{texto!r} -> nome={nome} args={args}` por caso.
- **Critério de conclusão (binário):** a saída é **exatamente** igual a `solucao_2.saida.txt` (a ação `ruim` vira `nome=? args=[]`); qualquer divergência reprova.
- **Solução de referência:** `trilha/solucoes/063-react/solucao_2.py`
- **Saída esperada:** `trilha/solucoes/063-react/solucao_2.saida.txt`

### Exercício 3 — Laço ReAct até a resposta final
- **Entrada inicial / setup:** `ferramentas = {"sub": ..., "soma": ...}` e a política determinística que resolve `(10 - 4) + 1` (ver esqueleto).
- **Passos de execução:** implemente o laço que imprime `Thought: ...`; quando a ação for `final`, imprime `Final Answer: {valor}` e encerra; senão executa a ferramenta, guarda a observação em `memoria` e imprime `Action: {acao}{args}` e `Observation: {obs}`.
- **Critério de conclusão (binário):** a saída é **exatamente** igual a `solucao_3.saida.txt` (termina em `Final Answer: 7`); qualquer divergência reprova.
- **Solução de referência:** `trilha/solucoes/063-react/solucao_3.py`
- **Saída esperada:** `trilha/solucoes/063-react/solucao_3.saida.txt`
