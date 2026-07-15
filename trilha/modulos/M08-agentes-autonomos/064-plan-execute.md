---
id: licao-064-plan-execute
ordinal: 64
modulo: M08-agentes-autonomos
titulo: "Padrão Plan-Execute"
slug: plan-execute
pre_requisitos:
  - licao-063-react
tempo_estimado_min: 50
objetivos_de_aprendizagem:
  - "Distinguir Plan-Execute de ReAct e justificar quando planejar antecipadamente"
  - "Implementar um planner que gera um plano ordenado e um executor sequencial"
  - "Implementar replanejamento determinístico quando um passo falha"
competencias:
  - req-agentes
classificacao_ementa: "complemento de aprofundamento à ementa"
conceitos_centrais:
  - plano-estatico
  - executor-sequencial
  - replanejamento
envolve_parsing_serializacao: false
---

# Lição 064 — Padrão Plan-Execute

> **Módulo:** M08 — Agentes Autônomos · **Ordem de estudo:** 64 · **Tempo:** ~50 min
> **Pré-requisitos:** [063] Padrão ReAct (reason + act)
> **Classificação:** complemento de aprofundamento à ementa

> **Convenção de formatação:** matemática em LaTeX (`$...$` inline, `$$...$$` em
> destaque, render nativo na pré-visualização do VS Code); figuras reprodutíveis
> geradas por `tools/figuras/gerar_figuras_m08.py` e incorporadas por caminho
> relativo `assets/<NNN>-<slug>/<nome>.png`; blocos ```python só para código e
> saída.

## Seção_Teórica

### Motivação

No ReAct o agente decide **um passo de cada vez**: pensa, age, observa e só então
decide o próximo passo. Isso é flexível, mas tem custos: o modelo é chamado a cada
passo (mais latência e tokens) e, em tarefas longas, ele pode "se perder" e divagar
sem terminar. O padrão **Plan-Execute** ataca isso separando o raciocínio em duas
fases. Primeiro, um **planner** olha o objetivo e produz **um plano completo** —
uma lista ordenada de passos — de uma só vez. Depois, um **executor** roda os passos
em sequência, sem precisar reconsultar o modelo a cada um. Planejar antes torna a
execução mais barata e previsível, e expõe o plano para inspeção antes de agir. O
preço é a rigidez: se a realidade diverge do plano (um passo falha), é preciso
**replanejar**.

### Princípio de funcionamento

Plan-Execute é um pipeline de duas etapas. Dado um objetivo $g$, o planner produz
um plano

$$P = [\,p_1, p_2, \ldots, p_n\,] = \text{planejar}(g),$$

e o executor o consome em ordem, encadeando um estado $s$:

$$s_0 \xrightarrow{\,p_1\,} s_1 \xrightarrow{\,p_2\,} s_2 \cdots \xrightarrow{\,p_n\,} s_n.$$

Enquanto no ReAct o raciocínio se entrelaça com cada ação, aqui ele acontece
**uma vez** no início. Quando um passo $p_i$ **falha**, o agente entra em
**replanejamento**: substitui o passo problemático (ou o restante do plano) por uma
alternativa e retoma a execução a partir dali. Na prática, agentes maduros combinam
os dois padrões: planejam em alto nível e usam ReAct dentro de passos individuais.

---

### Conceito central 1 — Plano estático

O planner transforma um objetivo em uma sequência de passos **antes** de qualquer
execução. Aqui, um mapa determinístico associa cada objetivo conhecido ao seu plano.

#### Exemplo_Resolvido 1.1

```python
# Planner: gera um plano ordenado (lista de passos) a partir do objetivo.
def planejar(objetivo):
    planos = {
        "relatorio": ["coletar_dados", "analisar", "escrever", "revisar"],
        "deploy": ["testar", "build", "publicar"],
    }
    return planos.get(objetivo, [])

plano = planejar("relatorio")
for i, passo in enumerate(plano, 1):
    print(f"{i}. {passo}")
print("total de passos:", len(plano))
```

**Explicação passo a passo:**
- **Bloco 1 (`planejar`):** mapeia o objetivo para uma lista ordenada de passos; objetivos desconhecidos resultam em plano vazio.
- **Bloco 2 (impressão):** numera e exibe o plano gerado e o seu tamanho — o plano existe por inteiro antes de executar qualquer passo.

**Saída esperada:**
```
1. coletar_dados
2. analisar
3. escrever
4. revisar
total de passos: 4
```

---

### Conceito central 2 — Executor sequencial

Com o plano em mãos, o executor aplica os passos em ordem, encadeando o resultado de
um no próximo. Não há nova decisão entre passos — só execução.

#### Exemplo_Resolvido 2.1

```python
# Executor sequencial: aplica os passos em ordem, encadeando o resultado.
passos = [
    ("dobrar", lambda x: x * 2),
    ("somar10", lambda x: x + 10),
    ("negar", lambda x: -x),
]
valor = 5
for nome, fn in passos:
    valor = fn(valor)
    print(f"{nome}: {valor}")
