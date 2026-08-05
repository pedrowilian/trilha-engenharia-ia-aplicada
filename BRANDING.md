# Guia de marca — TEIA

Identidade visual da **Trilha de Engenharia de IA Aplicada**. Este documento existe para
que a marca seja reproduzível: quem for gerar um slide, um card ou uma variação do logo
daqui a seis meses encontra aqui a geometria exata, os hex e as regras de uso — sem ter
que adivinhar a partir dos SVGs.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/brand/teia-lockup-dark.svg">
    <img alt="Lockup TEIA" src="assets/brand/teia-lockup-light.svg" width="360">
  </picture>
</p>

## 1. Nome

| | |
|---|---|
| **Nome completo** | Trilha de Engenharia de IA Aplicada |
| **Marca curta** | **TEIA** — sigla do nome completo |
| **Uso** | O repositório, o título do README e as citações formais usam o **nome completo**. `TEIA` é a forma curta, reservada a logo, favicon, wordmark e referências abreviadas. |

`TEIA` nunca substitui o nome completo na primeira menção de um texto. A sigla só carrega
significado depois que o leitor viu o nome por extenso.

## 2. Símbolo

O símbolo é um **DAG mínimo de 5 nós**, e não um ornamento: a trilha declara
pré-requisitos entre lições e o validador (`trilha/tools/validar_trilha.py`) checa esse
grafo com `networkx`. O desenho é literalmente o que o projeto é.

```
                    ● E          E em ciano (destaque):
              ╱  ╱                 o fim da trilha (M16)
        ● C ╱  ╱
       ╱      ● D               ← célula fechada B→C→E / B→D→E
   ● B ─────╱                     = a "teia"
  ╱
● A                             ← cauda A→B = a "trilha"
```

Duas metáforas num só desenho: a **cauda** `A→B` é o percurso linear (estudo sequencial);
a **célula fechada** `B→C→E` / `B→D→E` é a teia (conhecimento que se reconecta).

### Construção geométrica

`viewBox="0 0 32 32"`. Coordenadas dos centros dos nós:

| Nó | x | y | Papel |
|---|---|---|---|
| A | 5 | 28 | início da trilha |
| B | 11 | 22 | bifurcação |
| C | 16 | 10 | ramo superior |
| D | 21 | 20 | ramo inferior |
| E | 27 | 6 | nó terminal (**sempre ciano**) |

Arestas: `A→B`, `B→C`, `B→D`, `C→E`, `D→E`.

Parâmetros de traço:

- nós: círculos preenchidos, `r="3"`
- arestas: `stroke-width="2.5"`, `stroke-linecap="round"`, sem preenchimento

**Regras invioláveis da geometria:**

1. **Toda aresta sobe para a direita** — `x` cresce e `y` decresce. Progressão é a
   semântica do símbolo; uma aresta descendente o contradiz.
2. **Nenhuma aresta cruza outra.** O grafo é planar nessas coordenadas; qualquer
   reposicionamento precisa preservar isso.
3. **O nó E é o único ciano.** É o destaque, e destaque duplicado deixa de ser destaque.
4. **A célula fechada tem que ler como célula.** Nessas coordenadas o quadrilátero
   `B–C–E–D` tem área 120 un² e a folga mínima entre bordas de nós é 2,5 un. Aproximar os
   nós faz o símbolo virar um borrão em vez de um grafo — foi exatamente o erro da primeira
   versão (área 73,5 un², folga 1,07 un). Se mexer nas coordenadas, meça as duas coisas.

**Tamanho mínimo do símbolo completo: 32 px.** Verificado por rasterização — a 24 px os
cinco nós já se embolam e a cauda `A→B` vira um ponto solto. Abaixo de 32 px use o
`teia-favicon.svg`, que existe exatamente para isso e se sustenta a 16 px.

## 3. Paleta

| Uso | Hex | Onde |
|---|---|---|
| Base grafite | `#0D1117` | fundo escuro (é o mesmo fundo do GitHub em tema dark — o logo "flutua"), texto no tema claro |
| Ciano destaque | `#22D3EE` | nó terminal, acentos, régua do card social |
| Ciano claro | `#7DD3FC` | arestas no tema escuro |
| Texto claro | `#E6EDF3` | wordmark e nós no tema escuro |
| Neutro | `#6E7681` | texto secundário, arestas no tema claro |

### Regra de contraste — leia antes de usar o ciano

`#22D3EE` sobre `#0D1117` dá ~**10:1** (folgadamente AAA). Sobre branco dá ~**1.8:1**,
abaixo de AA.

Daí a regra: **ciano é cor de forma, nunca cor de texto sobre fundo claro.** Pode ser
preenchimento de nó, traço, régua, ícone. Não pode ser corpo de texto nem link em fundo
branco — nesse caso o texto vai para grafite `#0D1117` (~19:1 sobre branco).

E é exatamente por isso que existem **duas variantes de lockup** em vez de um SVG único:

- no tema claro as arestas viram neutro `#6E7681`, os nós e o wordmark viram grafite;
- o nó terminal ciano ganha um **anel grafite** (`stroke="#0D1117" stroke-width="1.5"`),
  senão ele desaparece no branco.

