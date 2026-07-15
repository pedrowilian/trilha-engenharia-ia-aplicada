# Trilha de Engenharia de IA Aplicada

Currículo autoral, **teoria-primeiro**, do fundamento absoluto ao avançado, com prática em
**Python** ao fim de cada lição. Uma lição = um único tópico. Estudo sequencial, sem deixar
nada solto.

**104 lições em 17 módulos (M00 → M16)** — de álgebra linear e fundamentos de ML até LLMs,
RAG, agentes autônomos, MCP, fine-tuning e arquitetura de sistemas com IA em produção.

## Por onde começar

- [`trilha/README.md`](trilha/README.md) — índice navegável das 104 lições, com pré-requisitos
  e estado de conclusão.
- [`trilha/EMENTA.md`](trilha/EMENTA.md) — ementa detalhada, com a descrição de cada aula.
- [`trilha/mapa-de-competencias.md`](trilha/mapa-de-competencias.md) — como cada lição se
  conecta às exigências reais do cargo de AI Engineer.

## Estrutura do repositório

```
trilha/
├── modulos/         # as 104 lições (teoria + exemplos resolvidos), M00 a M16
├── pratica/         # exercícios em Python de cada lição (espelha modulos/)
├── solucoes/        # soluções de referência + saída esperada (espelha pratica/)
├── capstone/        # projeto integrador: Micro-SaaS com RAG + Agente + MCP
├── tools/           # validador de conformidade da trilha (+ testes com Hypothesis)
├── competencias.yaml
├── progresso.yaml   # estado de estudo (nao_iniciada / em_andamento / concluida)
└── TEMPLATE-licao.md

.kiro/specs/trilha-engenharia-ia/   # requirements, design e plano de tarefas que geraram a trilha
```

## Visão geral dos módulos

| Módulo | Tema |
|--------|------|
| M00 | Fundamentos Matemáticos |
| M01 | Fundamentos de Machine Learning |
| M02 | Redes Neurais e Deep Learning |
| M03 | NLP, Tokenização, Embeddings e Busca Vetorial |
| M04 | Transformers por dentro |
| M05 | LLMs e Pipeline de Treino |
| M06 | GenAI Aplicado, Prompt Engineering e APIs |
| M07 | RAG e Vector DBs |
| M08 | Agentes Autônomos |
| M09 | MCP (Model Context Protocol) |
| M10 | Fine-Tuning e Processamento de Dados |
| M11 | Arquitetura de Sistemas com IA |
| M12 | Avaliação, Custo/Latência e MLOps/LLMOps |
| M13 | Segurança e Governança em IA |
| M14 | Ferramentas de IA Aplicadas (DevOps/UX/PM) |
| M15 | Capstone — Projeto Integrador |
| M16 | Carreira e Entrevistas para AI Engineer |

## Validação de conformidade

Toda lição segue o [`TEMPLATE-licao.md`](trilha/TEMPLATE-licao.md) e é verificada por um
validador Python que checa o DAG de pré-requisitos, a cobertura de tópicos obrigatórios e o
mapa de competências:

```bash
pip install -r trilha/tools/requirements.txt
python3 trilha/tools/validar_trilha.py
```

## Licença

Distribuído sob a licença [MIT](LICENSE).
