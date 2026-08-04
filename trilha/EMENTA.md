# Ementa Detalhada — Trilha de Engenharia de IA Aplicada

> Currículo autoral, **teoria-primeiro**, do zero ao avançado, com prática em **Python** ao fim de cada aula.
> Uma aula = um único assunto. Estudo sequencial, sem deixar nada solto.
>
> **Formato de cada aula:** Teoria (motivação → princípio de funcionamento → conceitos com exemplos resolvidos em Python) → Prática (exercícios com solução de referência e critério objetivo de "passou/não passou").
>
> **Legenda:** `Δ` = aprofundamento teórico que vai **além** da ementa de referência (UNIPDS).
> **Total: 104 aulas em 17 módulos (M00 → M16).**

---

## Visão geral dos módulos

| Módulo | Tema | Aulas |
|--------|------|-------|
| M00 | Fundamentos Matemáticos | 001–010 |
| M01 | Fundamentos de Machine Learning | 011–021 |
| M02 | Redes Neurais e Deep Learning | 022–031 |
| M03 | NLP, Tokenização, Embeddings e Busca Vetorial | 032–038 |
| M04 | Transformers por dentro | 039–043 |
| M05 | LLMs e Pipeline de Treino | 044–049 |
| M06 | GenAI Aplicado, Prompt Engineering e APIs | 050–054 |
| M07 | RAG e Vector DBs | 055–061 |
| M08 | Agentes Autônomos | 062–071 |
| M09 | MCP (Model Context Protocol) | 072–075 |
| M10 | Fine-Tuning e Processamento de Dados | 076–080 |
| M11 | Arquitetura de Sistemas com IA | 081–084 |
| M12 | Avaliação, Custo/Latência e MLOps/LLMOps | 085–089 |
| M13 | Segurança e Governança em IA | 090–094 |
| M14 | Ferramentas de IA Aplicadas (DevOps/UX/PM) | 095–098 |
| M15 | Capstone — Projeto Integrador | 099–100 |
| M16 | Carreira e Entrevistas para AI Engineer | 101–104 |

---

## M00 — Fundamentos Matemáticos
*A base de tudo. Sem isso, transformers e treino de modelos viram "caixa-preta". Aqui construímos a intuição matemática que sustenta o resto da trilha.*

- **001 — Vetores e espaços vetoriais** `Δ` — O que é um vetor, espaço vetorial, combinação linear e base. Por que dados viram vetores. Prática: operações com `numpy`.
- **002 — Matrizes e operações matriciais** `Δ` — Multiplicação, transposta, identidade, inversa. A matriz como transformação de dados.
- **003 — Transformações lineares e multiplicação matriz-vetor** `Δ` — Como uma camada de rede neural é, no fundo, uma transformação linear.
- **004 — Autovalores, autovetores, SVD/PCA (intuição)** `Δ` — Decomposição, redução de dimensionalidade e a intuição por trás de embeddings.
- **005 — Normas, produto interno e distâncias** `Δ` — Cosseno, L2, dot product — a base matemática da busca semântica.
- **006 — Funções, limites e derivadas** `Δ` — Taxa de variação; o que "otimizar" significa de fato.
- **007 — Derivadas parciais, gradiente e regra da cadeia** `Δ` — O motor do aprendizado: como o gradiente aponta a direção de melhora. Base do backpropagation.
- **008 — Probabilidade e distribuições** `Δ` — Incerteza, distribuições, Bayes. Por que modelos "preveem probabilidades".
- **009 — Estatística descritiva e inferência** `Δ` — Amostragem, estimação, significância — base de avaliação e testes A/B.
- **010 — Verossimilhança, entropia e divergência KL** `Δ` — As funções de perda dos modelos modernos nascem daqui.

## M01 — Fundamentos de Machine Learning
*O coração do "porquê". Tudo que entra em entrevista de fundamentos e sustenta deep learning.*

- **011 — O que é ML: supervisionado, não-supervisionado, RL** `Δ` — Taxonomia, quando usar cada um, formulação de um problema de ML.
- **012 — Funções de perda (MSE, cross-entropy)** `Δ` — Como o modelo "mede o erro"; ligação com verossimilhança e entropia.
- **013 — Gradient descent (batch, mini-batch, SGD)** `Δ` — A regra de atualização θ ← θ − η∇L; efeito da taxa de aprendizado; convergência.
- **014 — Backpropagation** `Δ` — Como o gradiente flui pela rede; a regra da cadeia em ação.
- **015 — Regularização (L1/L2, dropout, early stopping)** `Δ` — Como evitar decorar os dados.
- **016 — Trade-off viés-variância** `Δ` — O dilema central do ML (cai em entrevista). 
- **017 — Overfitting/underfitting e validação cruzada** `Δ` — Diagnóstico e protocolo de validação honesto.
- **018 — Calibração de modelos** `Δ` — Quando "90% de confiança" realmente significa 90% (cai em entrevista).
- **019 — Desbalanceamento de classes** `Δ` — Métricas além da acurácia; reamostragem; class weights.
- **020 — Data leakage** `Δ` — O erro silencioso que infla resultados (cai em entrevista).
- **021 — Metodologia de experimentação e testes A/B** `Δ` — Como medir melhoria de verdade, sem se enganar.

