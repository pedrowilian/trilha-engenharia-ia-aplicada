#!/usr/bin/env python3
"""Gera, de forma REPRODUTÍVEL, as figuras das lições do módulo M11.

As figuras são artefatos de build (PNG) versionados no repositório para que a
pré-visualização local do Markdown (VS Code) as renderize offline, sem depender
de execução. Este script é a fonte da verdade dessas imagens: rodá-lo regenera
TODOS os PNGs do zero, de maneira determinística.

Princípios de reprodutibilidade:
  - Backend "Agg" (sem janela/interatividade);
  - Estilo e tamanhos fixos (sem depender de configuração do usuário);
  - Semente fixa de RNG onde há aleatoriedade.

Uso:
    python trilha/tools/figuras/gerar_figuras_m11.py

As imagens são salvas em:
    trilha/modulos/M11-arquitetura-sistemas-ia/assets/<NNN>-<slug>/<nome>.png
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
ASSETS = RAIZ_TRILHA / "modulos" / "M11-arquitetura-sistemas-ia" / "assets"

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


def _caixa(ax, x, y, w, h, texto, cor, fontsize=10):
    """Desenha uma caixa rotulada centrada em (x, y)."""
    ax.add_patch(plt.Rectangle((x - w / 2, y - h / 2), w, h,
                               facecolor=cor, alpha=0.18,
                               edgecolor=cor, lw=1.8, zorder=2))
    ax.text(x, y, texto, ha="center", va="center", fontsize=fontsize,
            color="#222", zorder=3)


def _seta(ax, x0, y0, x1, y1, cor="#444", rad=0.0):
    estilo = dict(arrowstyle="-|>", color=cor, lw=2.0)
    if rad:
        estilo["connectionstyle"] = f"arc3,rad={rad}"
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0), arrowprops=estilo, zorder=1)


# ===========================================================================
# Lição 081 — Design AI-First (árvore de decisão IA vs regras)
# ===========================================================================
SLUG_081 = "081-design-ai-first"


def fig_081_decisao_ai_first():
    """Árvore de decisão AI-First: a partir de um problema, as três perguntas
    de triagem (regras determinísticas cobrem? a entrada é variável/ambígua?
    o custo do erro é tolerável?) levam a 'usar regras', 'usar IA' ou
    'IA com humano no laço'."""
    fig, ax = plt.subplots(figsize=(9.4, 5.6))
    ax.set_axis_off()

    _caixa(ax, 0.5, 0.90, 0.30, 0.12, "Problema", CINZA, 10.5)

    _caixa(ax, 0.5, 0.66, 0.40, 0.13,
           "Regras determinísticas\ncobrem os casos?", COR_A, 10)
    _caixa(ax, 0.5, 0.40, 0.40, 0.13,
           "Entrada variável /\nsemântica / ambígua?", COR_D, 10)
    _caixa(ax, 0.5, 0.14, 0.40, 0.13,
           "Custo do erro é\ntolerável sem revisão?", COR_E, 10)

    _caixa(ax, 0.88, 0.66, 0.18, 0.12, "Usar\nregras", COR_C, 10)
    _caixa(ax, 0.12, 0.40, 0.18, 0.12, "Usar\nregras", COR_C, 10)
    _caixa(ax, 0.88, 0.14, 0.18, 0.12, "IA com\nhumano no laço", COR_B, 9.5)
    _caixa(ax, 0.12, 0.14, 0.18, 0.12, "Usar\nIA", COR_B, 10)

    _seta(ax, 0.5, 0.84, 0.5, 0.725)
    # regras cobrem? sim -> usar regras
    _seta(ax, 0.70, 0.66, 0.79, 0.66, cor=COR_C)
    ax.text(0.74, 0.69, "sim", fontsize=9, color=COR_C)
    _seta(ax, 0.5, 0.595, 0.5, 0.465, cor="#555")
    ax.text(0.515, 0.53, "não", fontsize=9, color="#555")
    # entrada variável? não -> usar regras
    _seta(ax, 0.30, 0.40, 0.21, 0.40, cor=COR_C)
    ax.text(0.24, 0.43, "não", fontsize=9, color=COR_C)
    _seta(ax, 0.5, 0.335, 0.5, 0.205, cor="#555")
    ax.text(0.515, 0.27, "sim", fontsize=9, color="#555")
    # custo tolerável? sim -> usar IA ; não -> humano no laço
    _seta(ax, 0.30, 0.14, 0.21, 0.14, cor=COR_B)
    ax.text(0.24, 0.17, "sim", fontsize=9, color=COR_B)
    _seta(ax, 0.70, 0.14, 0.79, 0.14, cor=COR_B)
    ax.text(0.73, 0.17, "não", fontsize=9, color=COR_B)

    ax.text(0.5, 0.985,
            "Triagem AI-First: a IA entra onde regras não bastam e a entrada é ambígua",
            ha="center", fontsize=10.5)
    ax.set_xlim(0, 1)
    ax.set_ylim(0.05, 1)
    return _salvar(fig, SLUG_081, "decisao-ai-first")


# ===========================================================================
# Lição 083 — Padrões de projeto de IA (router, cache, HITL/approval)
# ===========================================================================
SLUG_083 = "083-padroes-design-ia"


def fig_083_padroes():
    """Quatro padrões de projeto de IA dispostos em painéis: model router
    (despacha por características), semantic cache (responde sem chamar o
    modelo quando há acerto), human-in-the-loop e approval gate (pausa para
    revisão antes de efetivar ações de alto risco)."""
    fig, axes = plt.subplots(2, 2, figsize=(10.6, 7.2))
    for ax in axes.flat:
        ax.set_axis_off()
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

    # (a) Model router
    ax = axes[0, 0]
    _caixa(ax, 0.18, 0.5, 0.20, 0.18, "requisição", CINZA, 9.5)
    _caixa(ax, 0.5, 0.5, 0.18, 0.18, "router", COR_A, 9.5)
    _caixa(ax, 0.85, 0.80, 0.22, 0.16, "modelo\nleve", COR_C, 9)
    _caixa(ax, 0.85, 0.50, 0.22, 0.16, "modelo\nmédio", COR_E, 9)
    _caixa(ax, 0.85, 0.20, 0.22, 0.16, "modelo\nforte", COR_B, 9)
    _seta(ax, 0.28, 0.5, 0.41, 0.5)
    _seta(ax, 0.59, 0.55, 0.74, 0.78, cor="#777")
    _seta(ax, 0.59, 0.5, 0.74, 0.5, cor="#777")
    _seta(ax, 0.59, 0.45, 0.74, 0.22, cor="#777")
    ax.set_title("Model router — despacha por complexidade", fontsize=9.5)

    # (b) Semantic cache
    ax = axes[0, 1]
    _caixa(ax, 0.18, 0.5, 0.20, 0.18, "consulta", CINZA, 9.5)
    _caixa(ax, 0.5, 0.5, 0.20, 0.18, "cache\nsemântico", COR_D, 9)
    _caixa(ax, 0.85, 0.74, 0.22, 0.16, "resposta\n(hit)", COR_C, 9)
    _caixa(ax, 0.85, 0.26, 0.22, 0.16, "modelo\n(miss)", COR_B, 9)
    _seta(ax, 0.28, 0.5, 0.40, 0.5)
    _seta(ax, 0.60, 0.55, 0.74, 0.72, cor=COR_C)
    ax.text(0.60, 0.66, "sim ≥ τ", fontsize=8, color=COR_C)
    _seta(ax, 0.60, 0.45, 0.74, 0.28, cor=COR_B)
    ax.text(0.60, 0.33, "não", fontsize=8, color=COR_B)
    ax.set_title("Semantic cache — acerto evita o modelo", fontsize=9.5)

    # (c) Human-in-the-loop
    ax = axes[1, 0]
    _caixa(ax, 0.18, 0.5, 0.18, 0.18, "saída IA", COR_A, 9)
    _caixa(ax, 0.5, 0.5, 0.20, 0.18, "confiança\n≥ limiar?", COR_E, 9)
    _caixa(ax, 0.85, 0.74, 0.22, 0.16, "aceitar\nautomático", COR_C, 9)
    _caixa(ax, 0.85, 0.26, 0.22, 0.16, "revisão\nhumana", COR_B, 9)
    _seta(ax, 0.27, 0.5, 0.40, 0.5)
    _seta(ax, 0.60, 0.55, 0.74, 0.72, cor=COR_C)
    ax.text(0.60, 0.66, "sim", fontsize=8, color=COR_C)
    _seta(ax, 0.60, 0.45, 0.74, 0.28, cor=COR_B)
    ax.text(0.60, 0.33, "não", fontsize=8, color=COR_B)
    ax.set_title("Human-in-the-loop — baixa confiança vai p/ humano", fontsize=9.5)

    # (d) Approval gate
    ax = axes[1, 1]
    _caixa(ax, 0.18, 0.5, 0.18, 0.18, "ação\nproposta", COR_A, 9)
    _caixa(ax, 0.5, 0.5, 0.20, 0.18, "alto risco?", COR_E, 9)
    _caixa(ax, 0.85, 0.74, 0.22, 0.16, "executar", COR_C, 9)
    _caixa(ax, 0.85, 0.26, 0.22, 0.16, "aguardar\naprovação", COR_B, 9)
    _seta(ax, 0.27, 0.5, 0.40, 0.5)
    _seta(ax, 0.60, 0.55, 0.74, 0.72, cor=COR_C)
    ax.text(0.60, 0.66, "não", fontsize=8, color=COR_C)
    _seta(ax, 0.60, 0.45, 0.74, 0.28, cor=COR_B)
    ax.text(0.60, 0.33, "sim", fontsize=8, color=COR_B)
    ax.set_title("Approval gate — ações críticas pausam p/ aprovar", fontsize=9.5)

    fig.suptitle("Padrões de projeto de IA: router, cache semântico, HITL e approval gate",
                 fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    return _salvar(fig, SLUG_083, "padroes-design-ia")


# ===========================================================================
# Lição 084 — Arquitetura enterprise (pilha em camadas)
# ===========================================================================
SLUG_084 = "084-arquitetura-enterprise"


def fig_084_pilha_enterprise():
    """Pilha enterprise de um sistema de IA: a requisição desce pelo API
    gateway, a camada de orquestração, a camada de serviços (modelos em
    tiers) e a observabilidade transversal que instrumenta todas as camadas."""
    fig, ax = plt.subplots(figsize=(9.6, 6.2))
    ax.set_axis_off()

    camadas = [
        (0.80, "API gateway\n(autenticação · rate limit · roteamento)", COR_A),
        (0.60, "Orquestração\n(agentes · workflows · políticas de fallback)", COR_D),
        (0.40, "Serviços de modelo\n(tier leve · tier médio · tier forte)", COR_E),
        (0.20, "Dados & ferramentas\n(vector DB · cache · APIs externas)", COR_C),
    ]
    for y, texto, cor in camadas:
        _caixa(ax, 0.46, y, 0.66, 0.135, texto, cor, 10)

    # fluxo descendente da requisição
    for y0, y1 in [(0.732, 0.668), (0.532, 0.468), (0.332, 0.268)]:
        _seta(ax, 0.46, y0, 0.46, y1, cor="#555")
    _seta(ax, 0.46, 0.93, 0.46, 0.872, cor="#555")
    _caixa(ax, 0.46, 0.955, 0.30, 0.07, "requisição do cliente", CINZA, 9.5)

    # observabilidade transversal (barra lateral cobrindo todas as camadas)
    ax.add_patch(plt.Rectangle((0.84, 0.13), 0.13, 0.74,
                               facecolor=COR_B, alpha=0.14,
                               edgecolor=COR_B, lw=1.8, zorder=2))
    ax.text(0.905, 0.50, "Observabilidade\n(latência · custo · erros · traces)",
            ha="center", va="center", fontsize=9, rotation=90, color="#222", zorder=3)
    for y, _t, _c in camadas:
        _seta(ax, 0.79, y, 0.84, y, cor=COR_B, rad=0.0)

    ax.text(0.5, 0.995,
            "Arquitetura enterprise: gateway → orquestração → serviços → dados, com observabilidade transversal",
            ha="center", fontsize=10)
    ax.set_xlim(0, 1)
    ax.set_ylim(0.1, 1.02)
    return _salvar(fig, SLUG_084, "pilha-enterprise")


# ---------------------------------------------------------------------------
TODAS_AS_FIGURAS = [
    fig_081_decisao_ai_first,
    fig_083_padroes,
    fig_084_pilha_enterprise,
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
