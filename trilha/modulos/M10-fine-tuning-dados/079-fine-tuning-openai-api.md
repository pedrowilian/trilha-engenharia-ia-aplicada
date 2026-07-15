---
id: licao-079-fine-tuning-openai-api
ordinal: 79
modulo: M10-fine-tuning-dados
titulo: "Fine-tuning via OpenAI API"
slug: fine-tuning-openai-api
pre_requisitos:
  - licao-076-preparacao-datasets-fine-tuning
  - licao-077-fine-tuning-completo
tempo_estimado_min: 50
objetivos_de_aprendizagem:
  - "Fazer upload e validar um arquivo JSONL de treino usando um cliente simulado"
  - "Criar um job de fine-tuning com hiperparâmetros e estimar o número de passos de treino"
  - "Monitorar a progressão do treino e usar o nome do modelo ajustado resultante"
competencias:
  - comp-fine-tuning-api
classificacao_ementa: "coberto pela ementa"
conceitos_centrais:
  - upload-e-validacao
  - job-e-hiperparametros
  - monitoramento-e-uso
envolve_parsing_serializacao: false
---

# Lição 079 — Fine-tuning via OpenAI API

> **Módulo:** M10 — Fine-Tuning e Processamento de Dados · **Ordem de estudo:** 79 · **Tempo:** ~50 min
> **Pré-requisitos:** [076] Preparação de datasets para fine-tuning · [077] Fine-tuning completo: quando e por quê
> **Classificação:** coberto pela ementa

> **Convenção de formatação:** matemática em LaTeX (`$...$` inline, `$$...$$` em
> destaque, render nativo na pré-visualização do VS Code); figuras reprodutíveis
> geradas por `tools/figuras/gerar_figuras_m10.py` e incorporadas por caminho
> relativo `assets/<NNN>-<slug>/<nome>.png`; blocos ```python só para código e
> saída.

## Seção_Teórica

### Motivação

Plataformas gerenciadas como a **API de fine-tuning da OpenAI** abstraem GPUs,
distribuição e otimizador: você envia um arquivo JSONL, escolhe hiperparâmetros,
dispara um **job** e recebe, ao final, o **nome de um modelo ajustado** pronto para
uso. Entender esse fluxo — upload, validação, criação do job, monitoramento e
consumo — é o que separa "li sobre fine-tuning" de "coloquei um modelo ajustado em
produção". Para aprender o fluxo sem custo nem dependência de rede, esta lição usa
um **cliente simulado**: um pequeno objeto Python determinístico que imita as
respostas da API. As ideias (formato dos objetos, estados do job, estimativa de
passos) são as mesmas do cliente real.

### Princípio de funcionamento

O ciclo de vida de um fine-tuning gerenciado tem quatro etapas. (1) **Upload**: o
arquivo JSONL é enviado e validado; cada linha precisa ter o campo `messages`. A
API devolve um `file-id`. (2) **Criação do job**: você referencia o `file-id`,
escolhe o modelo base e os **hiperparâmetros** — número de épocas, multiplicador da
taxa de aprendizado e tamanho do batch. O número de **passos** de treino é
$\text{passos} = n_{\text{épocas}} \cdot \lceil n_{\text{exemplos}} / b \rceil$,
onde $b$ é o batch size. (3) **Monitoramento**: o job transita por estados
(`validating_files` → `queued` → `running` → `succeeded`) e emite eventos com a
perda de treino. (4) **Uso**: ao terminar com sucesso, a API expõe um identificador
como `ft:base-mini:org::abc123`, que passa a ser usado como qualquer outro modelo.

---

### Conceito central 1 — Upload e validação

Antes de treinar, o arquivo precisa ser **válido**. A validação local — verificar
que cada linha parseia como JSON e contém `messages` não vazio — pega erros de
formatação cedo, evitando jobs que falham depois de enfileirados. O cliente
simulado reproduz esse comportamento devolvendo um `file-id` e o status
`processed`, ou levantando um erro na primeira linha inválida.

#### Exemplo_Resolvido 1.1

```python
import json