## M02 — Redes Neurais e Deep Learning
*Do neurônio à rede profunda. Aqui o "gradient explosion" e companhia aparecem na prática.*

- **022 — Perceptron e o neurônio artificial** `Δ` — A unidade básica; limites do perceptron.
- **023 — Funções de ativação (sigmoid, tanh, ReLU, GELU)** `Δ` — Por que precisamos de não-linearidade.
- **024 — Multi-Layer Perceptron (MLP)** `Δ` — Empilhar camadas; aproximação universal; forward pass.
- **025 — Treinamento de redes profundas e inicialização de pesos** `Δ` — Por que inicialização importa (Xavier, He).
- **026 — Normalização: batch norm e layer norm** `Δ` — Estabilizar o treino; layer norm é base do transformer.
- **027 — Vanishing e exploding gradients** `Δ` — O problema do gradient explosion (cai em entrevista) e como mitigar.
- **028 — Otimizadores: momentum, RMSProp, Adam** `Δ` — Além do SGD puro.
- **029 — Redes Convolucionais (CNN): convolução e pooling** `Δ` — Visão computacional; campos receptivos.
- **030 — Redes Recorrentes: RNN, LSTM, GRU** `Δ` — Sequências e memória; limitações que motivam o transformer.
- **031 — Arquiteturas profundas e transfer learning** `Δ` — Reaproveitar conhecimento; pré-treino → fine-tuning.

## M03 — NLP, Tokenização, Embeddings e Busca Vetorial
*Como texto vira número e como achamos "significado". Base do RAG e dos LLMs.*

- **032 — Fundamentos de NLP e representação de texto** `Δ` — Do bag-of-words ao denso; pipeline clássico.
- **033 — Tokenização: BPE, WordPiece, SentencePiece** `Δ` — Como o texto é fatiado em tokens. **Exercício round-trip** (parse→serialize→parse).
- **034 — Embeddings: word2vec, GloVe, contextuais** `Δ` — Vetores com significado; por que "rei − homem + mulher ≈ rainha".
- **035 — Métricas de distância e similaridade (cosseno, L2, dot)** `Δ` — Como comparar significado.
- **036 — Busca vetorial e k-NN exato** `Δ` — Encontrar os vizinhos mais próximos.
- **037 — Busca aproximada (ANN) e trade-offs recall/latência** `Δ` — Por que produção não usa busca exata.
- **038 — HNSW por dentro** `Δ` — O algoritmo que move os vector DBs modernos.

## M04 — Transformers por dentro
*O núcleo absoluto da IA generativa moderna — explicado a fundo, não citado de passagem.*

- **039 — Limitações de RNNs e a motivação para atenção** `Δ` — Por que precisávamos de algo novo.
- **040 — Self-attention com Query/Key/Value** `Δ` — O mecanismo central, com a matemática de Q/K/V.
- **041 — Positional encoding** `Δ` — Como o modelo sabe a ordem das palavras.
- **042 — Multi-head attention** `Δ` — Múltiplas "perspectivas" de atenção em paralelo.
- **043 — Arquitetura completa do Transformer (encoder/decoder, FFN, residual)** `Δ` — Montando tudo num bloco e numa pilha.

## M05 — LLMs e Pipeline de Treino
*Como um LLM nasce: do pré-treino ao alinhamento. Inclui o que a ementa de referência não cobre (DPO vs PPO).*

- **044 — O que são LLMs: modelagem de linguagem e escala** `Δ` — Next-token prediction; leis de escala.
- **045 — Pré-treinamento** `Δ` — Treinar em larga escala; objetivo, dados, custo.
- **046 — Instruction tuning / SFT** `Δ` — Transformar um modelo cru em um assistente.
- **047 — Otimização por preferência: RLHF e PPO** `Δ` — Alinhar o modelo a preferências humanas.
- **048 — DPO e comparação DPO vs PPO** `Δ` — Por que DPO substituiu PPO em muitos labs (cai em entrevista).
- **049 — Sampling e decodificação: temperature, top-p, top-k** `Δ` — Como o modelo escolhe a próxima palavra; controle de criatividade.