## 4. Wordmark

`T E I A` geométrico, com *tracking* largo. As quatro letras são compostas só de
segmentos retos, o que permite desenhá-las como geometria pura.

**Decisão técnica que não deve ser revertida: o wordmark é `<path>`, nunca `<text>`.**
`<text>` em SVG é renderizado com as fontes de quem está olhando — no GitHub, num leitor
RSS ou num proxy de imagem, o lockup quebra (letra errada, largura errada, ou nada). Com
`<path>` o resultado é pixel-idêntico em qualquer lugar, sem embutir fonte.

Métrica no `viewBox="0 0 188 56"` do lockup:

| | |
|---|---|
| Altura de caixa alta | 24 (de `y=16` a `y=40`) |
| Traço | `stroke-width="3.5"`, caps e joins arredondados |
| Origem x das letras | `T` 72 · `E` 106 · `I` 137 · `A` 151 |
| Símbolo no lockup | `translate(4 2) scale(1.5)` sobre o `viewBox` 32×32 |

A única exceção à regra do `<path>` é o **card social** (`teia-social-preview.svg`), cujas
linhas de tagline usam `<text>`. Ali é seguro porque o arquivo é rasterizado em PNG numa
máquina com fontes antes de ir para o GitHub — a dependência de fonte se resolve no ato de
gerar a imagem, não no dispositivo de quem vê.

## 5. Assets

Todos em [`assets/brand/`](assets/brand/):

| Arquivo | O que é |
|---|---|
| `teia-lockup-light.svg` | símbolo + wordmark, para fundo claro |
| `teia-lockup-dark.svg` | símbolo + wordmark, para fundo escuro |
| `teia-icon.svg` | só o símbolo, 32×32 |
| `teia-favicon.svg` | símbolo simplificado (sem a cauda `A→B`, célula ampliada 1,42×) para 16–32 px |
| `teia-social-preview.svg` | card 1280×640, **arquivo-fonte** do social preview |

### Troca automática claro/escuro

Use `<picture>` com `prefers-color-scheme`. Esse é o mecanismo que o GitHub documenta e
respeita:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/brand/teia-lockup-dark.svg">
  <img alt="TEIA — Trilha de Engenharia de IA Aplicada" src="assets/brand/teia-lockup-light.svg" width="420">
</picture>
```

Não tente resolver isso com `@media` dentro de um SVG único: o proxy de imagens do GitHub
(Camo) serve o SVG de forma que o CSS interno não recebe o contexto de tema da página.

### Social preview — passo manual

O GitHub aceita apenas **PNG, JPG ou GIF** em *Settings → General → Social preview*, e o
upload é manual. Rasterize o SVG-fonte antes:

```bash
# qualquer um destes serve
rsvg-convert -w 1280 -h 640 assets/brand/teia-social-preview.svg -o teia-social-preview.png
inkscape assets/brand/teia-social-preview.svg -w 1280 -h 640 -o teia-social-preview.png
python3 -c "import cairosvg; cairosvg.svg2png(url='assets/brand/teia-social-preview.svg', write_to='teia-social-preview.png', output_width=1280, output_height=640)"
```

O PNG gerado é artefato descartável e **não** é versionado — o SVG é a fonte da verdade.

A pilha de fontes das taglines é `Inter, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif`.
Se nenhuma estiver instalada na máquina que rasteriza, o rasterizador cai na sans-serif
padrão do sistema (DejaVu Sans no Linux) — legível, mas com métrica diferente. Se o
resultado importa, instale a Inter antes de gerar o PNG.

### Área de respiro

Reserve, ao redor do lockup, uma margem livre igual à **altura de caixa alta do wordmark**
(24 unidades do `viewBox`, ou seja ~43% da altura total do lockup). Nada — texto, borda,
badge — entra nessa faixa.

Tamanho mínimo do lockup: **120 px** de largura. Abaixo disso o wordmark perde legibilidade;
use o `teia-icon.svg` sozinho.

## 6. O que não fazer

- Não escreva o wordmark com `<text>` ou com fonte do sistema — quebra fora da sua máquina.
- Não use ciano como cor de texto em fundo claro (falha AA).
- Não pinte mais de um nó em ciano, nem mude qual nó é o terminal.
- Não inverta, espelhe ou rotacione o símbolo: as arestas deixariam de subir para a direita.
- Não redesenhe as arestas de modo que se cruzem.
- Não aplique sombra, gradiente, contorno externo ou efeito de brilho.
- Não estique o lockup de forma não proporcional.
- Não recolora o lockup fora da paleta acima.
- Não coloque o lockup sobre foto ou fundo de baixo contraste — use a variante certa em
  cor plana.
- Não use a identidade visual de nenhum empregador aqui. Este é um projeto **pessoal** e
  open source; a marca é própria da trilha.

## 7. Licença dos assets

Os assets de marca estão no repositório sob a mesma licença [MIT](LICENSE) do restante do
projeto. Isso permite reuso e fork; não implica endosso do projeto original a trabalhos
derivados, nem autoriza apresentar um fork como sendo a trilha oficial.