# Cliente simulado: NAO faz chamadas de rede; imita o endpoint de upload.
class ClienteSimulado:
    def __init__(self):
        self._seq = 0
    def upload(self, linhas_jsonl):
        for i, linha in enumerate(linhas_jsonl, 1):
            obj = json.loads(linha)
            if "messages" not in obj or not obj["messages"]:
                raise ValueError(f"linha {i} sem 'messages'")
        self._seq += 1
        return {"id": f"file-{self._seq:04d}", "n_exemplos": len(linhas_jsonl), "status": "processed"}

linhas = [
    json.dumps({"messages": [{"role": "user", "content": "oi"}, {"role": "assistant", "content": "ola"}]}),
    json.dumps({"messages": [{"role": "user", "content": "2+2"}, {"role": "assistant", "content": "4"}]}),
]
cli = ClienteSimulado()
res = cli.upload(linhas)
print("id do arquivo:", res["id"])
print("exemplos:", res["n_exemplos"])
print("status:", res["status"])
```

**Explicação passo a passo:**
- **Bloco 1 (`ClienteSimulado`):** imita a API localmente; `upload` valida cada linha e gera um `file-id` sequencial.
- **Bloco 2 (`linhas`):** dois exemplos de chat já serializados como JSON.
- **Bloco 3 (`print`):** o upload válido devolve `file-0001`, a contagem de exemplos e o status `processed`.

**Saída esperada:**
```
id do arquivo: file-0001
exemplos: 2
status: processed
```

---

### Conceito central 2 — Job e hiperparâmetros

O **job** amarra o arquivo de treino, o modelo base e os hiperparâmetros. As três
alavancas mais importantes são **n_epochs** (quantas vezes o dataset é percorrido),
**learning_rate_multiplier** (escala a taxa de aprendizado base) e **batch_size**.
Elas determinam quantos **passos** de gradiente o treino fará.

#### Exemplo_Resolvido 2.1

```python
def criar_job(file_id, modelo_base, n_epochs, lr_mult, batch_size):
    return {
        "id": "ftjob-0001",
        "model": modelo_base,
        "training_file": file_id,
        "hyperparameters": {
            "n_epochs": n_epochs,
            "learning_rate_multiplier": lr_mult,
            "batch_size": batch_size,
        },
        "status": "validating_files",
    }

job = criar_job("file-0001", "base-mini", n_epochs=3, lr_mult=0.1, batch_size=8)
print("job:", job["id"], "status:", job["status"])
for chave, valor in job["hyperparameters"].items():
    print(f"  {chave} = {valor}")
```

**Explicação passo a passo:**
- **Bloco 1 (`criar_job`):** monta o objeto do job referenciando o `file-id` e fixando o status inicial `validating_files`.
- **Bloco 2 (`job`/laço):** cria o job e imprime os hiperparâmetros; é a configuração que será efetivamente treinada.

**Saída esperada:**
```
job: ftjob-0001 status: validating_files
  n_epochs = 3
  learning_rate_multiplier = 0.1
  batch_size = 8
```

---

### Conceito central 3 — Monitoramento e uso

Depois de criado, o job é **acompanhado** até terminar. Os eventos reportam o
progresso e, no sucesso, a API entrega o **nome do modelo ajustado**, que é então
usado em chamadas normais de inferência. O cliente simulado reproduz a sequência de
estados e o consumo do modelo de forma determinística.

#### Exemplo_Resolvido 3.1

```python
# Simula a progressao de status e o uso do modelo ajustado (sem rede).
estados = ["validating_files", "queued", "running", "succeeded"]

def monitorar(estados):
    eventos = list(estados)
    modelo = "ft:base-mini:org::0001" if estados[-1] == "succeeded" else None
    return eventos, modelo

eventos, modelo = monitorar(estados)
for i, e in enumerate(eventos):
    print(f"evento {i}: {e}")
print("modelo ajustado:", modelo)