## M06 — GenAI Aplicado, Prompt Engineering e APIs
*Do conhecimento teórico ao uso prático das APIs e à arte/ciência do prompt.*

- **050 — Panorama de GenAI e modelos multimodais** — Texto, imagem, áudio, vídeo; quando usar cada um.
- **051 — APIs de provedores de LLM (interface, autenticação, custos)** — OpenAI, Anthropic, Gemini; tokens e custo.
- **052 — Prompt engineering: fundamentos e padrões** — Estrutura de um bom prompt.
- **053 — Prompt engineering avançado: few-shot, CoT, decomposição** `Δ` — Técnicas que aumentam precisão e reduzem alucinação.
- **054 — Saídas estruturadas e JSON mode** `Δ` — Forçar saídas confiáveis. **Exercício round-trip** (parse↔serialize).

## M07 — RAG e Vector DBs
*Dar memória e fontes ao modelo. Um dos pilares mais cobrados em vagas.*

- **055 — Fundamentos de RAG: motivação e arquitetura** — Por que RAG; quando é a escolha certa (e quando não é).
- **056 — Chunking e estratégias de indexação** `Δ` — Como fatiar documentos sem perder contexto.
- **057 — Pipeline RAG básico: retrieve-augment-generate** — O fluxo ponta a ponta.
- **058 — Vector databases (FAISS, pgvector, etc.)** `Δ` — Onde e como guardar embeddings.
- **059 — RAG híbrido: denso + esparso (BM25) e fusão** `Δ` — Combinar busca semântica e por palavra-chave.
- **060 — RAG multi-index e re-ranking** `Δ` — Melhorar a precisão da recuperação.
- **061 — Agentic RAG** `Δ` — Quando o próprio agente decide o que e como buscar.

## M08 — Agentes Autônomos
*Sistemas que raciocinam, usam ferramentas e agem. O tema mais quente do mercado atual.*

- **062 — Arquitetura de agentes** — Loop percepção→raciocínio→ação→feedback; planner, executor, memória, toolbox.
- **063 — Padrão ReAct (reason + act)** — Raciocínio + ação intercalados.
- **064 — Padrão Plan-Execute** `Δ` — Decompor o objetivo e executar de forma estruturada.
- **065 — Padrão Reflection** `Δ` — Autoavaliação e correção do próprio comportamento.
- **066 — Function calling / tool use** — Como o LLM chama funções. **Exercício round-trip** (JSON).
- **067 — Memória de agentes (curto/longo prazo)** `Δ` — Memória episódica, contextual; recuperação via embeddings.
- **068 — Gerenciamento de contexto e janela de contexto** `Δ` — Context pruning/stitching; orçamento de tokens.
- **069 — Orquestração com LangGraph** — Grafos de execução, roteamento, fallback, retry.
- **070 — Observabilidade e limites de agentes** `Δ` — Guardrails, human-in-the-loop, prevenção de runaway loops.
- **071 — Sistemas multi-agente** — Supervisor, hierárquico, group chat, delegação, consenso.

## M09 — MCP (Model Context Protocol)
*O protocolo que padroniza a conexão entre LLMs e o mundo (APIs, dados, serviços).*

- **072 — Fundamentos do MCP: motivação e arquitetura cliente-servidor** — Que problema o MCP resolve.
- **073 — Primitivas do MCP: resources, tools, prompts** `Δ` — Os blocos de construção.
- **074 — Protocolo MCP e mensagens JSON-RPC** `Δ` — O protocolo por dentro. **Exercício round-trip**.
- **075 — Construindo servidores e clientes MCP em Python** — Mão na massa do zero.

## M10 — Fine-Tuning e Processamento de Dados
*Quando e como customizar um modelo para um domínio específico.*

- **076 — Preparação de datasets para fine-tuning** — Coleta, limpeza, formato JSONL, qualidade/diversidade.
- **077 — Fine-tuning completo: quando e por quê** — Decision framework: RAG vs fine-tuning (cai em entrevista).
- **078 — LoRA / PEFT** `Δ` — Fine-tuning eficiente; trade-offs de parametrização.
- **079 — Fine-tuning via OpenAI API** — Upload, treino, hiperparâmetros, monitoramento.
- **080 — Avaliação do modelo ajustado e modelo de domínio customizado** — Métricas, A/B, overfitting/perda de generalização.

## M11 — Arquitetura de Sistemas com IA
*Projetar sistemas de IA reais, em produção, com trade-offs conscientes.*

