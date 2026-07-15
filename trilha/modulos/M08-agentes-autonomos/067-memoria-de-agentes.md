---
id: licao-067-memoria-de-agentes
ordinal: 67
modulo: M08-agentes-autonomos
titulo: "Memória de agentes (curto/longo prazo)"
slug: memoria-de-agentes
pre_requisitos:
  - licao-058-vector-databases
  - licao-062-arquitetura-de-agentes
tempo_estimado_min: 55
objetivos_de_aprendizagem:
  - "Distinguir memória de curto prazo, de longo prazo e episódica em agentes"
  - "Implementar um buffer de curto prazo de tamanho fixo e uma memória episódica com embeddings"
  - "Recuperar episódios relevantes por similaridade do cosseno (top-k)"
competencias:
  - req-agentes
  - req-rag
classificacao_ementa: "complemento de aprofundamento à ementa"
conceitos_centrais:
  - memoria-curto-prazo
  - memoria-longo-prazo-episodica
  - recuperacao-por-similaridade
envolve_parsing_serializacao: false
---

# Lição 067 — Memória de agentes (curto/longo prazo)

> **Módulo:** M08 — Agentes Autônomos · **Ordem de estudo:** 67 · **Tempo:** ~55 min
> **Pré-requisitos:** [058] Vector databases · [062] Arquitetura de agentes
> **Classificação:** complemento de aprofundamento à ementa

> **Convenção de formatação:** matemática em LaTeX (`$...$` inline, `$$...$$` em
> destaque, render nativo na pré-visualização do VS Code); figuras reprodutíveis
> geradas por `tools/figuras/gerar_figuras_m08.py` e incorporadas por caminho
> relativo `assets/<NNN>-<slug>/<nome>.png`; blocos ```python só para código e
> saída.

## Seção_Teórica

### Motivação

A janela de contexto de um LLM é finita: ela não cabe o histórico inteiro de uma
conversa longa nem todo o conhecimento que o agente acumulou. Sem memória, o agente
"esquece" o que aconteceu há alguns passos e repete erros. A solução é dar ao agente
uma **memória explícita**, gerenciada pelo seu código, com dois níveis. A **memória
de curto prazo** guarda os eventos recentes (o rascunho da tarefa atual) num buffer
pequeno e rápido. A **memória de longo prazo episódica** guarda experiências
passadas como **embeddings** e as recupera por **similaridade** quando são
relevantes para a situação atual — exatamente a técnica de busca vetorial da Lição
058, agora a serviço do agente. Essa combinação deixa o agente focado no presente
sem perder acesso ao passado.

### Princípio de funcionamento

A memória de curto prazo é um **buffer de tamanho fixo** (uma janela deslizante):
quando enche, o evento mais antigo sai para dar lugar ao mais novo. Ela mantém o
contexto imediato barato e atualizado.

A memória episódica de longo prazo guarda cada experiência como um par
$(\text{texto}, \mathbf{v})$, onde $\mathbf{v}$ é o **embedding** do texto. Para
recuperar o que é relevante a uma consulta $\mathbf{q}$, calculamos a **similaridade
do cosseno** com cada episódio e pegamos os $k$ maiores:

$$\text{sim}(\mathbf{q}, \mathbf{v}) = \frac{\mathbf{q} \cdot \mathbf{v}}{\lVert \mathbf{q} \rVert\, \lVert \mathbf{v} \rVert}.$$

Esse $\text{top-}k$ é então injetado no contexto do modelo. Para manter os exemplos
**determinísticos**, usamos embeddings fixos pequenos em vez de um modelo real — a
mecânica de armazenamento e recuperação é idêntica à de um sistema de produção.

---

### Conceito central 1 — Memória de curto prazo

A memória de curto prazo é uma janela dos eventos mais recentes. Um `deque` com
`maxlen` implementa exatamente isso: descarta automaticamente o item mais antigo
quando a capacidade é atingida.

#### Exemplo_Resolvido 1.1

```python
from collections import deque
# Memoria de curto prazo: buffer de tamanho fixo (mantem os ultimos k).
curto = deque(maxlen=3)
for evento in ["a", "b", "c", "d", "e"]:
    curto.append(evento)
    print("buffer:", list(curto))
print("janela final:", list(curto))
```

**Explicação passo a passo:**
- **Bloco 1 (`deque(maxlen=3)`):** cria um buffer que guarda no máximo 3 eventos.
- **Bloco 2 (laço):** ao adicionar o 4º e o 5º eventos, os mais antigos (`a`, `b`) são descartados — a janela "desliza".
- **Bloco 3 (`print` final):** a memória de curto prazo retém apenas os três eventos mais recentes (`c`, `d`, `e`).

**Saída esperada:**
```
buffer: ['a']
buffer: ['a', 'b']
buffer: ['a', 'b', 'c']
buffer: ['b', 'c', 'd']
buffer: ['c', 'd', 'e']
janela final: ['c', 'd', 'e']
```

---

### Conceito central 2 — Memória de longo prazo episódica

A memória de longo prazo guarda experiências como episódios, cada um com seu texto e
o **embedding** correspondente. Armazenar o vetor é o que permite, depois, recuperar
por significado em vez de por palavra exata.

#### Exemplo_Resolvido 2.1

```python
import numpy as np
# Memoria episodica de longo prazo: cada episodio guarda texto + embedding.
memoria = []
def gravar(texto, vetor):
    memoria.append({"texto": texto, "vetor": np.array(vetor, dtype=float)})

