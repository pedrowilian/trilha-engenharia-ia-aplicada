# Como contribuir

Obrigado por olhar o código e o conteúdo. Este é um projeto **pessoal e open source**, e
vai continuar aberto ao público. Contribuição é bem-vinda — desde que respeite as duas
invariantes que dão valor à trilha: **cada lição é autossuficiente** e **nada usa conceito
que não tenha sido ensinado antes**.

## O que ajuda mais

Em ordem de impacto:

1. **Erro de conteúdo** — matemática errada, explicação que induz a conclusão falsa, código
   de exemplo que não roda, solução de referência cuja saída não bate com o `.saida.txt`.
   Isso propaga para todas as lições que dependem da lição errada, então é o achado mais
   valioso.
2. **Explicação confusa** — o conteúdo está correto mas não ensina. Diga onde travou e o
   que faltou.
3. **Tooling** — bug ou melhoria no validador, no gerador de índice, no helper de progresso
   ou no capstone.
4. **Lição nova ou reordenação** — abra uma issue **antes** do PR. Mexer no currículo mexe
   no DAG de pré-requisitos e nos ordinais de todas as lições seguintes; vale alinhar o
   desenho primeiro.

## Antes de qualquer coisa: rode o CI localmente

```bash
git clone https://github.com/pedrowilian/trilha-engenharia-ia-aplicada.git
cd trilha-engenharia-ia-aplicada
pip install -r trilha/requirements.txt -r trilha/tools/requirements.txt

python3 trilha/tools/validar_trilha.py       # conformidade das 104 lições
python3 -m pytest trilha/tools/tests/        # testes do validador
python3 -m pytest trilha/capstone/tests/     # integração do capstone
python3 trilha/tools/gerar_indice.py --check # índice em dia
```

Se algum desses falha **antes** da sua mudança, isso já é uma issue de tooling — reporte em
vez de contornar.

## O padrão de lição

A fonte da verdade do formato é [`trilha/TEMPLATE-licao.md`](../trilha/TEMPLATE-licao.md),
que é ao mesmo tempo a especificação e um caso de teste do validador. Leia antes de editar
qualquer lição. O que o validador cobra, em resumo:

**Front-matter YAML**

- `id`, `ordinal` (único e global), `modulo`, `titulo`, `slug`
- `pre_requisitos`: lista de `id`s, **todos com `ordinal` menor** que o da lição atual —
  é isso que mantém o DAG acíclico e sem dependência "para frente"
- 1 a 5 `objetivos_de_aprendizagem`, escritos como comportamento observável
- `tempo_estimado_min` ≤ 60
- `competencias`, `conceitos_centrais`, `classificacao_ementa`

**Corpo**

- exatamente uma `Seção_Teórica`, seguida de exatamente uma `Seção_Prática` — os nomes
  dessas seções **não** podem ser renomeados
- a teoria abre com **Motivação** e **Princípio de funcionamento**
- ≥ 3 `Exemplos_Resolvidos`, com pelo menos um por conceito central; cada um com código
  Python, explicação bloco a bloco e a saída esperada
- ≥ 3 exercícios na prática, cada um com critério de aceite **binário**, solução de
  referência e `.saida.txt`

**Convenções de formatação**

- matemática em LaTeX (`$...$` inline, `$$...$$` em destaque), renderizável pelo KaTeX do
  VS Code. **Nunca** matemática dentro de bloco de código.
- bloco ` ```python ` só para código Python e saída de programa.
- figuras não são desenhadas à mão: são geradas por
  `trilha/tools/figuras/gerar_figuras_m<MM>.py` (matplotlib, backend `Agg`, sementes
  fixas), salvas em `modulos/M<MM>-<slug>/assets/<NNN>-<slug>/` e incluídas por caminho
  relativo. Figura nova exige o script que a gera.

### Se você mexer em exercício ou solução

Os três arquivos andam juntos e precisam continuar consistentes:

```
trilha/pratica/<NNN>-<slug>/exercicio_N.py     # esqueleto com raise NotImplementedError
trilha/solucoes/<NNN>-<slug>/solucao_N.py      # solução de referência comentada
trilha/solucoes/<NNN>-<slug>/solucao_N.saida.txt  # saída EXATA da solução
```

O `.saida.txt` é gerado pela execução da solução, nunca escrito à mão:

```bash
python3 trilha/solucoes/013-gradient-descent/solucao_1.py \
  > trilha/solucoes/013-gradient-descent/solucao_1.saida.txt
```

Saída precisa ser **determinística** — semente de RNG fixa, sem timestamp, sem caminho
absoluto, sem ordem de dicionário/set dependente de hash. O validador executa a solução e
compara byte a byte.

### Não edite estes arquivos à mão

- [`trilha/README.md`](../trilha/README.md) — gerado por `trilha/tools/gerar_indice.py`
- [`trilha/progresso.yaml`](../trilha/progresso.yaml) — use
  `python3 trilha/tools/progresso.py set <NNN> <estado>`

Progresso de estudo é estado local seu. **Não** inclua mudança de `progresso.yaml` (nem o
`trilha/README.md` regenerado por causa dela) num PR de conteúdo — isso sobrescreveria o
progresso de quem clonou o repositório.

## Idioma e voz

O currículo é em **português do Brasil**. Termo técnico consagrado em inglês fica em inglês
(*gradient descent*, *embedding*, *attention*, *prompt*) — traduzir força o leitor a
retraduzir na hora de ler um paper. Explicação, comentário de código e nome de seção em
português.

Escreva direto, sem enfeite: o leitor está estudando, não sendo vendido. Prefira mostrar o
mecanismo a afirmar que ele é importante.

## Commits

Este repositório usa [Conventional Commits](https://www.conventionalcommits.org/pt-br/):

```
<tipo>(<escopo opcional>): <descrição no imperativo, minúscula, sem ponto final>
```

Tipos em uso: `feat`, `fix`, `docs`, `ci`, `chore`, `refactor`, `test`.

```
fix(licao-013): corrige o sinal do gradiente no exemplo 2
docs(readme): documenta o ciclo de correção de exercício
feat(tools): valida determinismo da saída das soluções
```

Um commit = uma unidade coerente. Não misture correção de conteúdo com mudança de tooling.

## Pull requests

1. Abra a partir de um branch seu (não de `main`).
2. Título do PR no mesmo formato de commit.
3. Preencha o [template de PR](pull_request_template.md) — inclusive a seção de
   verificação. **Não marque caixa de comando que você não rodou**; se um comando não se
   aplica, escreva qual e por quê.
4. O [CI](workflows/ci.yml) roda em Python 3.11 e 3.12. PR com CI vermelho não é revisado.
5. Revisão pode pedir mudança de conteúdo, de estrutura ou de escrita. Discordância técnica
   é bem-vinda — traga o argumento.

Como o projeto é pessoal, a decisão final sobre escopo e ordem do currículo é do autor. Se
uma proposta grande for recusada, o fork é livre (MIT) e sem ressentimento.

## Identidade visual

Se sua mudança toca logo, cores ou assets de marca, leia [`BRANDING.md`](../BRANDING.md)
primeiro — há decisões técnicas ali que parecem arbitrárias e não são (o wordmark ser
`<path>` em vez de `<text>`, o nó ciano ganhar anel no tema claro, existirem dois lockups em
vez de um).

## Código de conduta

Participar deste projeto implica concordar com o [Código de Conduta](CODE_OF_CONDUCT.md).

## Licença

Ao contribuir, você concorda que sua contribuição é distribuída sob a licença
[MIT](../LICENSE) do projeto.