def responder(modelo, pergunta):
    # resposta simulada e deterministica
    return f"[{modelo}] resposta para: {pergunta}"

print(responder(modelo, "Qual a capital do Brasil?"))
```

**Explicação passo a passo:**
- **Bloco 1 (`estados`):** a sequência típica de status de um job bem-sucedido.
- **Bloco 2 (`monitorar`):** percorre os estados e, no estado final `succeeded`, expõe o nome do modelo ajustado.
- **Bloco 3 (`responder`/`print`):** usa o modelo ajustado como qualquer outro — aqui a resposta é simulada e determinística, sem rede.

**Saída esperada:**
```
evento 0: validating_files
evento 1: queued
evento 2: running
evento 3: succeeded
modelo ajustado: ft:base-mini:org::0001
[ft:base-mini:org::0001] resposta para: Qual a capital do Brasil?
```

## Seção_Prática

> **Como reproduzir:** execute cada solução de referência com
> `python trilha/solucoes/079-fine-tuning-openai-api/solucao_<n>.py` e compare a
> saída com o arquivo `.saida.txt` correspondente. Os enunciados/esqueletos
> ficam em `trilha/pratica/079-fine-tuning-openai-api/exercicio_<n>.py`.

### Exercício 1 — Upload simulado com validação
- **Entrada inicial / setup:** a classe `ClienteSimulado` (a implementar), 3 linhas JSONL válidas e uma quarta linha sem `messages`.
- **Passos de execução:** implemente `upload(linhas)` que valida cada linha (erro `f"linha {i} invalida: sem 'messages'"`) e devolve {id, n_exemplos, status}; faça o upload válido (imprima id, n e status) e o inválido capturando o erro.
- **Critério de conclusão (binário):** a saída é **exatamente** igual a `solucao_1.saida.txt` (`upload ok: file-0001 3 processed` e `erro capturado: linha 4 invalida: sem 'messages'`); qualquer divergência reprova.
- **Solução de referência:** `trilha/solucoes/079-fine-tuning-openai-api/solucao_1.py`
- **Saída esperada:** `trilha/solucoes/079-fine-tuning-openai-api/solucao_1.saida.txt`

### Exercício 2 — Criar job e estimar passos
- **Entrada inicial / setup:** file_id="file-0001", modelo_base="base-mini", n_exemplos=50, n_epochs=3, lr_mult=0.2, batch_size=8.
- **Passos de execução:** implemente `criar_job(...)` com `passos_estimados = n_epochs * ceil(n_exemplos / batch_size)` e imprima o cabeçalho do job, os hiperparâmetros e os passos estimados.
- **Critério de conclusão (binário):** a saída é **exatamente** igual a `solucao_2.saida.txt` (`passos estimados: 21`); qualquer divergência reprova.
- **Solução de referência:** `trilha/solucoes/079-fine-tuning-openai-api/solucao_2.py`
- **Saída esperada:** `trilha/solucoes/079-fine-tuning-openai-api/solucao_2.saida.txt`

### Exercício 3 — Monitorar e usar o modelo ajustado
- **Entrada inicial / setup:** 4 passos, perda inicial 2.0, decaimento 0.8.
- **Passos de execução:** implemente `monitorar(...)` (lista de (passo, round(perda,4)), status "succeeded", nome "ft:base-mini:org::abc123") e `responder(modelo, pergunta)` (`f"[{modelo}] -> {pergunta.upper()}"`); imprima a curva de perda, o status, o modelo e a resposta para "ola mundo".
- **Critério de conclusão (binário):** a saída é **exatamente** igual a `solucao_3.saida.txt` (`passo 4: train_loss=1.024` e a resposta `[ft:base-mini:org::abc123] -> OLA MUNDO`); qualquer divergência reprova.
- **Solução de referência:** `trilha/solucoes/079-fine-tuning-openai-api/solucao_3.py`
- **Saída esperada:** `trilha/solucoes/079-fine-tuning-openai-api/solucao_3.saida.txt`