gravar("gosto de cafe", [1.0, 0.0, 0.0])
gravar("prefiro cha", [0.0, 1.0, 0.0])
gravar("cafe pela manha", [0.9, 0.0, 0.1])

print("episodios:", len(memoria))
for e in memoria:
    print(e["texto"], "->", e["vetor"].tolist())
```

**Explicação passo a passo:**
- **Bloco 1 (`gravar`):** cada episódio é um dicionário com o texto e seu embedding como `np.array`.
- **Bloco 2 (gravações):** registra três experiências com embeddings fixos (determinísticos).
- **Bloco 3 (`print`):** confirma o número de episódios e exibe o conteúdo de cada um — a base sobre a qual a recuperação vai operar.

**Saída esperada:**
```
episodios: 3
gosto de cafe -> [1.0, 0.0, 0.0]
prefiro cha -> [0.0, 1.0, 0.0]
cafe pela manha -> [0.9, 0.0, 0.1]
```

---

### Conceito central 3 — Recuperação por similaridade

Dada uma consulta, recuperamos os episódios mais parecidos pela similaridade do
cosseno e usamos só os $k$ melhores. É assim que o agente "lembra" do que importa
para a situação atual.

#### Exemplo_Resolvido 3.1

```python
import numpy as np
# Recuperacao por similaridade do cosseno: top-k episodios mais parecidos.
memoria = [
    ("gosto de cafe", np.array([1.0, 0.0, 0.0])),
    ("prefiro cha", np.array([0.0, 1.0, 0.0])),
    ("cafe pela manha", np.array([0.9, 0.0, 0.1])),
]
def cosseno(u, v):
    return float(u @ v / (np.linalg.norm(u) * np.linalg.norm(v)))

consulta = np.array([1.0, 0.0, 0.0])
ranking = sorted(memoria, key=lambda e: cosseno(consulta, e[1]), reverse=True)
for texto, vetor in ranking[:2]:
    print(f"{texto}: {cosseno(consulta, vetor):.3f}")
```

**Explicação passo a passo:**
- **Bloco 1 (`memoria`):** os três episódios com seus embeddings.
- **Bloco 2 (`cosseno`):** similaridade do cosseno entre dois vetores (produto interno normalizado).
- **Bloco 3 (ranking + `print`):** ordena por similaridade decrescente e mostra os 2 episódios mais relevantes; "cafe pela manha" (0.994) supera "prefiro cha" (0.0), embora não compartilhe palavras exatas com a consulta.

**Saída esperada:**
```
gosto de cafe: 1.000
cafe pela manha: 0.994
```

## Seção_Prática

> **Como reproduzir:** execute cada solução de referência com
> `python trilha/solucoes/067-memoria-de-agentes/solucao_<n>.py` e compare a
> saída com o arquivo `.saida.txt` correspondente. Os enunciados/esqueletos
> ficam em `trilha/pratica/067-memoria-de-agentes/exercicio_<n>.py`.

### Exercício 1 — Buffer de curto prazo
- **Entrada inicial / setup:** eventos `["p1", "p2", "p3", "p4"]`; capacidade do buffer `2`.
- **Passos de execução:** use `deque(maxlen=2)`; a cada `append`, imprima `buffer: {lista}`; ao final, imprima `janela final: {lista}`.
- **Critério de conclusão (binário):** a saída é **exatamente** igual a `solucao_1.saida.txt` (`janela final: ['p3', 'p4']`); qualquer divergência reprova.
- **Solução de referência:** `trilha/solucoes/067-memoria-de-agentes/solucao_1.py`
- **Saída esperada:** `trilha/solucoes/067-memoria-de-agentes/solucao_1.saida.txt`

### Exercício 2 — Memória episódica
- **Entrada inicial / setup:** três episódios `("python e linguagem", [1,0,0])`, `("cobra python", [0.8,0.2,0])`, `("cafe quente", [0,0,1])`.
- **Passos de execução:** implemente `gravar(texto, vetor)` (dict com `texto` e `vetor` como `np.array` de float); imprima `episodios: {n}` e, por episódio, `{texto} -> {vetor como lista}`.
- **Critério de conclusão (binário):** a saída é **exatamente** igual a `solucao_2.saida.txt` (`episodios: 3`); qualquer divergência reprova.
- **Solução de referência:** `trilha/solucoes/067-memoria-de-agentes/solucao_2.py`
- **Saída esperada:** `trilha/solucoes/067-memoria-de-agentes/solucao_2.saida.txt`

### Exercício 3 — Recuperação por similaridade (top-k)
- **Entrada inicial / setup:** a memória do exercício 2 e a consulta `np.array([1.0, 0.0, 0.0])`.
- **Passos de execução:** implemente `cosseno(u, v)`; ordene por similaridade decrescente e imprima os 2 mais parecidos como `{texto}: {sim:.3f}`.
- **Critério de conclusão (binário):** a saída é **exatamente** igual a `solucao_3.saida.txt` (`cobra python: 0.970`); qualquer divergência reprova.
- **Solução de referência:** `trilha/solucoes/067-memoria-de-agentes/solucao_3.py`
- **Saída esperada:** `trilha/solucoes/067-memoria-de-agentes/solucao_3.saida.txt`
