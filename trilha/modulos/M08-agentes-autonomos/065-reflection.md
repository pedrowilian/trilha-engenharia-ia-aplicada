---
id: licao-065-reflection
ordinal: 65
modulo: M08-agentes-autonomos
titulo: "Padrão Reflection"
slug: reflection
pre_requisitos:
  - licao-063-react
tempo_estimado_min: 50
objetivos_de_aprendizagem:
  - "Explicar o padrão Reflection e o papel do crítico na auto-revisão"
  - "Implementar um ciclo gerar → criticar → revisar determinístico"
  - "Definir um critério de aceitação por qualidade e por limite de iterações"
competencias:
  - req-agentes
classificacao_ementa: "complemento de aprofundamento à ementa"
conceitos_centrais:
  - critico-avaliador
  - ciclo-gerar-criticar-revisar
  - criterio-de-aceitacao
envolve_parsing_serializacao: false
---

# Lição 065 — Padrão Reflection

> **Módulo:** M08 — Agentes Autônomos · **Ordem de estudo:** 65 · **Tempo:** ~50 min
> **Pré-requisitos:** [063] Padrão ReAct (reason + act)
> **Classificação:** complemento de aprofundamento à ementa

> **Convenção de formatação:** matemática em LaTeX (`$...$` inline, `$$...$$` em
> destaque, render nativo na pré-visualização do VS Code); figuras reprodutíveis
> geradas por `tools/figuras/gerar_figuras_m08.py` e incorporadas por caminho
> relativo `assets/<NNN>-<slug>/<nome>.png`; blocos ```python só para código e
> saída.

## Seção_Teórica

### Motivação

A primeira resposta de um modelo raramente é a melhor. Pessoas escrevem rascunhos,
releem, encontram falhas e revisam — e agentes podem fazer o mesmo. O padrão
**Reflection** dá ao agente a capacidade de **criticar o próprio trabalho** e
**revisá-lo** antes de entregar. Em vez de aceitar a primeira saída, o agente gera
um rascunho, um **crítico** o avalia (apontando problemas concretos) e um
**revisor** produz uma versão melhor que incorpora o feedback. Esse ciclo se repete
até a saída atingir um padrão de qualidade. Reflection costuma elevar bastante a
qualidade em tarefas de escrita, código e raciocínio — ao custo de iterações
adicionais, o que torna o **critério de parada** essencial.

### Princípio de funcionamento

Reflection é um laço de auto-aperfeiçoamento com três papéis:

$$\text{gerar} \rightarrow \text{criticar} \rightarrow \text{revisar} \rightarrow \text{criticar} \rightarrow \cdots$$

O **gerador** produz um rascunho $r_0$. O **crítico** $C$ avalia o rascunho e
devolve um feedback estruturado (uma lista de problemas ou uma nota). O **revisor**
$R$ usa o feedback para produzir $r_{t+1} = R(r_t, C(r_t))$. O laço termina por um
**critério de aceitação**: ou o crítico não encontra mais problemas (ou a nota
ultrapassa um limiar), ou atinge-se um número máximo de revisões. O detalhe crucial
é que o crítico precisa ser **mais exigente** ou usar um **ângulo diferente** do
gerador — senão ele aprova qualquer coisa e o ciclo não agrega valor. Aqui, crítico
e revisor são funções determinísticas, para focar na mecânica do ciclo.

---

### Conceito central 1 — Crítico avaliador

O crítico inspeciona um rascunho e devolve um diagnóstico — aqui, uma nota e a lista
de problemas encontrados por regras simples. É a peça que torna a auto-revisão
possível.

#### Exemplo_Resolvido 1.1

```python
# Critico deterministico: pontua um rascunho por regras simples.
def criticar(texto):
    problemas = []
    if len(texto) < 20:
        problemas.append("muito curto")
    if "conclusao" not in texto:
        problemas.append("falta conclusao")
    nota = 10 - 3 * len(problemas)
    return nota, problemas

for rascunho in ["resumo breve", "texto longo com conclusao detalhada aqui"]:
    nota, problemas = criticar(rascunho)
    print(f"nota={nota} problemas={problemas}")
```

**Explicação passo a passo:**
- **Bloco 1 (`criticar`):** acumula problemas por duas regras (comprimento mínimo e presença da palavra `conclusao`) e converte a contagem em nota.
- **Bloco 2 (laço de teste):** o rascunho curto e sem conclusão recebe dois problemas (nota 4); o rascunho completo passa sem problemas (nota 10).

**Saída esperada:**
```
nota=4 problemas=['muito curto', 'falta conclusao']
nota=10 problemas=[]
```

---

### Conceito central 2 — Ciclo gerar → criticar → revisar

Com o crítico em mãos, o ciclo de Reflection alterna avaliação e revisão. A cada
iteração, o revisor incorpora **um** ponto do feedback, melhorando o rascunho até o
crítico aprová-lo.

#### Exemplo_Resolvido 2.1

```python
# Ciclo gerar -> criticar -> revisar ate o rascunho passar.
def criticar(texto):
    falta = []
    if "intro" not in texto: falta.append("intro")
    if "corpo" not in texto: falta.append("corpo")
    if "fim" not in texto: falta.append("fim")
    return falta

