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

## Instalação

```bash
git clone https://github.com/pedrowilian/trilha-engenharia-ia-aplicada.git
cd trilha-engenharia-ia-aplicada

# Dependências dos exemplos resolvidos e das soluções (numpy, matplotlib):
pip install -r trilha/requirements.txt

# Dependências do validador de conformidade (pyyaml, networkx, pytest, hypothesis):
pip install -r trilha/tools/requirements.txt
```

Em ambientes "externally managed" (Debian/Ubuntu recentes, etc.), use
`pip install --user --break-system-packages -r <arquivo>`.

## Como estudar — o ciclo completo

1. **Descubra onde retomar.** A lição atual fica marcada em
   [`trilha/README.md`](trilha/README.md) na linha "▶ Retomar em", ou rode:

   ```bash
   python3 trilha/tools/progresso.py retomar
   ```

2. **Marque a lição como em andamento** (opcional, mas ajuda a rastrear onde você está caso
   pare no meio):

   ```bash
   python3 trilha/tools/progresso.py set 013 em_andamento
   ```

3. **Estude a `Seção_Teórica`** da lição em `trilha/modulos/M<MM>-.../<NNN>-<slug>.md`
   (motivação → princípio de funcionamento → conceitos com exemplos resolvidos em Python).

4. **Resolva os exercícios** em `trilha/pratica/<NNN>-<slug>/exercicio_1.py`,
   `exercicio_2.py`, `exercicio_3.py`. Cada um começa como um esqueleto com
   `raise NotImplementedError` — o enunciado e o critério de aceite estão no docstring do
   próprio arquivo.

5. **Corrija o exercício** (veja a seção abaixo) e, quando os três exercícios da lição
   passarem, **marque como concluída** e avance:

   ```bash
   python3 trilha/tools/progresso.py set 013 concluida
   python3 trilha/tools/gerar_indice.py   # atualiza a tabela e o "▶ Retomar em" no índice
   ```

## Como corrigir um exercício

Não existe corretor automático que rode o seu código por você — o critério é **binário e
objetivo**: a saída do seu script precisa ser **exatamente igual** ao arquivo
`.saida.txt` da solução de referência.

```bash
# 1. Rode o seu exercício e veja a saída:
python3 trilha/pratica/013-gradient-descent/exercicio_1.py

# 2. Compare com a saída esperada (diff vazio = passou):
python3 trilha/pratica/013-gradient-descent/exercicio_1.py \
  | diff - trilha/solucoes/013-gradient-descent/solucao_1.saida.txt && echo "PASSOU"

# 3. Se travar, a solução de referência comentada está em:
cat trilha/solucoes/013-gradient-descent/solucao_1.py
```

Troque `013-gradient-descent` e `exercicio_1`/`solucao_1` pelo `<NNN>-<slug>` e número do
exercício da lição em que você estiver. Só espie a solução depois de tentar — o valor do
exercício está em travar, depurar e destravar sozinho.

## Como atualizar o progresso

O progresso de estudo (`nao_iniciada` / `em_andamento` / `concluida`, por lição) é **estado
mutável**, separado do conteúdo imutável das lições, guardado em
[`trilha/progresso.yaml`](trilha/progresso.yaml). Nunca edite esse arquivo à mão — use o
helper, que preserva o formato e os comentários-doc do arquivo:

| Comando | O que faz |
|---|---|
| `python3 trilha/tools/progresso.py set <NNN> <estado>` | Define o estado de uma lição (ex.: `set 013 concluida`). |
| `python3 trilha/tools/progresso.py get <NNN>` | Mostra o estado atual de uma lição. |
| `python3 trilha/tools/progresso.py listar` | Lista todas as lições com estado registrado. |
| `python3 trilha/tools/progresso.py retomar` | Mostra a próxima lição a estudar (primeira `em_andamento`, senão a primeira `nao_iniciada`). |

Depois de qualquer mudança em `progresso.yaml`, regenere o índice navegável para refletir os
novos ☑/◐/☐ e o novo ponto de retomada em `trilha/README.md`:

```bash
python3 trilha/tools/gerar_indice.py
# ou, só para checar se o índice está desatualizado sem escrever nada:
python3 trilha/tools/gerar_indice.py --check
```

## Capstone — projeto integrador (M15)

Um Micro-SaaS de suporte offline e determinístico (sem rede, sem LLM real) que integra RAG,
Agente e MCP num único fluxo ponta a ponta:

```bash
python3 trilha/capstone/src/main.py            # roda o fluxo completo, imprime evidência de cada componente
python3 -m pytest trilha/capstone/tests/       # teste de integração end-to-end
```

Detalhes de arquitetura em [`trilha/capstone/README.md`](trilha/capstone/README.md).

## Validação de conformidade

Toda lição segue o [`TEMPLATE-licao.md`](trilha/TEMPLATE-licao.md). Um validador Python
executa as soluções de referência, compara a saída com os `.saida.txt`, checa o DAG de
pré-requisitos, a cobertura de tópicos obrigatórios do currículo e a consistência com o mapa
de competências:

```bash
python3 trilha/tools/validar_trilha.py
```

Saída esperada com o repositório íntegro: `Trilha conforme: 104 lição(ões) verificada(s),
nenhuma não-conformidade.` Os testes de propriedade do próprio validador (Hypothesis) ficam
em `trilha/tools/tests/` e rodam com `python3 -m pytest trilha/tools/tests/`.

## Estrutura do repositório

```
trilha/
├── modulos/         # as 104 lições (teoria + exemplos resolvidos), M00 a M16
├── pratica/         # exercícios em Python de cada lição (espelha modulos/)
├── solucoes/        # soluções de referência + saída esperada (espelha pratica/)
├── capstone/        # projeto integrador: Micro-SaaS com RAG + Agente + MCP
├── tools/           # validador, gerador de índice, helper de progresso (+ testes)
├── competencias.yaml
├── progresso.yaml   # estado de estudo (nao_iniciada / em_andamento / concluida)
└── TEMPLATE-licao.md
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

## Licença

Distribuído sob a licença [MIT](LICENSE).
