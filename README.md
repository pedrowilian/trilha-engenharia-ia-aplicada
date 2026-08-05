<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/brand/teia-lockup-dark.svg">
    <img alt="TEIA — Trilha de Engenharia de IA Aplicada" src="assets/brand/teia-lockup-light.svg" width="420">
  </picture>
</p>

<h1 align="center">Trilha de Engenharia de IA Aplicada</h1>

<p align="center">
  <strong>104 lições em 17 módulos</strong> — do fundamento matemático absoluto a LLMs, RAG,<br>
  agentes autônomos, MCP e arquitetura de sistemas com IA em produção.<br>
  Teoria-primeiro, prática em Python ao fim de cada lição.
</p>

<p align="center">
  <a href="https://github.com/pedrowilian/trilha-engenharia-ia-aplicada/actions/workflows/ci.yml"><img alt="CI" src="https://img.shields.io/github/actions/workflow/status/pedrowilian/trilha-engenharia-ia-aplicada/ci.yml?branch=main&style=flat-square&label=CI"></a>
  <a href="trilha/README.md"><img alt="104 lições" src="https://img.shields.io/badge/li%C3%A7%C3%B5es-104-22D3EE?style=flat-square"></a>
  <a href="#instalação"><img alt="Python 3.11+" src="https://img.shields.io/badge/python-3.11%2B-7DD3FC?style=flat-square"></a>
  <a href=".github/CONTRIBUTING.md"><img alt="PRs bem-vindos" src="https://img.shields.io/badge/PRs-bem--vindos-22D3EE?style=flat-square"></a>
  <a href="LICENSE"><img alt="Licença MIT" src="https://img.shields.io/badge/licen%C3%A7a-MIT-6E7681?style=flat-square"></a>
</p>

---

## O que é

Um currículo autoral e completo de Engenharia de IA, escrito para ser estudado do começo
ao fim, sem lacunas e sem pré-requisito implícito. Não é uma lista de links: cada uma das
104 lições é um documento fechado, com teoria, exemplos resolvidos em Python, exercícios e
solução de referência executável.

**Uma lição = um único tópico.** Estudo sequencial, sem deixar nada solto.

### Por que teoria-primeiro

A maior parte do material de IA aplicada começa na API e nunca volta para o fundamento —
você aprende a chamar um endpoint sem saber o que é atenção, por que o embedding tem a
dimensão que tem, ou o que a temperatura faz na distribuição. Quando o sistema falha em
produção, não há de onde puxar o diagnóstico.

Aqui a ordem é a inversa e é deliberada:

1. **Motivação** — que problema real existe antes da técnica.
2. **Princípio de funcionamento** — por que a técnica resolve, na matemática.
3. **Conceitos com exemplos resolvidos** — o mecanismo em Python, executável.
4. **Prática** — três exercícios com critério de aceite objetivo.

O preço é começar por álgebra linear e cálculo em vez de pela primeira chamada de LLM. O
retorno é chegar em M08 (agentes) entendendo o que está acontecendo por dentro.

### O que garante que a trilha é íntegra

O currículo é verificado por código, não por revisão manual. Um validador Python executa
todas as soluções de referência, compara a saída com o esperado, checa o DAG de
pré-requisitos entre as 104 lições, a cobertura dos tópicos obrigatórios e a consistência
com o mapa de competências — e roda no [CI](.github/workflows/ci.yml) a cada push.

## Instalação

Requer **Python 3.11+**.

```bash
git clone https://github.com/pedrowilian/trilha-engenharia-ia-aplicada.git
cd trilha-engenharia-ia-aplicada
pip install -r trilha/requirements.txt -r trilha/tools/requirements.txt
```

<details>
<summary>O que cada arquivo de dependências instala (e o que fazer em ambiente "externally managed")</summary>

- [`trilha/requirements.txt`](trilha/requirements.txt) — dependências de **estudo**: `numpy`
  (exemplos e soluções) e `matplotlib` (geração reprodutível das figuras das lições).
- [`trilha/tools/requirements.txt`](trilha/tools/requirements.txt) — dependências do
  **tooling**: `pyyaml`, `networkx`, `pytest`, `hypothesis`.

Em ambientes "externally managed" (Debian/Ubuntu recentes, etc.):

```bash
pip install --user --break-system-packages -r trilha/requirements.txt -r trilha/tools/requirements.txt
```

</details>

## Comece por aqui

