#!/usr/bin/env python3
"""Gera, de forma REPRODUTÍVEL, as figuras das lições do módulo M15 (Capstone).

As figuras são artefatos de build (PNG) versionados no repositório para que a
pré-visualização local do Markdown (VS Code) as renderize offline, sem depender
de execução. Este script é a fonte da verdade dessas imagens: rodá-lo regenera
TODOS os PNGs do zero, de maneira determinística.

Princípios de reprodutibilidade:
  - Backend "Agg" (sem janela/interatividade);
  - Estilo e tamanhos fixos (sem depender de configuração do usuário);
  - Sem aleatoriedade (os diagramas são posicionais e fixos).

Uso:
    python trilha/tools/figuras/gerar_figuras_m15.py

As imagens são salvas em:
    trilha/modulos/M15-capstone/assets/<NNN>-<slug>/<nome>.png
e referenciadas nas lições por caminho RELATIVO (assets/<...>.png).
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # backend não interativo (determinístico, sem display)

import matplotlib.pyplot as plt

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
ASSETS = RAIZ_TRILHA / "modulos" / "M15-capstone" / "assets"

COR_A = "#1f5fa8"   # MCP
COR_B = "#c1432a"   # entrada/saída
COR_C = "#2e8b57"   # RAG
COR_D = "#8e6abf"   # agente
COR_E = "#d9920a"   # evidência
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
# Lição 099 — Capstone: planejamento e arquitetura do Micro-SaaS
# ===========================================================================
SLUG_099 = "099-capstone-planejamento-arquitetura"


def fig_099_arquitetura():
    """Arquitetura da solução do Micro-SaaS: a pergunta entra pelo cliente MCP,
    que descobre e invoca a capacidade no servidor MCP; o servidor delega ao
    agente, que usa a ferramenta de busca para consultar o RAG; a resposta
    retorna acompanhada da evidência de cada componente."""
    fig, ax = plt.subplots(figsize=(10.0, 5.2))
    ax.set_axis_off()

    _caixa(ax, 0.08, 0.55, 0.13, 0.18, "Pergunta", COR_B, 10)
    _caixa(ax, 0.28, 0.55, 0.16, 0.20, "Cliente MCP", COR_A, 10)
    _caixa(ax, 0.50, 0.55, 0.16, 0.20, "Servidor MCP\n(ferramentas)", COR_A, 9.5)
    _caixa(ax, 0.72, 0.55, 0.15, 0.20, "Agente\n(ReAct)", COR_D, 10)
    _caixa(ax, 0.92, 0.55, 0.13, 0.20, "RAG\n(em memória)", COR_C, 9.5)
    _caixa(ax, 0.50, 0.16, 0.40, 0.14, "Evidência por componente (RAG · agente · MCP)", COR_E, 9.5)

    _seta(ax, 0.145, 0.55, 0.20, 0.55)
    _seta(ax, 0.36, 0.55, 0.42, 0.55)
    ax.text(0.39, 0.62, "tools/list\ntools/call", fontsize=7.5, color="#555", ha="center")
    _seta(ax, 0.58, 0.55, 0.645, 0.55)
    _seta(ax, 0.795, 0.55, 0.855, 0.55)
    ax.text(0.825, 0.62, "buscar", fontsize=7.5, color="#555", ha="center")
    # retorno da resposta
    _seta(ax, 0.92, 0.44, 0.28, 0.44, cor=CINZA, rad=0.12)
    ax.text(0.5, 0.34, "resposta", fontsize=8.5, color="#666", ha="center")
    # coleta de evidência
    _seta(ax, 0.50, 0.45, 0.50, 0.24, cor=COR_E)

    ax.text(0.5, 0.96,
            "Arquitetura do Micro-SaaS: cliente/servidor MCP → agente → RAG, com evidência observável",
            ha="center", fontsize=10.5)
    ax.set_xlim(0, 1)
    ax.set_ylim(0.05, 1)
    return _salvar(fig, SLUG_099, "arquitetura-solucao")


# ===========================================================================
# Lição 100 — Capstone: implementação, fluxo ponta a ponta e critérios
# ===========================================================================
SLUG_100 = "100-capstone-implementacao-fluxo"


def fig_100_fluxo_evidencia():
    """Fluxo ponta a ponta com os pontos de evidência: cada componente
    incrementa um contador observável (consultas do RAG, passos do agente,
    chamadas do MCP), e o critério de conclusão exige que os três sejam > 0."""
    fig, ax = plt.subplots(figsize=(9.8, 4.6))
    ax.set_axis_off()

    _caixa(ax, 0.15, 0.62, 0.20, 0.22, "MCP\nchamadas≥2", COR_A, 10)
    _caixa(ax, 0.45, 0.62, 0.20, 0.22, "Agente\npassos≥1", COR_D, 10)
    _caixa(ax, 0.75, 0.62, 0.20, 0.22, "RAG\nconsultas≥1", COR_C, 10)
    _caixa(ax, 0.45, 0.20, 0.46, 0.16, "completo() = (RAG>0) ∧ (agente>0) ∧ (MCP>0)", COR_E, 9.5)

    _seta(ax, 0.25, 0.62, 0.35, 0.62)
    _seta(ax, 0.55, 0.62, 0.65, 0.62)
    _seta(ax, 0.15, 0.51, 0.30, 0.28, cor=CINZA)
    _seta(ax, 0.45, 0.51, 0.45, 0.28, cor=CINZA)
    _seta(ax, 0.75, 0.51, 0.60, 0.28, cor=CINZA)

    ax.text(0.5, 0.93,
            "Critério de conclusão ponta a ponta: evidência de cada componente deve ser > 0",
            ha="center", fontsize=10.5)
    ax.set_xlim(0, 1)
    ax.set_ylim(0.1, 1)
    return _salvar(fig, SLUG_100, "fluxo-evidencia")


# ---------------------------------------------------------------------------
TODAS_AS_FIGURAS = [
    fig_099_arquitetura,
    fig_100_fluxo_evidencia,
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
