---
id: licao-082-single-vs-multi-agente
ordinal: 82
modulo: M11-arquitetura-sistemas-ia
titulo: "Single-agent vs multi-agente"
slug: single-vs-multi-agente
pre_requisitos:
  - licao-071-multi-agente
  - licao-081-design-ai-first
tempo_estimado_min: 55
objetivos_de_aprendizagem:
  - "Quantificar o custo de coordenação adicional de uma arquitetura multi-agente"
  - "Comparar a latência sequencial (single) com a latência paralela (multi)"
  - "Decidir entre single-agent e multi-agente a partir de especialização, latência e orçamento"
competencias:
  - req-agentes
classificacao_ementa: "coberto pela ementa"
conceitos_centrais:
  - custo-de-coordenacao
  - latencia-sequencial-vs-paralela
  - criterio-de-decisao
envolve_parsing_serializacao: false
---

# Lição 082 — Single-agent vs multi-agente

> **Módulo:** M11 — Arquitetura de Sistemas com IA · **Ordem de estudo:** 82 · **Tempo:** ~55 min
> **Pré-requisitos:** [071] Sistemas multi-agente · [081] Design AI-First
> **Classificação:** coberto pela ementa

> **Convenção de formatação:** matemática em LaTeX (`$...$` inline, `$$...$$` em
> destaque, render nativo na pré-visualização do VS Code); figuras reprodutíveis
> geradas por `tools/figuras/gerar_figuras_m11.py` e incorporadas por caminho
> relativo `assets/<NNN>-<slug>/<nome>.png`; blocos ```python só para código e
> saída.

## Seção_Teórica

### Motivação

Depois de conhecer os padrões multi-agente (Lição 071), surge a tentação de
**dividir tudo** em vários agentes especializados. Mas multi-agente **não é grátis**:
cada handoff entre agentes consome tokens (o contexto precisa ser re-passado), cada
supervisor adiciona uma rodada de raciocínio, e o sistema fica mais difícil de
depurar. Para muitas tarefas — responder uma pergunta, classificar um ticket — um
**único agente** bem instruído é mais barato, mais rápido e mais simples. A pergunta
de arquitetura, então, não é "single ou multi?" em abstrato, mas **quando o ganho de
especialização e paralelismo supera o custo de coordenação**. Esta lição transforma
essa intuição em **contas que você pode fazer antes de escrever código**.

### Princípio de funcionamento

Comparar as duas arquiteturas exige três modelos quantitativos simples.

O primeiro é o **custo de coordenação**. Num sistema single-agent, o custo é o
trabalho útil: $n$ subtarefas a $t$ tokens cada, ou seja $n\,t$. Num sistema
multi-agente, cada subtarefa vai para um agente diferente, e cada despacho/retorno
adiciona um **overhead de handoff** $h$:

$$C_{\text{multi}} = n\,t + n\,h, \qquad C_{\text{single}} = n\,t$$

O overhead $n\,h$ é o preço da coordenação — cresce linearmente com o número de
subtarefas.

O segundo é a **latência**. O single-agent processa as subtarefas **em sequência**,
então a latência é a **soma** das durações. O multi-agente pode rodar os agentes
**em paralelo**, então a latência é o **máximo** das durações mais um overhead de
coordenação $k$:

$$L_{\text{single}} = \sum_i d_i, \qquad L_{\text{multi}} = \max_i d_i + k$$

Quando as durações são parecidas e numerosas, a paralelização do multi-agente ganha;
quando há uma subtarefa dominante, o ganho some.

O terceiro é o **critério de decisão**. Multi-agente vale a pena quando **três
condições** valem ao mesmo tempo: (1) há **especialização** real (≥ 2 competências
distintas), (2) a latência paralela é **menor** que a sequencial e (3) o custo extra
**cabe** no orçamento. Faltando qualquer uma, o single-agent é a escolha mais
sensata. É a mesma disciplina da Lição 081: só adicione complexidade quando ela paga.

---

### Conceito central 1 — Custo de coordenação

O custo extra do multi-agente é o **overhead de handoff**: cada vez que o supervisor
despacha uma subtarefa e recebe o resultado, há tokens gastos só com coordenação.
Modelar isso explicitamente mostra que o overhead cresce com o número de subtarefas —
e que, para poucas subtarefas, ele pode dominar o orçamento.

#### Exemplo_Resolvido 1.1

```python
# Custo de coordenacao: multi-agente soma um overhead de handoff por subtarefa.
def custo_single(subtarefas, tokens_por_subtarefa):
    return subtarefas * tokens_por_subtarefa