```bash
python3 trilha/tools/progresso.py retomar
```

Isso imprime a próxima lição a estudar. Daí em diante:

| Documento | Para quê |
|---|---|
| [`trilha/README.md`](trilha/README.md) | **Índice navegável** das 104 lições, com pré-requisitos e estado de conclusão (☑ / ◐ / ☐). |
| [`trilha/EMENTA.md`](trilha/EMENTA.md) | Ementa detalhada, com a descrição de cada aula. |
| [`trilha/mapa-de-competencias.md`](trilha/mapa-de-competencias.md) | Como cada lição se conecta às exigências reais do cargo de AI Engineer. |
| [`trilha/TEMPLATE-licao.md`](trilha/TEMPLATE-licao.md) | A estrutura que toda lição obedece — e que o validador cobra. |

## Mapa dos 17 módulos

| Módulo | Tema | Lições | Aulas |
|---|---|:---:|:---:|
| **M00** | Fundamentos Matemáticos | 10 | 001–010 |
| **M01** | Fundamentos de Machine Learning | 11 | 011–021 |
| **M02** | Redes Neurais e Deep Learning | 10 | 022–031 |
| **M03** | NLP, Tokenização, Embeddings e Busca Vetorial | 7 | 032–038 |
| **M04** | Transformers por dentro | 5 | 039–043 |
| **M05** | LLMs e Pipeline de Treino | 6 | 044–049 |
| **M06** | GenAI Aplicado, Prompt Engineering e APIs | 5 | 050–054 |
| **M07** | RAG e Vector DBs | 7 | 055–061 |
| **M08** | Agentes Autônomos | 10 | 062–071 |
| **M09** | MCP (Model Context Protocol) | 4 | 072–075 |
| **M10** | Fine-Tuning e Processamento de Dados | 5 | 076–080 |
| **M11** | Arquitetura de Sistemas com IA | 4 | 081–084 |
| **M12** | Avaliação, Custo/Latência e MLOps/LLMOps | 5 | 085–089 |
| **M13** | Segurança e Governança em IA | 5 | 090–094 |
| **M14** | Ferramentas de IA Aplicadas (DevOps/UX/PM) | 4 | 095–098 |
| **M15** | Capstone — Projeto Integrador | 2 | 099–100 |
| **M16** | Carreira e Entrevistas para AI Engineer | 4 | 101–104 |

## Como estudar

<details>
<summary><strong>O ciclo completo de uma lição</strong> — descobrir onde retomar, estudar, resolver, concluir</summary>

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

5. **Corrija o exercício** (veja abaixo) e, quando os três exercícios da lição passarem,
   **marque como concluída** e avance:

   ```bash
   python3 trilha/tools/progresso.py set 013 concluida
   python3 trilha/tools/gerar_indice.py   # atualiza a tabela e o "▶ Retomar em" no índice
   ```

</details>

<details>
<summary><strong>Como corrigir um exercício</strong> — o critério é binário e objetivo</summary>

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

</details>

<details>
<summary><strong>Como atualizar o progresso</strong> — helper de estado e regeneração do índice</summary>

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

</details>

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

Os quatro comandos que o CI executa, para rodar localmente antes de abrir um PR:

```bash
python3 trilha/tools/validar_trilha.py
python3 -m pytest trilha/tools/tests/
python3 -m pytest trilha/capstone/tests/
python3 trilha/tools/gerar_indice.py --check
```

## Estrutura do repositório

```
assets/brand/        # identidade visual TEIA (ver BRANDING.md)
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

## Contribuindo

Correção de erro de conteúdo, melhoria de explicação e ajuste de tooling são bem-vindos.
Veja [`CONTRIBUTING.md`](.github/CONTRIBUTING.md) para o padrão de lição, o formato de
commit e o que rodar antes de abrir o PR — e o
[Código de Conduta](.github/CODE_OF_CONDUCT.md).

Para reportar algo sem abrir PR, use os
[templates de issue](https://github.com/pedrowilian/trilha-engenharia-ia-aplicada/issues/new/choose).

## Identidade visual

A marca **TEIA** (logo, paleta, wordmark) está documentada em [`BRANDING.md`](BRANDING.md),
com a geometria exata do símbolo e as regras de uso. Os assets ficam em
[`assets/brand/`](assets/brand/).

## Licença

Distribuído sob a licença [MIT](LICENSE). Projeto pessoal e open source — feito para ser
usado, forkado e melhorado.
