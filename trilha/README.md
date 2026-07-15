# Trilha de Engenharia de IA Aplicada — Índice

> Currículo autoral, **teoria-primeiro**, do fundamento absoluto ao avançado, com prática em **Python**
> ao fim de cada lição. Uma lição = um único tópico. Estudo sequencial, sem deixar nada solto.
>
> Este `README.md` é o **índice navegável** da Trilha (R11.1, R11.2): a lista de todas as lições na
> ordem de estudo numerada, com módulo, pré-requisitos e estado de conclusão. Para a ementa detalhada
> voltada ao estudo (visão de módulos e descrição de cada aula), consulte [`EMENTA.md`](EMENTA.md).

## Como estudar

1. Comece pela lição de menor número que ainda não concluiu (veja **▶ Retomar em**, abaixo).
2. Estude a `Seção_Teórica` (motivação → princípio de funcionamento → conceitos com exemplos
   resolvidos) e depois resolva os exercícios da `Seção_Prática`.
3. Registre seu progresso em [`progresso.yaml`](progresso.yaml) (`nao_iniciada` → `em_andamento` →
   `concluida`). O estado exibido neste índice é derivado desse arquivo.
4. Avance para a próxima lição na ordem numerada.

## Convenção de nomes e organização dos arquivos

A ordem global de estudo é **codificada no nome do arquivo** — ordenar todos os arquivos de lição pelo
seu prefixo numérico reproduz a sequência completa, sem lacunas nem repetições.

Cada lição vive em:

```
modulos/M<MM>-<modulo-slug>/<NNN>-<topico-slug>.md
```

- `<MM>` — número do módulo com 2 dígitos (`00`..`16`), com zero à esquerda para que a ordenação
  lexicográfica coincida com a numérica (ex.: `M00`, `M01`, ..., `M16`).
- `<NNN>` — **ordinal global** de estudo com 3 dígitos, contíguo a partir de `001`, **único em toda a
  Trilha**. É a fonte da verdade da ordem de estudo.
- `<topico-slug>` — slug em kebab-case do tópico único da lição.

Exemplo: `modulos/M01-fundamentos-de-ml/013-gradient-descent.md`.

### Espelhamento em `pratica/` e `solucoes/`

Os exercícios e as soluções de cada lição ficam em diretórios-irmãos que **espelham** o prefixo
`<NNN>-<topico-slug>` da lição, amarrando código e enunciados à sua lição de origem:

```
modulos/M01-fundamentos-de-ml/013-gradient-descent.md   # a lição (teoria + prática descrita)
pratica/013-gradient-descent/                            # exercícios em Python (enunciado/esqueleto)
  ├─ exercicio_1.py
  ├─ exercicio_2.py
  └─ exercicio_3.py
solucoes/013-gradient-descent/                           # soluções de referência + saída esperada
  ├─ solucao_1.py
  ├─ solucao_1.saida.txt
  └─ ...
```

Regra geral: para a lição `<NNN>-<topico-slug>`, existem `pratica/<NNN>-<topico-slug>/` e
`solucoes/<NNN>-<topico-slug>/` com o mesmo prefixo `<NNN>-<topico-slug>`.

## ▶ Retomar em

<!-- MARCADOR-RETOMAR: preenchido automaticamente pelo gerador (tarefa 26) a partir de progresso.yaml.
     Aponta para a primeira lição (na ordem numerada) em estado "em_andamento"; na ausência desta,
     a primeira em estado "nao_iniciada"; se todas estiverem "concluida", indica "trilha completa". -->