def custo_multi(subtarefas, tokens_por_subtarefa, overhead_handoff):
    return subtarefas * tokens_por_subtarefa + subtarefas * overhead_handoff

for n in [1, 3, 5]:
    s = custo_single(n, 100)
    m = custo_multi(n, 100, 40)
    print(f"subtarefas={n}: single={s} multi={m} overhead={m - s}")
```

**Explicação passo a passo:**
- **Bloco 1 (`custo_single`):** o custo do agente único é só o trabalho útil, $n \cdot t$.
- **Bloco 2 (`custo_multi`):** adiciona $n \cdot h$ — o overhead de handoff de cada despacho/retorno entre agentes.
- **Bloco 3 (laço):** para 1, 3 e 5 subtarefas, o overhead cresce de 40 para 200 tokens; com poucas subtarefas, esse custo extra é uma fração grande do total.

**Saída esperada:**
```
subtarefas=1: single=100 multi=140 overhead=40
subtarefas=3: single=300 multi=420 overhead=120
subtarefas=5: single=500 multi=700 overhead=200
```

---

### Conceito central 2 — Latência sequencial vs paralela

A vantagem do multi-agente é poder rodar subtarefas **em paralelo**. Enquanto o
single-agent paga a **soma** das durações, o multi-agente paga o **máximo** mais um
overhead de coordenação. Com `numpy`, a comparação é direta: `sum` versus `max + k`.

#### Exemplo_Resolvido 2.1

```python
import numpy as np
# Latencia: single processa em sequencia (soma); multi em paralelo (max + overhead).
duracoes = np.array([120, 80, 200, 60])   # ms por subtarefa
coordenacao = 50                          # ms de overhead do supervisor

lat_single = int(duracoes.sum())
lat_multi = int(duracoes.max() + coordenacao)
print("latencia single (sequencial):", lat_single)
print("latencia multi (paralelo):", lat_multi)
print("ganho:", lat_single - lat_multi)
```

**Explicação passo a passo:**
- **Bloco 1 (`duracoes`):** quatro subtarefas com durações diferentes; a mais longa leva 200 ms.
- **Bloco 2 (`lat_single`/`lat_multi`):** o single soma tudo (460 ms); o multi paga o máximo (200 ms) mais 50 ms de coordenação.
- **Bloco 3 (`print`):** o multi-agente economiza 210 ms — o paralelismo compensa porque há várias subtarefas de durações comparáveis.

**Saída esperada:**
```
latencia single (sequencial): 460
latencia multi (paralelo): 250
ganho: 210
```

---

### Conceito central 3 — Critério de decisão

A escolha não é estética: multi-agente vale a pena quando há **especialização**,
**ganho de latência** e o custo extra **cabe no orçamento** — as três coisas ao mesmo
tempo. Codificar esse `AND` numa função evita adotar a arquitetura complexa por moda.

#### Exemplo_Resolvido 3.1

```python
# Decisao single vs multi: multi so vence se especializa E paraleliza E cabe no orcamento.
def decidir(n_competencias, lat_single, lat_multi, custo_extra, orcamento_extra):
    paraleliza = lat_multi < lat_single
    especializa = n_competencias >= 2
    cabe_orcamento = custo_extra <= orcamento_extra
    if especializa and paraleliza and cabe_orcamento:
        return "multi-agente"
    return "single-agente"

