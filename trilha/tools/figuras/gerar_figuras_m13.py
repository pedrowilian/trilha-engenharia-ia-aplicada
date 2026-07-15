#!/usr/bin/env python3
"""Gera, de forma REPRODUTÍVEL, as figuras das lições do módulo M13.

As figuras são artefatos de build (PNG) versionados no repositório para que a
pré-visualização local do Markdown (VS Code) as renderize offline, sem depender
de execução. Este script é a fonte da verdade dessas imagens: rodá-lo regenera
TODOS os PNGs do zero, de maneira determinística.

Princípios de reprodutibilidade:
  - Backend "Agg" (sem janela/interatividade);
  - Estilo e tamanhos fixos (sem depender de configuração do usuário);
  - Semente fixa de RNG onde há aleatoriedade.

Uso:
    python trilha/tools/figuras/gerar_figuras_m13.py

As imagens são salvas em:
    trilha/modulos/M13-seguranca-governanca/assets/<NNN>-<slug>/<nome>.png
e referenciadas nas lições por caminho RELATIVO (assets/<...>.png).
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # backend não interativo (determinístico, sem display)

import matplotlib.pyplot as plt
import numpy as np

# --- Estilo fixo, independente da config do usuário -------------------------
plt.rcParams.update({
    "figure.dpi": 110,
    "savefig.dpi": 110,
    "font.size": 11,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

# --- Localização dos assets (relativa a este arquivo) -----------------------
RAIZ_TRILHA = Path(__file__).resolve().parents[2]   # .../trilha
ASSETS = RAIZ_TRILHA / "modulos" / "M13-seguranca-governanca" / "assets"

COR_A = "#1f5fa8"
COR_B = "#c1432a"
COR_C = "#2e8b57"
COR_D = "#8e6abf"
COR_E = "#d9920a"
CINZA = "#9aa7b5"


def _salvar(fig, slug: str, nome: str) -> Path:
    """Salva a figura em assets/<slug>/<nome>.png e fecha a figura."""
    destino = ASSETS / slug / f"{nome}.png"
    destino.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(destino, bbox_inches="tight")
    plt.close(fig)
    return destino


# ===========================================================================
# Lição 090 — Interpretabilidade e explicabilidade (atribuição de features)
# ===========================================================================
SLUG_090 = "090-interpretabilidade-explicabilidade"


def fig_090_atribuicao_features():
    """Atribuição de features para uma única predição: a contribuição de cada
    feature é w_i * x_i, somando ao logito junto ao viés. Barras divergentes
    (verde empurra para cima, vermelho para baixo) tornam a explicação local
    legível de relance."""
    nomes = ["renda", "dívida", "atrasos", "tempo_conta", "consultas"]
    contribs = np.array([1.20, -0.85, -1.40, 0.60, -0.30])

    ordem = np.argsort(np.abs(contribs))      # menor -> maior importância
    nomes = [nomes[i] for i in ordem]
    contribs = contribs[ordem]
    cores = [COR_C if c >= 0 else COR_B for c in contribs]

    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    y = np.arange(len(nomes))
    ax.barh(y, contribs, color=cores, alpha=0.55, edgecolor=cores, lw=1.6)
    ax.set_yticks(y)
    ax.set_yticklabels(nomes)
    ax.axvline(0.0, color="#444", lw=1.0)
    for yi, c in zip(y, contribs):
        ax.text(c + (0.04 if c >= 0 else -0.04), yi, f"{c:+.2f}",
                va="center", ha="left" if c >= 0 else "right", fontsize=9)
    ax.set_xlabel("contribuição para o logito ($w_i\\,x_i$)")
    ax.set_xlim(-1.9, 1.9)
    ax.set_title("Atribuição de features de uma predição (explicação local)")
    fig.tight_layout()
    return _salvar(fig, SLUG_090, "atribuicao-features")


# ===========================================================================
# Lição 091 — Vieses e fairness (taxas de seleção por grupo)
# ===========================================================================
SLUG_091 = "091-vieses-fairness"


def fig_091_taxas_selecao():
    """Taxa de seleção (predição positiva) por grupo protegido. A diferença
    entre as barras é a paridade demográfica; a razão é o disparate impact. A
    linha tracejada marca a regra dos 80%."""
    grupos = ["Grupo A", "Grupo B"]
    taxas = np.array([0.60, 0.36])

    fig, ax = plt.subplots(figsize=(6.8, 4.2))
    x = np.arange(len(grupos))
    cores = [COR_A, COR_E]
    ax.bar(x, taxas, width=0.55, color=cores, alpha=0.55,
           edgecolor=cores, lw=1.6)
    for xi, t in zip(x, taxas):
        ax.text(xi, t + 0.015, f"{t:.0%}", ha="center", fontsize=10)
    # regra dos 80%: limiar = 0.8 * maior taxa
    limiar = 0.8 * taxas.max()
    ax.axhline(limiar, color=COR_B, ls="--", lw=1.6)
    ax.text(len(grupos) - 1, limiar + 0.012,
            f"80% do máximo = {limiar:.0%}", color=COR_B, ha="right", fontsize=9)
    ax.set_xticks(x)
    ax.set_xticklabels(grupos)
    ax.set_ylabel("taxa de seleção (predição positiva)")
    ax.set_ylim(0, 0.72)
    ax.set_title("Paridade demográfica: taxas de seleção por grupo")
    fig.tight_layout()
    return _salvar(fig, SLUG_091, "taxas-selecao")


# ===========================================================================
# Lição 092 — Riscos e segurança (detecção por categoria de ataque)
# ===========================================================================
SLUG_092 = "092-riscos-seguranca"


def fig_092_deteccao_ataques():
    """Resultado de um filtro de entrada determinístico sobre um lote sintético
    de prompts: quantas mensagens dispararam cada categoria de risco. Ilustra
    onde está o volume de ameaças que um guardrail precisa cobrir."""
    rng = np.random.default_rng(13)
    categorias = ["injeção de\nprompt", "jailbreak", "exfiltração\nde dados", "PII\nexposta"]
    # contagens determinísticas (semente fixa) de um lote de 200 mensagens
    contagens = rng.integers(low=[18, 10, 6, 14], high=[40, 26, 18, 33])

    fig, ax = plt.subplots(figsize=(7.8, 4.2))
    x = np.arange(len(categorias))
    cores = [COR_B, COR_D, COR_E, COR_A]
    ax.bar(x, contagens, width=0.6, color=cores, alpha=0.55,
           edgecolor=cores, lw=1.6)
    for xi, c in zip(x, contagens):
        ax.text(xi, c + 0.4, str(int(c)), ha="center", fontsize=10)
    ax.set_xticks(x)
    ax.set_xticklabels(categorias)
    ax.set_ylabel("mensagens sinalizadas (lote de 200)")
    ax.set_ylim(0, max(contagens) + 6)
    ax.set_title("Filtro de entrada: mensagens sinalizadas por categoria de risco")
    fig.tight_layout()
    return _salvar(fig, SLUG_092, "deteccao-ataques")


# ===========================================================================
# Lição 093 — Legal, regulatório e IA responsável (pirâmide de risco)
# ===========================================================================
SLUG_093 = "093-legal-regulatorio-ia-responsavel"


def fig_093_piramide_risco():
    """Pirâmide de risco no estilo do AI Act da UE: quanto maior o risco, mais
    rígida a obrigação regulatória e menor o conjunto de sistemas que se
    encaixam no topo."""
    niveis = [
        ("Inaceitável — proibido", 0.95, COR_B),
        ("Alto risco — conformidade rígida", 0.72, COR_E),
        ("Risco limitado — transparência", 0.49, COR_D),
        ("Risco mínimo — sem obrigação", 0.26, COR_C),
    ]
    fig, ax = plt.subplots(figsize=(7.8, 4.6))
    ax.set_axis_off()
    altura = 0.20
    y = 0.78
    for rotulo, largura, cor in niveis:
        x0 = 0.5 - largura / 2
        ax.add_patch(plt.Rectangle((x0, y), largura, altura,
                                   facecolor=cor, alpha=0.30,
                                   edgecolor=cor, lw=1.8))
        ax.text(0.5, y + altura / 2, rotulo, ha="center", va="center",
                fontsize=10, color="#222")
        y -= altura + 0.02
    ax.annotate("", xy=(0.045, 0.80), xytext=(0.045, 0.18),
                arrowprops=dict(arrowstyle="-|>", color="#444", lw=2.0))
    ax.text(0.02, 0.49, "risco / obrigação", rotation=90,
            va="center", ha="center", fontsize=9, color="#444")
    ax.set_xlim(0, 1)
    ax.set_ylim(0.12, 1.02)
    ax.set_title("Classificação por risco: obrigação cresce com o risco", fontsize=11)
    return _salvar(fig, SLUG_093, "piramide-risco")


# ===========================================================================
# Lição 094 — Custos e sustentabilidade (impacto acumulado de otimizações)
# ===========================================================================
SLUG_094 = "094-custos-sustentabilidade"


def fig_094_otimizacoes():
    """Custo mensal projetado conforme otimizações são acumuladas (baseline ->
    cache -> modelo menor -> batching). Cada barra mostra o efeito multiplicativo
    das alavancas de custo sobre a mesma carga."""
    etapas = ["baseline", "+ cache\n(40%)", "+ modelo\nmenor", "+ batching"]
    # fatores multiplicativos acumulados sobre o custo mensal
    base = 1200.0
    fatores = [1.0, 0.60, 0.60 * 0.55, 0.60 * 0.55 * 0.80]
    custos = [base * f for f in fatores]

    fig, ax = plt.subplots(figsize=(7.8, 4.2))
    x = np.arange(len(etapas))
    cores = [CINZA, COR_A, COR_D, COR_C]
    ax.bar(x, custos, width=0.6, color=cores, alpha=0.55,
           edgecolor=cores, lw=1.6)
    for xi, c in zip(x, custos):
        ax.text(xi, c + 12, f"${c:,.0f}", ha="center", fontsize=9.5)
    ax.set_xticks(x)
    ax.set_xticklabels(etapas)
    ax.set_ylabel("custo mensal projetado (US$)")
    ax.set_ylim(0, base * 1.12)
    ax.set_title("Alavancas de custo acumuladas sobre a mesma carga")
    fig.tight_layout()
    return _salvar(fig, SLUG_094, "otimizacoes-custo")


# ---------------------------------------------------------------------------
TODAS_AS_FIGURAS = [
    fig_090_atribuicao_features,
    fig_091_taxas_selecao,
    fig_092_deteccao_ataques,
    fig_093_piramide_risco,
    fig_094_otimizacoes,
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
