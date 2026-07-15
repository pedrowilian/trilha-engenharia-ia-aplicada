---
id: licao-068-gerenciamento-de-contexto
ordinal: 68
modulo: M08-agentes-autonomos
titulo: "Gerenciamento de contexto e janela de contexto"
slug: gerenciamento-de-contexto
pre_requisitos:
  - licao-067-memoria-de-agentes
tempo_estimado_min: 50
objetivos_de_aprendizagem:
  - "Estimar o consumo de tokens de um histórico e compará-lo ao orçamento da janela"
  - "Aplicar truncamento por recência preservando a mensagem de sistema"
  - "Reduzir tokens por sumarização do histórico antigo"
competencias:
  - req-agentes
classificacao_ementa: "complemento de aprofundamento à ementa"
conceitos_centrais:
  - orcamento-de-tokens
  - truncamento-por-recencia
  - sumarizacao-de-historico
envolve_parsing_serializacao: false
---

# Lição 068 — Gerenciamento de contexto e janela de contexto

> **Módulo:** M08 — Agentes Autônomos · **Ordem de estudo:** 68 · **Tempo:** ~50 min
> **Pré-requisitos:** [067] Memória de agentes (curto/longo prazo)
> **Classificação:** complemento de aprofundamento à ementa

> **Convenção de formatação:** matemática em LaTeX (`$...$` inline, `$$...$$` em
> destaque, render nativo na pré-visualização do VS Code); figuras reprodutíveis
> geradas por `tools/figuras/gerar_figuras_m08.py` e incorporadas por caminho
> relativo `assets/<NNN>-<slug>/<nome>.png`; blocos ```python só para código e
> saída.

## Seção_Teórica

### Motivação

Todo LLM tem uma **janela de contexto** finita — um número máximo de tokens que cabe
numa chamada. Um agente que conversa por muitos turnos, consulta documentos e
acumula observações rapidamente **estoura** esse limite. Quando isso acontece, ou a
chamada falha, ou o provedor corta silenciosamente parte do histórico, fazendo o
agente "esquecer" instruções importantes. **Gerenciar o contexto** é decidir, a cada
passo, **o que entra** na janela e **o que fica de fora**, dentro de um orçamento de
tokens. As três alavancas básicas são: **medir** o consumo, **truncar** o que é menos
relevante e **sumarizar** o histórico antigo para comprimi-lo. Fazer isso bem é o que
separa um agente que aguenta conversas longas de um que se perde após poucos turnos.

### Princípio de funcionamento

Tudo começa por **contar tokens**. Em produção usa-se o tokenizador do modelo; aqui,
para manter determinismo, aproximamos um token por palavra. Dado um orçamento $B$ e
mensagens com custos $c_1, \ldots, c_n$, a restrição é

$$\sum_{i \in \text{incluídas}} c_i \le B.$$

Quando o histórico não cabe, aplicamos uma **política de seleção**. A mais comum é o
**truncamento por recência**: preserva-se a mensagem de **sistema** (que carrega as
instruções) e incluem-se as mensagens **mais recentes** que couberem, descartando as
antigas. Quando descartar perderia informação importante, usa-se **sumarização**:
substitui-se um bloco de mensagens antigas por um **resumo** curto, que custa muito
menos tokens e preserva o essencial. Na prática combinam-se as três: medir sempre,
truncar o irrelevante e sumarizar o que precisa ser lembrado mas não cabe inteiro.

---

### Conceito central 1 — Orçamento de tokens

Antes de decidir o que cortar, é preciso **medir**. Contar os tokens de cada mensagem
e somá-los diz se o histórico cabe no orçamento da janela.

#### Exemplo_Resolvido 1.1

```python
# Orcamento de tokens: conta tokens (aprox. por palavras) e compara ao limite.
def contar_tokens(texto):
    return len(texto.split())

mensagens = ["ola tudo bem", "preciso de ajuda com python", "ok"]
limite = 8
total = sum(contar_tokens(m) for m in mensagens)
print("tokens por mensagem:", [contar_tokens(m) for m in mensagens])
print("total:", total)
print("cabe no limite?", total <= limite)
```

**Explicação passo a passo:**
- **Bloco 1 (`contar_tokens`):** aproxima o número de tokens pela contagem de palavras (determinístico).
- **Bloco 2 (soma):** soma o custo de todas as mensagens.
- **Bloco 3 (`print`):** o total (9) excede o orçamento (8), então `cabe no limite?` é `False` — sinal de que é preciso truncar ou sumarizar.

**Saída esperada:**
```
tokens por mensagem: [3, 5, 1]
total: 9
cabe no limite? False
```

---

### Conceito central 2 — Truncamento por recência

Quando o histórico não cabe, mantemos a mensagem de sistema e as **mais recentes**
que couberem, descartando as antigas. Percorrer o histórico de trás para frente
torna a seleção simples.

#### Exemplo_Resolvido 2.1

```python
# Truncamento: mantem a mensagem de sistema + as mais recentes que couberem.
def contar(t):
    return len(t.split())