casos = [
    ("FAQ simples", 1, 300, 260, 120, 200),
    ("pesquisa+codigo+teste", 3, 600, 280, 150, 200),
    ("relatorio longo", 2, 500, 300, 400, 200),
]
for nome, comp, ls, lm, ce, orc in casos:
    print(f"{nome:>22}: {decidir(comp, ls, lm, ce, orc)}")
```

**Explicação passo a passo:**
- **Bloco 1 (`decidir`):** calcula as três condições e só devolve `multi-agente` quando todas valem (um `AND` explícito).
- **Bloco 2 (`casos`):** cada caso traz competências, latências single/multi, custo extra e orçamento.
- **Bloco 3 (laço):** `FAQ simples` tem 1 competência (não especializa → single); `pesquisa+codigo+teste` satisfaz tudo (→ multi); `relatorio longo` paraleliza e especializa, mas o custo extra (400) estoura o orçamento (200) → single.

**Saída esperada:**
```
           FAQ simples: single-agente
 pesquisa+codigo+teste: multi-agente
       relatorio longo: single-agente
```

## Seção_Prática

> **Como reproduzir:** execute cada solução de referência com
> `python trilha/solucoes/082-single-vs-multi-agente/solucao_<n>.py` e compare a saída
> com o arquivo `.saida.txt` correspondente. Os enunciados/esqueletos ficam em
> `trilha/pratica/082-single-vs-multi-agente/exercicio_<n>.py`.

### Exercício 1 — Custo de coordenação
- **Entrada inicial / setup:** `tokens_por_subtarefa = 80`, `overhead_handoff = 30` e a lista de quantidades `subtarefas ∈ [2, 4, 6]`.
- **Passos de execução:** implemente `custo_single(n, t)` e `custo_multi(n, t, h)` e, para cada `n`, imprima `subtarefas={n}: single={s} multi={m} overhead={m - s}`.
- **Critério de conclusão (binário):** a saída é **exatamente** igual a `solucao_1.saida.txt` (`subtarefas=6: single=480 multi=660 overhead=180`); qualquer divergência reprova.
- **Solução de referência:** `trilha/solucoes/082-single-vs-multi-agente/solucao_1.py`
- **Saída esperada:** `trilha/solucoes/082-single-vs-multi-agente/solucao_1.saida.txt`

### Exercício 2 — Latência sequencial vs paralela
- **Entrada inicial / setup:** `duracoes = [150, 90, 300, 120, 60]` (ms) e `coordenacao = 70` (ms).
- **Passos de execução:** calcule `lat_single` como a soma das durações e `lat_multi` como `max + coordenacao` (use inteiros); imprima `latencia single (sequencial): {ls}`, `latencia multi (paralelo): {lm}` e `ganho: {ls - lm}`.
- **Critério de conclusão (binário):** a saída é **exatamente** igual a `solucao_2.saida.txt` (`ganho: 350`); qualquer divergência reprova.
- **Solução de referência:** `trilha/solucoes/082-single-vs-multi-agente/solucao_2.py`
- **Saída esperada:** `trilha/solucoes/082-single-vs-multi-agente/solucao_2.saida.txt`

### Exercício 3 — Critério de decisão
- **Entrada inicial / setup:** `casos = [("chat suporte", 1, 200, 180, 50, 100), ("rag+sumario", 2, 500, 260, 80, 100), ("pipeline dados", 3, 900, 400, 250, 100)]` (campos: `nome, n_competencias, lat_single, lat_multi, custo_extra, orcamento_extra`).
- **Passos de execução:** implemente `decidir(...)` que devolve `multi-agente` apenas quando há especialização (≥ 2), ganho de latência (`lat_multi < lat_single`) e o custo extra cabe no orçamento; imprima `{nome:>16}: {decisao}`.
- **Critério de conclusão (binário):** a saída é **exatamente** igual a `solucao_3.saida.txt` (`rag+sumario: multi-agente`, demais `single-agente`); qualquer divergência reprova.
- **Solução de referência:** `trilha/solucoes/082-single-vs-multi-agente/solucao_3.py`
- **Saída esperada:** `trilha/solucoes/082-single-vs-multi-agente/solucao_3.saida.txt`