def revisar(texto, falta):
    return texto + " " + falta[0]

rascunho = "intro"
for it in range(1, 6):
    falta = criticar(rascunho)
    print(f"iter {it}: rascunho={rascunho!r} falta={falta}")
    if not falta:
        print("aceito")
        break
    rascunho = revisar(rascunho, falta)
```

**Explicação passo a passo:**
- **Bloco 1 (`criticar`):** devolve a lista de seções ausentes no rascunho.
- **Bloco 2 (`revisar`):** concatena a primeira seção faltante — uma melhoria por iteração.
- **Bloco 3 (laço):** imprime o estado de cada iteração; quando o crítico não acha mais faltas, o rascunho é `aceito` e o ciclo para (em 3 iterações).

**Saída esperada:**
```
iter 1: rascunho='intro' falta=['corpo', 'fim']
iter 2: rascunho='intro corpo' falta=['fim']
iter 3: rascunho='intro corpo fim' falta=[]
aceito
```

---

### Conceito central 3 — Critério de aceitação

Reflection pode melhorar indefinidamente, então precisa de um freio. O critério de
aceitação combina **qualidade** (nota acima de um limiar) com **orçamento** (número
máximo de revisões), garantindo que o ciclo sempre termina.

#### Exemplo_Resolvido 3.1

```python
# Criterio de aceitacao: nota >= limiar OU numero maximo de revisoes.
def avaliar(versao):
    return 4 + 2 * versao

limiar = 9
max_revisoes = 5
versao = 0
while True:
    nota = avaliar(versao)
    print(f"versao {versao}: nota={nota}")
    if nota >= limiar:
        print("aceito por qualidade")
        break
    if versao >= max_revisoes:
        print("parou no limite de revisoes")
        break
    versao += 1
```

**Explicação passo a passo:**
- **Bloco 1 (`avaliar`):** a nota cresce 2 pontos a cada revisão (modelo determinístico de melhoria).
- **Bloco 2 (laço com duas saídas):** aceita quando a nota atinge o limiar 9; senão, pararia ao esgotar `max_revisoes` — aqui a qualidade é atingida na versão 3 (nota 10).

**Saída esperada:**
```
versao 0: nota=4
versao 1: nota=6
versao 2: nota=8
versao 3: nota=10
aceito por qualidade
```

## Seção_Prática

> **Como reproduzir:** execute cada solução de referência com
> `python trilha/solucoes/065-reflection/solucao_<n>.py` e compare a saída com o
> arquivo `.saida.txt` correspondente. Os enunciados/esqueletos ficam em
> `trilha/pratica/065-reflection/exercicio_<n>.py`.

### Exercício 1 — Crítico determinístico
- **Entrada inicial / setup:** rascunhos `["titulo e mais texto", "curto"]`.
- **Passos de execução:** implemente `criticar(texto)` com as regras "sem titulo" (palavra `titulo` ausente) e "poucas palavras" (< 3 palavras); nota `10 - 4 * len(problemas)`; imprima `{texto!r}: nota={nota} problemas={problemas}`.
- **Critério de conclusão (binário):** a saída é **exatamente** igual a `solucao_1.saida.txt` (o rascunho `curto` recebe nota 2); qualquer divergência reprova.
- **Solução de referência:** `trilha/solucoes/065-reflection/solucao_1.py`
- **Saída esperada:** `trilha/solucoes/065-reflection/solucao_1.saida.txt`

### Exercício 2 — Ciclo gerar → criticar → revisar
- **Entrada inicial / setup:** partes obrigatórias `["abertura", "dados", "conclusao"]`; rascunho inicial `"abertura"`.
- **Passos de execução:** implemente `criticar` (partes faltantes) e `revisar` (adiciona a primeira faltante); itere até 5 vezes imprimindo `iter {it}: falta={falta}`; ao não faltar nada, imprima `aceito` e pare; imprima `final: {rascunho}`.
- **Critério de conclusão (binário):** a saída é **exatamente** igual a `solucao_2.saida.txt` (`final: abertura dados conclusao`); qualquer divergência reprova.
- **Solução de referência:** `trilha/solucoes/065-reflection/solucao_2.py`
- **Saída esperada:** `trilha/solucoes/065-reflection/solucao_2.saida.txt`

### Exercício 3 — Critério de aceitação
- **Entrada inicial / setup:** `avaliar(versao) = 3 + 3 * versao`; `limiar = 9`; `max_revisoes = 5`.
- **Passos de execução:** itere sobre versões imprimindo `versao {versao}: nota={nota}`; pare com `aceito por qualidade` (nota ≥ limiar) ou `parou no limite de revisoes` (versão ≥ max).
- **Critério de conclusão (binário):** a saída é **exatamente** igual a `solucao_3.saida.txt` (aceito na versão 2, nota 9); qualquer divergência reprova.
- **Solução de referência:** `trilha/solucoes/065-reflection/solucao_3.py`
- **Saída esperada:** `trilha/solucoes/065-reflection/solucao_3.saida.txt`