sistema = "voce e um assistente"          # 4 tokens, sempre mantido
historico = ["primeira pergunta", "segunda pergunta", "terceira pergunta agora"]
limite = 10

incluidas = []
usado = contar(sistema)
for msg in reversed(historico):           # das mais recentes para as antigas
    c = contar(msg)
    if usado + c <= limite:
        incluidas.append(msg)
        usado += c
    else:
        break
incluidas.reverse()
print("sistema:", sistema)
print("incluidas:", incluidas)
print("tokens usados:", usado)
```

**Explicação passo a passo:**
- **Bloco 1 (`sistema`/`historico`):** a mensagem de sistema é reservada primeiro (sempre presente); o orçamento restante é para o histórico.
- **Bloco 2 (laço `reversed`):** inclui mensagens da mais recente para a mais antiga enquanto cabem; ao estourar, para.
- **Bloco 3 (`reverse` + `print`):** restaura a ordem cronológica; a mensagem mais antiga ficou de fora, e o uso total (9) respeita o limite (10).

**Saída esperada:**
```
sistema: voce e um assistente
incluidas: ['segunda pergunta', 'terceira pergunta agora']
tokens usados: 9
```

---

### Conceito central 3 — Sumarização de histórico

Truncar perde informação. Quando o passado importa mas não cabe, **sumarizamos**:
trocamos várias mensagens antigas por um resumo curto, reduzindo o custo em tokens
sem perder o essencial.

#### Exemplo_Resolvido 3.1

```python
# Sumarizacao: comprime mensagens antigas num resumo curto para caber no contexto.
def contar(t):
    return len(t.split())

antigas = ["cliente pediu reembolso", "agente abriu chamado", "chamado foi aprovado"]
resumo = "resumo: reembolso aprovado"

tokens_antes = sum(contar(m) for m in antigas)
tokens_depois = contar(resumo)
print("tokens antes:", tokens_antes)
print("tokens depois:", tokens_depois)
print("reducao:", tokens_antes - tokens_depois)
```

**Explicação passo a passo:**
- **Bloco 1 (`antigas`/`resumo`):** três mensagens antigas e o resumo que as condensa.
- **Bloco 2 (contagem):** soma os tokens antes e mede o resumo.
- **Bloco 3 (`print`):** a sumarização reduz de 9 para 3 tokens (economia de 6), liberando espaço na janela mantendo o sentido.

**Saída esperada:**
```
tokens antes: 9
tokens depois: 3
reducao: 6
```

## Seção_Prática

> **Como reproduzir:** execute cada solução de referência com
> `python trilha/solucoes/068-gerenciamento-de-contexto/solucao_<n>.py` e compare
> a saída com o arquivo `.saida.txt` correspondente. Os enunciados/esqueletos
> ficam em `trilha/pratica/068-gerenciamento-de-contexto/exercicio_<n>.py`.

### Exercício 1 — Orçamento de tokens
- **Entrada inicial / setup:** `mensagens = ["bom dia", "quero saber sobre agentes de ia", "obrigado"]`; `limite = 10`.
- **Passos de execução:** implemente `contar_tokens(texto)`; imprima `tokens por mensagem: {lista}`, `total: {soma}` e `cabe no limite? {bool}`.
- **Critério de conclusão (binário):** a saída é **exatamente** igual a `solucao_1.saida.txt` (`cabe no limite? True`); qualquer divergência reprova.
- **Solução de referência:** `trilha/solucoes/068-gerenciamento-de-contexto/solucao_1.py`
- **Saída esperada:** `trilha/solucoes/068-gerenciamento-de-contexto/solucao_1.saida.txt`

### Exercício 2 — Truncamento por recência
- **Entrada inicial / setup:** `sistema = "assistente util"`; `historico = ["passo um inicial", "passo dois meio", "passo tres final"]`; `limite = 8`.
- **Passos de execução:** reserve o sistema; inclua mensagens da mais recente para a mais antiga enquanto couberem; restaure a ordem; imprima `sistema:`, `incluidas:` e `tokens usados:`.
- **Critério de conclusão (binário):** a saída é **exatamente** igual a `solucao_2.saida.txt` (`tokens usados: 8`); qualquer divergência reprova.
- **Solução de referência:** `trilha/solucoes/068-gerenciamento-de-contexto/solucao_2.py`
- **Saída esperada:** `trilha/solucoes/068-gerenciamento-de-contexto/solucao_2.saida.txt`

### Exercício 3 — Sumarização de histórico
- **Entrada inicial / setup:** `antigas = [...]` (4 mensagens) e `resumo = "resumo: bug corrigido e publicado"`.
- **Passos de execução:** conte os tokens antes (soma das antigas) e depois (resumo); imprima `tokens antes:`, `tokens depois:` e `reducao:`.
- **Critério de conclusão (binário):** a saída é **exatamente** igual a `solucao_3.saida.txt` (`reducao: 6`); qualquer divergência reprova.
- **Solução de referência:** `trilha/solucoes/068-gerenciamento-de-contexto/solucao_3.py`
- **Saída esperada:** `trilha/solucoes/068-gerenciamento-de-contexto/solucao_3.saida.txt`