print("resultado:", valor)
```

**Explicação passo a passo:**
- **Bloco 1 (`passos`):** o plano como lista de pares `(nome, função)` — cada passo transforma o valor corrente.
- **Bloco 2 (laço):** aplica os passos em sequência, encadeando `valor` e imprimindo o estado após cada um; o resultado final é a composição das três operações.

**Saída esperada:**
```
dobrar: 10
somar10: 20
negar: -20
resultado: -20
```

---

### Conceito central 3 — Replanejamento

A fragilidade do plano estático aparece quando um passo falha. O replanejamento
substitui o passo problemático por uma alternativa e retoma a execução, sem
descartar o progresso já feito.

#### Exemplo_Resolvido 3.1

```python
# Replanejamento: se um passo falha, o agente substitui o plano restante.
def executar(passo):
    if passo == "rota_rapida":
        return False
    return True

plano = ["preparar", "rota_rapida", "entregar"]
alternativo = {"rota_rapida": ["rota_alternativa"]}

i = 0
historico = []
while i < len(plano):
    passo = plano[i]
    ok = executar(passo)
    historico.append((passo, "ok" if ok else "falhou"))
    if not ok:
        plano = plano[:i] + alternativo[passo] + plano[i+1:]
        continue
    i += 1

for passo, status in historico:
    print(f"{passo}: {status}")
print("plano final:", plano)
```

**Explicação passo a passo:**
- **Bloco 1 (`executar`):** simula uma falha determinística no passo `rota_rapida` (retorna `False`).
- **Bloco 2 (laço com índice):** executa passo a passo, registrando o status no histórico.
- **Bloco 3 (substituição):** ao falhar, troca o passo atual pelos passos alternativos e usa `continue` para reprocessar a mesma posição — o agente prossegue por `rota_alternativa` e conclui em `entregar`.

**Saída esperada:**
```
preparar: ok
rota_rapida: falhou
rota_alternativa: ok
entregar: ok
plano final: ['preparar', 'rota_alternativa', 'entregar']
```

## Seção_Prática

> **Como reproduzir:** execute cada solução de referência com
> `python trilha/solucoes/064-plan-execute/solucao_<n>.py` e compare a saída com
> o arquivo `.saida.txt` correspondente. Os enunciados/esqueletos ficam em
> `trilha/pratica/064-plan-execute/exercicio_<n>.py`.

### Exercício 1 — Planner estático
- **Entrada inicial / setup:** `planejar(objetivo)` com o mapa `{"relatorio": [...], "deploy": ["testar", "build", "publicar"]}`; objetivo `"deploy"`.
- **Passos de execução:** gere o plano de `"deploy"`, imprima cada passo numerado (`{i}. {passo}`) e, ao final, `total de passos: {n}`.
- **Critério de conclusão (binário):** a saída é **exatamente** igual a `solucao_1.saida.txt` (`total de passos: 3`); qualquer divergência reprova.
- **Solução de referência:** `trilha/solucoes/064-plan-execute/solucao_1.py`
- **Saída esperada:** `trilha/solucoes/064-plan-execute/solucao_1.saida.txt`

### Exercício 2 — Executor sequencial
- **Entrada inicial / setup:** `passos = [("incrementar", +1), ("triplicar", *3), ("subtrair2", -2)]`, `valor = 3`.
- **Passos de execução:** aplique os passos em ordem encadeando o resultado; imprima `{nome}: {valor}` após cada passo e `resultado: {valor}` ao final.
- **Critério de conclusão (binário):** a saída é **exatamente** igual a `solucao_2.saida.txt` (`resultado: 10`); qualquer divergência reprova.
- **Solução de referência:** `trilha/solucoes/064-plan-execute/solucao_2.py`
- **Saída esperada:** `trilha/solucoes/064-plan-execute/solucao_2.saida.txt`

### Exercício 3 — Replanejamento ao falhar
- **Entrada inicial / setup:** `plano = ["login", "pagamento", "recibo"]`; `executar` falha só em `"pagamento"`; `alternativo = {"pagamento": ["pagamento_2fa"]}`.
- **Passos de execução:** execute por índice registrando `(passo, status)` em `historico`; ao falhar, substitua o passo pelo plano alternativo e retome; imprima cada `{passo}: {status}` e `plano final: {plano}`.
- **Critério de conclusão (binário):** a saída é **exatamente** igual a `solucao_3.saida.txt` (`plano final: ['login', 'pagamento_2fa', 'recibo']`); qualquer divergência reprova.
- **Solução de referência:** `trilha/solucoes/064-plan-execute/solucao_3.py`
- **Saída esperada:** `trilha/solucoes/064-plan-execute/solucao_3.saida.txt`
