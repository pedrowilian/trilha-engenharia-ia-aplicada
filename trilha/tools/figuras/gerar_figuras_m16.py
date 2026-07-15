#!/usr/bin/env python3
"""Gera, de forma REPRODUTIVEL, as figuras das licoes do modulo M16.

Modulo M16 - Carreira e Entrevistas para AI Engineer (licoes 101-104).

As figuras sao artefatos de build (PNG) versionados no repositorio para que a
pre-visualizacao local do Markdown (VS Code) as renderize offline, sem depender
de execucao. Este script e a fonte da verdade dessas imagens: roda-lo regenera
TODOS os PNGs do zero, de maneira deterministica.

Principios de reprodutibilidade:
  - Backend "Agg" (sem janela/interatividade);
  - Estilo e tamanhos fixos (sem depender de configuracao do usuario);
  - Semente fixa de RNG onde ha aleatoriedade.

Uso:
    python3 trilha/tools/figuras/gerar_figuras_m16.py

As imagens sao salvas em:
    trilha/modulos/M16-carreira-entrevistas/assets/<NNN>-<slug>/<nome>.png
e referenciadas nas licoes por caminho RELATIVO (assets/<...>.png).
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # backend nao interativo (deterministico, sem display)

import matplotlib.pyplot as plt
import numpy as np

# --- Estilo fixo, independente da config do usuario -------------------------
plt.rcParams.update({
    "figure.dpi": 110,
    "savefig.dpi": 110,
    "font.size": 11,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

# --- Localizacao dos assets (relativa a este arquivo) -----------------------
RAIZ_TRILHA = Path(__file__).resolve().parents[2]   # .../trilha
ASSETS = RAIZ_TRILHA / "modulos" / "M16-carreira-entrevistas" / "assets"

COR_A = "#1f5fa8"
COR_B = "#c1432a"
COR_C = "#2e8b57"
COR_D = "#8e6abf"
COR_E = "#d39a00"
CINZA = "#9aa7b5"


def _salvar(fig, slug: str, nome: str) -> Path:
    """Salva a figura em assets/<slug>/<nome>.png e fecha a figura."""
    destino = ASSETS / slug / f"{nome}.png"
    destino.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(destino, bbox_inches="tight")
    plt.close(fig)
    return destino


# ===========================================================================
# Licao 101 - O mercado e o papel do AI Engineer; portfolio
# ===========================================================================
SLUG_101 = "101-mercado-papel-portfolio"


def fig_101_niveis_dimensoes():
    """Como autonomia, escopo e impacto crescem por nivel de senioridade."""
    niveis = ["Junior", "Pleno", "Senior", "Staff", "Principal"]
    autonomia = [1, 2, 3, 4, 5]
    escopo = [1, 2, 4, 5, 5]
    impacto = [1, 2, 3, 5, 5]
    x = np.arange(len(niveis))
    largura = 0.26

    fig, ax = plt.subplots(figsize=(8.8, 4.4))
    ax.bar(x - largura, autonomia, largura, label="Autonomia", color=COR_A,
           edgecolor="white")
    ax.bar(x, escopo, largura, label="Escopo", color=COR_C, edgecolor="white")
    ax.bar(x + largura, impacto, largura, label="Impacto", color=COR_E,
           edgecolor="white")
    ax.set_xticks(x)
    ax.set_xticklabels(niveis)
    ax.set_ylim(0, 5.6)
    ax.set_ylabel("nivel da dimensao (1-5)")
    ax.legend()
    ax.set_title("Senioridade cresce em autonomia, escopo e impacto, nao em sintaxe")
    return _salvar(fig, SLUG_101, "niveis-dimensoes")


def fig_101_portfolio_sinais():
    """Sinais de qualidade que um recrutador le num repositorio de portfolio."""
    sinais = ["README", "Testes", "CI", "Docs", "Demo"]
    repo_forte = [5, 4, 4, 4, 5]
    repo_fraco = [2, 0, 0, 1, 1]
    x = np.arange(len(sinais))
    largura = 0.38

    fig, ax = plt.subplots(figsize=(8.4, 4.4))
    ax.bar(x - largura / 2, repo_forte, largura, label="Repo com sinais fortes",
           color=COR_C, edgecolor="white")
    ax.bar(x + largura / 2, repo_fraco, largura, label="Repo com sinais fracos",
           color=COR_B, edgecolor="white")
    ax.set_xticks(x)
    ax.set_xticklabels(sinais)
    ax.set_ylim(0, 5.6)
    ax.set_ylabel("forca do sinal (0-5)")
    ax.legend()
    ax.set_title("Portfolio: o recrutador le sinais, nao conta linhas de codigo")
    return _salvar(fig, SLUG_101, "portfolio-sinais")


# ===========================================================================
# Licao 102 - Entrevistas: Fundamentos de ML
# ===========================================================================
SLUG_102 = "102-entrevistas-fundamentos-ml"


def fig_102_vies_variancia():
    """Curva em U do erro total: vies^2 cai, variancia sobe com a complexidade."""
    complexidade = np.arange(1, 16)
    vies2 = 9.0 / complexidade          # cai com a capacidade do modelo
    variancia = 0.06 * complexidade     # sobe com a capacidade
    ruido = 1.0                         # erro irredutivel
    total = vies2 + variancia + ruido
    k_otimo = complexidade[int(np.argmin(total))]

    fig, ax = plt.subplots(figsize=(8.4, 4.6))
    ax.plot(complexidade, vies2, "o-", color=COR_A, lw=2.0, label="vies$^2$")
    ax.plot(complexidade, variancia, "s-", color=COR_E, lw=2.0, label="variancia")
    ax.plot(complexidade, total, "^-", color=COR_B, lw=2.4, label="erro total")
    ax.axhline(ruido, color=CINZA, ls=":", lw=1.5, label="ruido (irredutivel)")
    ax.axvline(k_otimo, color=COR_C, ls="--", lw=1.8)
    ax.text(k_otimo + 0.2, total.max() * 0.85,
            f"complexidade otima = {k_otimo}", color=COR_C, fontsize=9)
    ax.set_xlabel("complexidade do modelo")
    ax.set_ylabel("erro esperado")
    ax.set_title("Trade-off vies-variancia: o erro total e uma curva em U")
    ax.legend()
    return _salvar(fig, SLUG_102, "vies-variancia")


def fig_102_reliability():
    """Diagrama de confiabilidade: confianca prevista x acuracia observada."""
    centros = np.array([0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95])
    # modelo super-confiante: acuracia abaixo da diagonal nos bins altos
    acuracia = np.array([0.06, 0.12, 0.20, 0.28, 0.36, 0.45, 0.52, 0.60, 0.68, 0.78])

    fig, ax = plt.subplots(figsize=(7.6, 5.0))
    ax.plot([0, 1], [0, 1], "--", color=CINZA, lw=1.8,
            label="calibracao perfeita")
    ax.bar(centros, acuracia, width=0.09, color=COR_A, alpha=0.8,
           edgecolor="white", label="acuracia observada")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel("confianca prevista")
    ax.set_ylabel("acuracia observada (fracao de acertos)")
    ax.set_title("Diagrama de confiabilidade: barras abaixo da diagonal = excesso de confianca")
    ax.legend(loc="upper left")
    return _salvar(fig, SLUG_102, "reliability")


# ===========================================================================
# Licao 103 - Entrevistas: Engenharia de sistemas de IA
# ===========================================================================
SLUG_103 = "103-entrevistas-sistemas-ia"


def fig_103_recall_at_k():
    """Recall@k cresce com k: mais candidatos recuperados, mais relevantes achados."""
    k = np.arange(1, 11)
    # dois recuperadores: denso (forte no topo) x lexical (cresce mais devagar)
    denso = np.array([0.40, 0.60, 0.72, 0.80, 0.86, 0.90, 0.93, 0.95, 0.97, 0.98])
    lexical = np.array([0.25, 0.40, 0.52, 0.61, 0.68, 0.74, 0.79, 0.83, 0.86, 0.88])

    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    ax.plot(k, denso, "o-", color=COR_A, lw=2.2, label="recuperador denso")
    ax.plot(k, lexical, "s-", color=COR_E, lw=2.2, label="recuperador lexical (BM25)")
    ax.set_xticks(k)
    ax.set_ylim(0, 1.02)
    ax.set_xlabel("k (numero de documentos recuperados)")
    ax.set_ylabel("recall@k")
    ax.set_title("Recall@k: quanto da resposta o retriever traz para o contexto")
    ax.legend(loc="lower right")
    return _salvar(fig, SLUG_103, "recall-at-k")


def fig_103_custo_latencia():
    """Fronteira custo x latencia para opcoes de arquitetura de inferencia."""
    nomes = ["Modelo grande\n(sem cache)", "Modelo grande\n+ cache",
             "Modelo pequeno\n+ RAG", "Cascata\n(pequeno->grande)"]
    custo = np.array([10.0, 6.5, 3.0, 4.5])      # $/1k requisicoes
    latencia = np.array([1800, 1100, 700, 950])  # ms (p95)
    cores = [COR_B, COR_D, COR_C, COR_A]

    fig, ax = plt.subplots(figsize=(8.4, 4.8))
    ax.scatter(latencia, custo, s=160, c=cores, edgecolor="black", zorder=3)
    for nome, x, y in zip(nomes, latencia, custo):
        ax.annotate(nome, (x, y), textcoords="offset points",
                    xytext=(8, 6), fontsize=9)
    ax.set_xlabel("latencia p95 (ms)")
    ax.set_ylabel("custo por 1k requisicoes ($)")
    ax.set_title("Trade-off custo x latencia: nao existe almoco gratis em system design")
    return _salvar(fig, SLUG_103, "custo-latencia")


# ===========================================================================
# Licao 104 - Exercicios de entrevista resolvidos em Python
# ===========================================================================
SLUG_104 = "104-exercicios-entrevista-python"


def fig_104_complexidade():
    """Crescimento de O(n), O(n log n) e O(n^2): por que a escolha importa."""
    n = np.arange(1, 51)
    linear = n.astype(float)
    nlogn = n * np.log2(n + 1)
    quadratico = n.astype(float) ** 2

    fig, ax = plt.subplots(figsize=(8.4, 4.6))
    ax.plot(n, linear, color=COR_C, lw=2.2, label="O(n)")
    ax.plot(n, nlogn, color=COR_A, lw=2.2, label="O(n log n)")
    ax.plot(n, quadratico, color=COR_B, lw=2.2, label="O(n$^2$)")
    ax.set_ylim(0, 1600)
    ax.set_xlabel("tamanho da entrada n")
    ax.set_ylabel("operacoes (aprox.)")
    ax.set_title("Complexidade: a diferenca entre passar e estourar o tempo limite")
    ax.legend(loc="upper left")
    return _salvar(fig, SLUG_104, "complexidade")


# ---------------------------------------------------------------------------
TODAS_AS_FIGURAS = [
    fig_101_niveis_dimensoes,
    fig_101_portfolio_sinais,
    fig_102_vies_variancia,
    fig_102_reliability,
    fig_103_recall_at_k,
    fig_103_custo_latencia,
    fig_104_complexidade,
]


def main() -> int:
    gerados = []
    for gerar in TODAS_AS_FIGURAS:
        caminho = gerar()
        rel = caminho.relative_to(RAIZ_TRILHA)
        gerados.append(rel)
        print(f"[ok] {rel}")
    print(f"\n{len(gerados)} figura(s) gerada(s) em {ASSETS.relative_to(RAIZ_TRILHA)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