▶ **Retomar em:** [#001 — Vetores e espaços vetoriais](modulos/M00-fundamentos-matematicos/001-vetores-e-espacos-vetoriais.md)

## Índice de lições

> O corpo desta tabela (as 104 lições, em ordem de `001` a `104`) é **gerado automaticamente** pelo
> índice na tarefa 26, a partir dos arquivos em `modulos/` e do estado em `progresso.yaml`. Por ora,
> apenas o cabeçalho e a convenção estão definidos.
>
> **Estado:** ☐ não iniciada · ◐ em andamento · ☑ concluída.

| # | Módulo | Lição | Pré-requisitos | Estado |
|---|--------|-------|----------------|--------|
<!-- INICIO-LINHAS-LICOES (gerado na tarefa 26) -->
| [001](modulos/M00-fundamentos-matematicos/001-vetores-e-espacos-vetoriais.md) | M00 — Fundamentos Matemáticos | Vetores e espaços vetoriais | — | ☐ não iniciada |
| [002](modulos/M00-fundamentos-matematicos/002-matrizes-e-operacoes.md) | M00 — Fundamentos Matemáticos | Matrizes e operações matriciais | 001 | ☐ não iniciada |
| [003](modulos/M00-fundamentos-matematicos/003-transformacoes-lineares-multiplicacao-matriz-vetor.md) | M00 — Fundamentos Matemáticos | Transformações lineares e multiplicação matriz-vetor | 002 | ☐ não iniciada |
| [004](modulos/M00-fundamentos-matematicos/004-autovalores-autovetores-svd-pca.md) | M00 — Fundamentos Matemáticos | Autovalores, autovetores, SVD/PCA (intuição) | 003 | ☐ não iniciada |
| [005](modulos/M00-fundamentos-matematicos/005-normas-produto-interno-distancias.md) | M00 — Fundamentos Matemáticos | Normas, produto interno e distâncias | 001 | ☐ não iniciada |
| [006](modulos/M00-fundamentos-matematicos/006-funcoes-limites-derivadas.md) | M00 — Fundamentos Matemáticos | Funções, limites e derivadas | — | ☐ não iniciada |
| [007](modulos/M00-fundamentos-matematicos/007-derivadas-parciais-gradiente-regra-da-cadeia.md) | M00 — Fundamentos Matemáticos | Derivadas parciais, gradiente e regra da cadeia | 006 | ☐ não iniciada |
| [008](modulos/M00-fundamentos-matematicos/008-probabilidade-e-distribuicoes.md) | M00 — Fundamentos Matemáticos | Probabilidade e Distribuições | — | ☐ não iniciada |
| [009](modulos/M00-fundamentos-matematicos/009-estatistica-descritiva-e-inferencia.md) | M00 — Fundamentos Matemáticos | Estatística Descritiva e Inferência | 008 | ☐ não iniciada |
| [010](modulos/M00-fundamentos-matematicos/010-verossimilhanca-entropia-kl.md) | M00 — Fundamentos Matemáticos | Verossimilhança, Entropia e Divergência KL | 007, 008 | ☐ não iniciada |
| [011](modulos/M01-fundamentos-de-ml/011-o-que-e-ml.md) | M01 — Fundamentos de ML | O que é Machine Learning: supervisionado, não-supervisionado e por reforço | 009 | ☐ não iniciada |
| [012](modulos/M01-fundamentos-de-ml/012-funcoes-de-perda.md) | M01 — Fundamentos de ML | Funções de perda: MSE e cross-entropy | 010, 011 | ☐ não iniciada |
| [013](modulos/M01-fundamentos-de-ml/013-gradient-descent.md) | M01 — Fundamentos de ML | Gradient Descent | 007, 012 | ☐ não iniciada |
| [014](modulos/M01-fundamentos-de-ml/014-backpropagation.md) | M01 — Fundamentos de ML | Backpropagation | 013 | ☐ não iniciada |
| [015](modulos/M01-fundamentos-de-ml/015-regularizacao.md) | M01 — Fundamentos de ML | Regularização: L1, L2, dropout e early stopping | 012 | ☐ não iniciada |
| [016](modulos/M01-fundamentos-de-ml/016-vies-variancia.md) | M01 — Fundamentos de ML | Trade-off viés-variância | 011, 015 | ☐ não iniciada |
| [017](modulos/M01-fundamentos-de-ml/017-overfitting-validacao-cruzada.md) | M01 — Fundamentos de ML | Overfitting, underfitting e validação cruzada | 016 | ☐ não iniciada |
| [018](modulos/M01-fundamentos-de-ml/018-calibracao.md) | M01 — Fundamentos de ML | Calibração de modelos | 008, 017 | ☐ não iniciada |
| [019](modulos/M01-fundamentos-de-ml/019-desbalanceamento-de-classes.md) | M01 — Fundamentos de ML | Desbalanceamento de classes | 017 | ☐ não iniciada |
| [020](modulos/M01-fundamentos-de-ml/020-data-leakage.md) | M01 — Fundamentos de ML | Data leakage (vazamento de dados) | 017 | ☐ não iniciada |
| [021](modulos/M01-fundamentos-de-ml/021-experimentacao-testes-ab.md) | M01 — Fundamentos de ML | Metodologia de experimentação e testes A/B | 009, 017 | ☐ não iniciada |
| [022](modulos/M02-redes-neurais-deep-learning/022-perceptron.md) | M02 — Redes Neurais e Deep Learning | Perceptron e o neurônio artificial | 014 | ☐ não iniciada |
| [023](modulos/M02-redes-neurais-deep-learning/023-funcoes-de-ativacao.md) | M02 — Redes Neurais e Deep Learning | Funções de ativação (sigmoid, tanh, ReLU, GELU) | 022 | ☐ não iniciada |
| [024](modulos/M02-redes-neurais-deep-learning/024-mlp.md) | M02 — Redes Neurais e Deep Learning | Multi-Layer Perceptron (MLP) | 023 | ☐ não iniciada |
| [025](modulos/M02-redes-neurais-deep-learning/025-treino-redes-profundas-inicializacao.md) | M02 — Redes Neurais e Deep Learning | Treinamento de redes profundas e inicialização de pesos | 024 | ☐ não iniciada |
| [026](modulos/M02-redes-neurais-deep-learning/026-batch-layer-norm.md) | M02 — Redes Neurais e Deep Learning | Normalização: batch norm e layer norm | 025 | ☐ não iniciada |
| [027](modulos/M02-redes-neurais-deep-learning/027-vanishing-exploding-gradients.md) | M02 — Redes Neurais e Deep Learning | Vanishing e exploding gradients | 014, 025 | ☐ não iniciada |
| [028](modulos/M02-redes-neurais-deep-learning/028-otimizadores.md) | M02 — Redes Neurais e Deep Learning | Otimizadores: momentum, RMSProp, Adam | 013, 025 | ☐ não iniciada |
| [029](modulos/M02-redes-neurais-deep-learning/029-cnn.md) | M02 — Redes Neurais e Deep Learning | Redes Convolucionais (CNN): convolução e pooling | 024 | ☐ não iniciada |
| [030](modulos/M02-redes-neurais-deep-learning/030-rnn-lstm-gru.md) | M02 — Redes Neurais e Deep Learning | Redes Recorrentes: RNN, LSTM, GRU | 024, 027 | ☐ não iniciada |
| [031](modulos/M02-redes-neurais-deep-learning/031-arquiteturas-profundas-transfer-learning.md) | M02 — Redes Neurais e Deep Learning | Arquiteturas profundas e transfer learning | 029, 030 | ☐ não iniciada |
| [032](modulos/M03-nlp-tokenizacao-embeddings-busca-vetorial/032-nlp-fundamentos.md) | M03 — NLP, Tokenização, Embeddings e Busca Vetorial | Fundamentos de NLP e representação de texto | 011 | ☐ não iniciada |
| [033](modulos/M03-nlp-tokenizacao-embeddings-busca-vetorial/033-tokenizacao.md) | M03 — NLP, Tokenização, Embeddings e Busca Vetorial | Tokenização: BPE, WordPiece e SentencePiece | 032 | ☐ não iniciada |
| [034](modulos/M03-nlp-tokenizacao-embeddings-busca-vetorial/034-embeddings.md) | M03 — NLP, Tokenização, Embeddings e Busca Vetorial | Embeddings: word2vec, GloVe e contextuais | 005, 033 | ☐ não iniciada |
| [035](modulos/M03-nlp-tokenizacao-embeddings-busca-vetorial/035-metricas-distancia-similaridade.md) | M03 — NLP, Tokenização, Embeddings e Busca Vetorial | Métricas de distância e similaridade: cosseno, L2 e dot | 005, 034 | ☐ não iniciada |
| [036](modulos/M03-nlp-tokenizacao-embeddings-busca-vetorial/036-busca-vetorial-knn-exato.md) | M03 — NLP, Tokenização, Embeddings e Busca Vetorial | Busca vetorial e k-NN exato | 035 | ☐ não iniciada |
| [037](modulos/M03-nlp-tokenizacao-embeddings-busca-vetorial/037-busca-aproximada-ann.md) | M03 — NLP, Tokenização, Embeddings e Busca Vetorial | Busca aproximada (ANN) e trade-offs recall/latência | 036 | ☐ não iniciada |
| [038](modulos/M03-nlp-tokenizacao-embeddings-busca-vetorial/038-hnsw.md) | M03 — NLP, Tokenização, Embeddings e Busca Vetorial | HNSW por dentro: grafos hierárquicos navegáveis | 037 | ☐ não iniciada |
| [039](modulos/M04-transformers/039-motivacao-atencao.md) | M04 — Transformers por dentro | Limitações de RNNs e a motivação para atenção | 030 | ☐ não iniciada |
| [040](modulos/M04-transformers/040-self-attention-qkv.md) | M04 — Transformers por dentro | Self-attention com Query/Key/Value | 034, 039 | ☐ não iniciada |
| [041](modulos/M04-transformers/041-positional-encoding.md) | M04 — Transformers por dentro | Positional encoding | 040 | ☐ não iniciada |
| [042](modulos/M04-transformers/042-multi-head-attention.md) | M04 — Transformers por dentro | Multi-head attention | 040 | ☐ não iniciada |
| [043](modulos/M04-transformers/043-arquitetura-transformer.md) | M04 — Transformers por dentro | Arquitetura completa do Transformer | 026, 041, 042 | ☐ não iniciada |
| [044](modulos/M05-llms-pipeline-de-treino/044-llms-modelagem-linguagem-escala.md) | M05 — LLMs e Pipeline de Treino | O que são LLMs: modelagem de linguagem e leis de escala | 043 | ☐ não iniciada |
| [045](modulos/M05-llms-pipeline-de-treino/045-pre-treinamento.md) | M05 — LLMs e Pipeline de Treino | Pré-treinamento de LLMs: objetivo, dados e custo | 044 | ☐ não iniciada |
| [046](modulos/M05-llms-pipeline-de-treino/046-instruction-tuning-sft.md) | M05 — LLMs e Pipeline de Treino | Instruction tuning e Supervised Fine-Tuning (SFT) | 045 | ☐ não iniciada |
| [047](modulos/M05-llms-pipeline-de-treino/047-rlhf-ppo.md) | M05 — LLMs e Pipeline de Treino | Otimização por preferência: RLHF e PPO | 046 | ☐ não iniciada |
| [048](modulos/M05-llms-pipeline-de-treino/048-dpo-vs-ppo.md) | M05 — LLMs e Pipeline de Treino | DPO e comparação DPO vs PPO | 047 | ☐ não iniciada |
| [049](modulos/M05-llms-pipeline-de-treino/049-sampling-decodificacao.md) | M05 — LLMs e Pipeline de Treino | Sampling e decodificação: temperature, top-p e top-k | 044 | ☐ não iniciada |
| [050](modulos/M06-genai-prompt-apis/050-genai-multimodais.md) | M06 — GenAI Aplicado, Prompt Engineering e APIs | Panorama de GenAI e modelos multimodais | 044 | ☐ não iniciada |
| [051](modulos/M06-genai-prompt-apis/051-apis-provedores-llm.md) | M06 — GenAI Aplicado, Prompt Engineering e APIs | APIs de provedores de LLM: interface, autenticação, tokens e custo | 049, 050 | ☐ não iniciada |
| [052](modulos/M06-genai-prompt-apis/052-prompt-engineering-fundamentos.md) | M06 — GenAI Aplicado, Prompt Engineering e APIs | Prompt engineering: fundamentos e padrões | 051 | ☐ não iniciada |
| [053](modulos/M06-genai-prompt-apis/053-prompt-engineering-avancado.md) | M06 — GenAI Aplicado, Prompt Engineering e APIs | Prompt engineering avançado: few-shot, chain-of-thought e decomposição | 052 | ☐ não iniciada |
| [054](modulos/M06-genai-prompt-apis/054-saidas-estruturadas-json-mode.md) | M06 — GenAI Aplicado, Prompt Engineering e APIs | Saídas estruturadas e JSON mode | 051, 052 | ☐ não iniciada |
| [055](modulos/M07-rag-vector-dbs/055-rag-fundamentos.md) | M07 — RAG e Vector DBs | Fundamentos de RAG: motivação e arquitetura | 038, 051 | ☐ não iniciada |
| [056](modulos/M07-rag-vector-dbs/056-chunking-indexacao.md) | M07 — RAG e Vector DBs | Chunking e estratégias de indexação | 055 | ☐ não iniciada |
| [057](modulos/M07-rag-vector-dbs/057-pipeline-rag-basico.md) | M07 — RAG e Vector DBs | Pipeline RAG básico: retrieve-augment-generate | 056 | ☐ não iniciada |
| [058](modulos/M07-rag-vector-dbs/058-vector-databases.md) | M07 — RAG e Vector DBs | Vector databases (FAISS, pgvector) — por dentro | 038, 056 | ☐ não iniciada |
| [059](modulos/M07-rag-vector-dbs/059-rag-hibrido.md) | M07 — RAG e Vector DBs | RAG híbrido: denso + esparso (BM25) e fusão | 057, 058 | ☐ não iniciada |
| [060](modulos/M07-rag-vector-dbs/060-rag-multi-index-reranking.md) | M07 — RAG e Vector DBs | RAG multi-index e re-ranking | 059 | ☐ não iniciada |
| [061](modulos/M07-rag-vector-dbs/061-agentic-rag.md) | M07 — RAG e Vector DBs | Agentic RAG | 060 | ☐ não iniciada |
| [062](modulos/M08-agentes-autonomos/062-arquitetura-de-agentes.md) | M08 — Agentes Autônomos | Arquitetura de agentes | 053, 057 | ☐ não iniciada |
| [063](modulos/M08-agentes-autonomos/063-react.md) | M08 — Agentes Autônomos | Padrão ReAct (reason + act) | 062 | ☐ não iniciada |
| [064](modulos/M08-agentes-autonomos/064-plan-execute.md) | M08 — Agentes Autônomos | Padrão Plan-Execute | 063 | ☐ não iniciada |
| [065](modulos/M08-agentes-autonomos/065-reflection.md) | M08 — Agentes Autônomos | Padrão Reflection | 063 | ☐ não iniciada |
| [066](modulos/M08-agentes-autonomos/066-function-calling-tool-use.md) | M08 — Agentes Autônomos | Function calling / tool use | 054, 062 | ☐ não iniciada |
| [067](modulos/M08-agentes-autonomos/067-memoria-de-agentes.md) | M08 — Agentes Autônomos | Memória de agentes (curto/longo prazo) | 058, 062 | ☐ não iniciada |
| [068](modulos/M08-agentes-autonomos/068-gerenciamento-de-contexto.md) | M08 — Agentes Autônomos | Gerenciamento de contexto e janela de contexto | 067 | ☐ não iniciada |
| [069](modulos/M08-agentes-autonomos/069-orquestracao-langgraph.md) | M08 — Agentes Autônomos | Orquestração com LangGraph | 063, 064, 066 | ☐ não iniciada |
| [070](modulos/M08-agentes-autonomos/070-observabilidade-limites.md) | M08 — Agentes Autônomos | Observabilidade e limites de agentes | 069 | ☐ não iniciada |
| [071](modulos/M08-agentes-autonomos/071-multi-agente.md) | M08 — Agentes Autônomos | Sistemas multi-agente | 069 | ☐ não iniciada |
| [072](modulos/M09-mcp/072-mcp-fundamentos.md) | M09 — MCP | MCP: motivação e arquitetura cliente-servidor | 066 | ☐ não iniciada |
| [073](modulos/M09-mcp/073-mcp-primitivas.md) | M09 — MCP | Primitivas do MCP: resources, tools e prompts | 072 | ☐ não iniciada |
| [074](modulos/M09-mcp/074-mcp-jsonrpc.md) | M09 — MCP | O protocolo MCP sobre JSON-RPC 2.0 | 054, 073 | ☐ não iniciada |
| [075](modulos/M09-mcp/075-mcp-servidores-clientes-python.md) | M09 — MCP | Construindo servidores e clientes MCP em Python (simulado) | 073, 074 | ☐ não iniciada |
| [076](modulos/M10-fine-tuning-dados/076-preparacao-datasets-fine-tuning.md) | M10 — Fine-Tuning e Processamento de Dados | Preparação de datasets para fine-tuning | 046 | ☐ não iniciada |
| [077](modulos/M10-fine-tuning-dados/077-fine-tuning-completo.md) | M10 — Fine-Tuning e Processamento de Dados | Fine-tuning completo: quando e por quê | 046, 076 | ☐ não iniciada |
| [078](modulos/M10-fine-tuning-dados/078-lora-peft.md) | M10 — Fine-Tuning e Processamento de Dados | LoRA e PEFT: adaptação de baixo posto | 077 | ☐ não iniciada |
| [079](modulos/M10-fine-tuning-dados/079-fine-tuning-openai-api.md) | M10 — Fine-Tuning e Processamento de Dados | Fine-tuning via OpenAI API | 076, 077 | ☐ não iniciada |
| [080](modulos/M10-fine-tuning-dados/080-avaliacao-modelo-ajustado.md) | M10 — Fine-Tuning e Processamento de Dados | Avaliação do modelo ajustado e modelo de domínio | 077 | ☐ não iniciada |
| [081](modulos/M11-arquitetura-sistemas-ia/081-design-ai-first.md) | M11 — Arquitetura de Sistemas com IA | Design AI-First | 057, 062 | ☐ não iniciada |
| [082](modulos/M11-arquitetura-sistemas-ia/082-single-vs-multi-agente.md) | M11 — Arquitetura de Sistemas com IA | Single-agent vs multi-agente | 071, 081 | ☐ não iniciada |
| [083](modulos/M11-arquitetura-sistemas-ia/083-padroes-design-ia.md) | M11 — Arquitetura de Sistemas com IA | Padrões de projeto de IA | 082 | ☐ não iniciada |
| [084](modulos/M11-arquitetura-sistemas-ia/084-arquitetura-enterprise.md) | M11 — Arquitetura de Sistemas com IA | Arquitetura enterprise | 075, 083 | ☐ não iniciada |
| [085](modulos/M12-avaliacao-custo-latencia-llmops/085-evals-metodologia.md) | M12 — Avaliação, Custo/Latência e MLOps/LLMOps | Metodologia de avaliação e evals para sistemas LLM | 057, 062 | ☐ não iniciada |
| [086](modulos/M12-avaliacao-custo-latencia-llmops/086-metricas-datasets-avaliacao.md) | M12 — Avaliação, Custo/Latência e MLOps/LLMOps | Métricas e datasets de avaliação (offline/online) e LLM-as-judge | 085 | ☐ não iniciada |
| [087](modulos/M12-avaliacao-custo-latencia-llmops/087-custo-inferencia.md) | M12 — Avaliação, Custo/Latência e MLOps/LLMOps | Otimização de custo de inferência (alto volume e concorrência) | 051, 085 | ☐ não iniciada |
| [088](modulos/M12-avaliacao-custo-latencia-llmops/088-latencia-inferencia.md) | M12 — Avaliação, Custo/Latência e MLOps/LLMOps | Otimização de latência de inferência (streaming, percentis, Little's law) | 087 | ☐ não iniciada |
| [089](modulos/M12-avaliacao-custo-latencia-llmops/089-mlops-llmops-observabilidade.md) | M12 — Avaliação, Custo/Latência e MLOps/LLMOps | MLOps/LLMOps e observabilidade (tracing, SLOs e rollout canary) | 070, 086 | ☐ não iniciada |
| [090](modulos/M13-seguranca-governanca/090-interpretabilidade-explicabilidade.md) | M13 — Segurança e Governança em IA | Interpretabilidade e explicabilidade | 031, 085 | ☐ não iniciada |
| [091](modulos/M13-seguranca-governanca/091-vieses-fairness.md) | M13 — Segurança e Governança em IA | Vieses e fairness em IA | 090 | ☐ não iniciada |
| [092](modulos/M13-seguranca-governanca/092-riscos-seguranca.md) | M13 — Segurança e Governança em IA | Riscos e segurança: prompt injection, jailbreak e privacidade | 066, 090 | ☐ não iniciada |
| [093](modulos/M13-seguranca-governanca/093-legal-regulatorio-ia-responsavel.md) | M13 — Segurança e Governança em IA | Legal, regulatório e IA responsável | 091, 092 | ☐ não iniciada |
| [094](modulos/M13-seguranca-governanca/094-custos-sustentabilidade.md) | M13 — Segurança e Governança em IA | Gestão de custos e sustentabilidade de IA | 087 | ☐ não iniciada |
| [095](modulos/M14-ferramentas-aplicadas/095-ia-devops-i.md) | M14 — Ferramentas de IA Aplicadas | IA para DevOps I: copiloto de IaC, agentes para Kubernetes, troubleshooting, AIOps e ChatOps | 069 | ☐ não iniciada |
| [096](modulos/M14-ferramentas-aplicadas/096-ia-devops-ii.md) | M14 — Ferramentas de IA Aplicadas | IA para DevOps II: segurança/compliance, CI/CD, FinOps, RAG sobre runbooks e auto-remediação | 057, 095 | ☐ não iniciada |
| [097](modulos/M14-ferramentas-aplicadas/097-ia-ux-ui.md) | M14 — Ferramentas de IA Aplicadas | IA para UX & UI: geração de UI (text-to-UI), prototipação assistida e validação de fluxos | 050 | ☐ não iniciada |
| [098](modulos/M14-ferramentas-aplicadas/098-ia-gestao-projetos.md) | M14 — Ferramentas de IA Aplicadas | IA para Gestão de Projetos: requirements copilot, priorização (RICE/WSJF/MoSCoW), estimativas (Monte Carlo) e relatórios | 062 | ☐ não iniciada |
| [099](modulos/M15-capstone/099-capstone-planejamento-arquitetura.md) | M15 — Capstone | Capstone: planejamento e arquitetura do Micro-SaaS (RAG + agentes + MCP) | 061, 071, 075, 084 | ☐ não iniciada |
| [100](modulos/M15-capstone/100-capstone-implementacao-fluxo.md) | M15 — Capstone | Capstone: implementação, fluxo ponta-a-ponta e critérios de conclusão | 099 | ☐ não iniciada |
| [101](modulos/M16-carreira-entrevistas/101-mercado-papel-portfolio.md) | M16 — Carreira e Entrevistas para AI Engineer | O mercado e o papel do AI Engineer; portfólio | 100 | ☐ não iniciada |
| [102](modulos/M16-carreira-entrevistas/102-entrevistas-fundamentos-ml.md) | M16 — Carreira e Entrevistas para AI Engineer | Entrevistas — Fundamentos de ML | 013, 014, 016, 018, 020 | ☐ não iniciada |
| [103](modulos/M16-carreira-entrevistas/103-entrevistas-sistemas-ia.md) | M16 — Carreira e Entrevistas para AI Engineer | Entrevistas — Engenharia de sistemas de IA | 061, 071, 085, 088 | ☐ não iniciada |
| [104](modulos/M16-carreira-entrevistas/104-exercicios-entrevista-python.md) | M16 — Carreira e Entrevistas para AI Engineer | Exercícios de entrevista resolvidos em Python e simulação | 102, 103 | ☐ não iniciada |
<!-- FIM-LINHAS-LICOES -->