- **081 — Design AI-First** `Δ` — IA vs regras determinísticas; trade-offs latência/precisão/custo.
- **082 — Arquiteturas single-agent vs multi-agente** — Quando usar cada uma.
- **083 — Padrões de projeto específicos de IA** `Δ` — Model router, semantic cache, HITL, approval gates.
- **084 — Arquitetura corporativa (enterprise) e escalabilidade** `Δ` — API Gateway → orquestração → serviços → observabilidade; model tiering.

## M12 — Avaliação, Custo/Latência e MLOps/LLMOps
*O que separa um protótipo de um sistema de produção confiável e barato.*

- **085 — Metodologia de avaliação e evals para sistemas LLM** `Δ` — Como medir qualidade de saída de forma sistemática.
- **086 — Métricas e datasets de avaliação (offline/online)** `Δ` — Construir um framework de avaliação.
- **087 — Otimização de custo de inferência (alto volume/concorrência)** `Δ` — Cache, batching, escolha de modelo.
- **088 — Otimização de latência de inferência** `Δ` — Streaming, quantização, estratégias de servir.
- **089 — MLOps / LLMOps e observabilidade** `Δ` — Rastreamento de prompts, logs, métricas, deploy.

## M13 — Segurança e Governança em IA
*Responsabilidade, risco e conformidade — cada vez mais exigido, especialmente em times de governança.*

- **090 — Interpretabilidade e explicabilidade** `Δ` — Abrir a caixa-preta; por que o modelo decidiu aquilo.
- **091 — Vieses e fairness em IA** `Δ` — Detecção e mitigação de vieses.
- **092 — Riscos e segurança: prompt injection, jailbreak, privacidade** `Δ` — Ataques e defesas; verificação de saídas.
- **093 — Legal, regulatório e IA responsável (governança)** `Δ` — LGPD/AI Act; frameworks de governança.
- **094 — Gestão de custos e sustentabilidade de IA** `Δ` — Custo financeiro e ambiental dos modelos.

## M14 — Ferramentas de IA Aplicadas (DevOps / UX / Gestão de Projetos)
*Aplicações práticas no dia a dia de engenharia — alinhado ao escopo do seu time.*

- **095 — IA para DevOps I** — Copiloto de IaC, agentes para Kubernetes, troubleshooting, AIOps, ChatOps.
- **096 — IA para DevOps II** — Segurança/compliance, CI/CD, FinOps, RAG sobre runbooks, auto-remediação.
- **097 — IA para UX & UI** — Geração de UI, prototipação assistida, validação de fluxos.
- **098 — IA para Gestão de Projetos** — Requirements copilot, priorização, estimativas, relatórios.

## M15 — Capstone: Projeto Integrador
*Consolidação: construir um Micro-SaaS real integrando tudo.*

- **099 — Capstone: planejamento e arquitetura do Micro-SaaS (RAG + agentes + MCP)** — Problema, escopo, arquitetura, critérios de conclusão por componente.
- **100 — Capstone: implementação, fluxo ponta-a-ponta e critérios de conclusão** — RAG + agentes + MCP num único fluxo em Python, com teste de integração.

## M16 — Carreira e Entrevistas para AI Engineer
*Converter o conhecimento em vaga e progressão.*

- **101 — O mercado e o papel do AI Engineer; portfólio** — Níveis (Junior → Principal), GitHub, marca pessoal.
- **102 — Entrevistas — Fundamentos de ML** `Δ` — ≥10 questões: viés-variância, calibração, data leakage, gradient descent/backprop.
- **103 — Entrevistas — Engenharia de sistemas de IA** `Δ` — ≥10 questões: RAG, agentes, evals, custo/latência, system design.
- **104 — Exercícios de entrevista resolvidos em Python e simulação** `Δ` — Live coding, problem solving, simulação completa.

---

## Como vamos estudar

1. Seguimos **na ordem numerada** (001 → 104). Cada aula tem pré-requisitos garantidos nas aulas anteriores.
2. Em cada aula: você lê a **teoria** (com exemplos resolvidos em Python), depois faz a **prática** (exercícios com solução de referência e critério objetivo de "passou/não passou").
3. Você estuda, **faz perguntas**, e quando se sentir seguro marca a aula como concluída no índice de progresso.
4. As aulas marcadas com `Δ` são aprofundamentos teóricos que vão **além** da ementa de referência — é onde está boa parte do seu diferencial.

> Esta ementa é a visão de estudo. A estrutura técnica completa está no repositório: o
> template de aula em [`TEMPLATE-licao.md`](TEMPLATE-licao.md), o mapa de competências em
> [`mapa-de-competencias.md`](mapa-de-competencias.md) e a validação automatizada em
> [`tools/validar_trilha.py`](tools/validar_trilha.py).
