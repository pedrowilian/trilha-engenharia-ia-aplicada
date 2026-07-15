#!/usr/bin/env python3
"""Gera, de forma REPRODUTÍVEL, as figuras das lições do módulo M08.

As figuras são artefatos de build (PNG) versionados no repositório para que a
pré-visualização local do Markdown (VS Code) as renderize offline, sem depender
de execução. Este script é a fonte da verdade dessas imagens: rodá-lo regenera
TODOS os PNGs do zero, de maneira determinística.

Princípios de reprodutibilidade:
  - Backend "Agg" (sem janela/interatividade);
  - Estilo e tamanhos fixos (sem depender de configuração do usuário);
  - Semente fixa de RNG onde há aleatoriedade.

Uso:
    python trilha/tools/figuras/gerar_figuras_m08.py

As imagens são salvas em:
    trilha/modulos/M08-agentes-autonomos/assets/<NNN>-<slug>/<nome>.png
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
ASSETS = RAIZ_TRILHA / "modulos" / "M08-agentes-autonomos" / "assets"

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
# Lição 062 — Arquitetura de agentes (loop perceção→raciocínio→ação→feedback)
# ===========================================================================
SLUG_062 = "062-arquitetura-de-agentes"


def fig_062_agent_loop():
    """O laço de controle de um agente: percepção -> raciocínio -> ação ->
    feedback, com a memória/contexto no centro alimentando cada etapa."""
    fig, ax = plt.subplots(figsize=(7.6, 6.0))
    ax.set_axis_off()

    centro = (0.5, 0.5)
    raio = 0.30
    etapas = [
        ("Percepção\n(observação)", COR_A),
        ("Raciocínio\n(planner)", COR_D),
        ("Ação\n(toolbox)", COR_C),
        ("Feedback\n(resultado)", COR_E),
    ]
    # posições nos quatro pontos cardeais (topo, direita, baixo, esquerda)
    angulos = [90, 0, 270, 180]
    pos = []
    for ang in angulos:
        rad = np.deg2rad(ang)
        pos.append((centro[0] + raio * np.cos(rad),
                    centro[1] + raio * np.sin(rad)))

    for (x, y), (texto, cor) in zip(pos, etapas):
        _caixa(ax, x, y, 0.26, 0.16, texto, cor, 10)

    # setas em ciclo (topo -> direita -> baixo -> esquerda -> topo)
    for i in range(4):
        x0, y0 = pos[i]
        x1, y1 = pos[(i + 1) % 4]
        _seta(ax, x0, y0, x1, y1, cor="#555", rad=0.25)

    # memória/contexto no centro
    _caixa(ax, centro[0], centro[1], 0.22, 0.14,
           "Memória /\ncontexto", CINZA, 10)

    ax.text(0.5, 0.96,
            "Laço do agente: percepção → raciocínio → ação → feedback",
            ha="center", fontsize=11)
    ax.set_xlim(0, 1)
    ax.set_ylim(0.08, 1)
    return _salvar(fig, SLUG_062, "agent-loop")


# ===========================================================================
# Lição 069 — Orquestração com LangGraph (grafo de execução)
# ===========================================================================
SLUG_069 = "069-orquestracao-langgraph"


def fig_069_grafo_execucao():
    """Grafo de execução didático no estilo LangGraph: nós são funções que
    transformam um estado compartilhado; arestas condicionais decidem se o
    fluxo volta ao 'agente' (mais uma ferramenta) ou termina."""
    fig, ax = plt.subplots(figsize=(9.2, 4.6))
    ax.set_axis_off()

    _caixa(ax, 0.10, 0.50, 0.14, 0.18, "START", CINZA, 10)
    _caixa(ax, 0.36, 0.50, 0.18, 0.22, "agente\n(raciocina)", COR_D, 10)
    _caixa(ax, 0.64, 0.72, 0.18, 0.22, "ferramenta\n(executa)", COR_C, 10)
    _caixa(ax, 0.64, 0.28, 0.16, 0.18, "END", COR_B, 10)

    _seta(ax, 0.17, 0.50, 0.27, 0.50)
    # aresta condicional: agente -> ferramenta (continua)
    _seta(ax, 0.45, 0.56, 0.55, 0.68, cor="#2e8b57")
    ax.text(0.49, 0.66, "tool_call?\nsim", fontsize=8, color="#2e8b57")
    # aresta condicional: agente -> END (terminou)
    _seta(ax, 0.45, 0.44, 0.56, 0.32, cor="#c1432a")
    ax.text(0.49, 0.34, "não", fontsize=8, color="#c1432a")
    # ferramenta volta para o agente (laço)
    _seta(ax, 0.64, 0.61, 0.42, 0.61, cor="#555", rad=0.3)
    ax.text(0.50, 0.80, "observação alimenta o estado", fontsize=8, color="#555")

    ax.text(0.5, 0.97,
            "Grafo de execução: nós transformam um estado; arestas condicionais decidem o próximo nó",
            ha="center", fontsize=10.5)
    ax.set_xlim(0, 1)
    ax.set_ylim(0.1, 1)
    return _salvar(fig, SLUG_069, "grafo-execucao")


# ===========================================================================
# Lição 071 — Sistemas multi-agente (topologias)
# ===========================================================================
SLUG_071 = "071-multi-agente"


def fig_071_topologias():
    """Três topologias multi-agente: supervisor (estrela), hierárquica
    (árvore) e group-chat (totalmente conectada)."""
    fig, axes = plt.subplots(1, 3, figsize=(11.0, 4.2))
    for ax in axes:
        ax.set_axis_off()
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

    def no(ax, x, y, txt, cor):
        ax.add_patch(plt.Circle((x, y), 0.085, facecolor=cor, alpha=0.2,
                                 edgecolor=cor, lw=1.8, zorder=2))
        ax.text(x, y, txt, ha="center", va="center", fontsize=8.5, zorder=3)

    def aresta(ax, p, q, cor="#666"):
        ax.plot([p[0], q[0]], [p[1], q[1]], color=cor, lw=1.6, zorder=1)

    # (a) supervisor — estrela
    sup = (0.5, 0.8)
    trab = [(0.2, 0.3), (0.5, 0.25), (0.8, 0.3)]
    for t in trab:
        aresta(axes[0], sup, t)
    no(axes[0], *sup, "Sup", COR_B)
    for i, t in enumerate(trab, 1):
        no(axes[0], *t, f"A{i}", COR_A)
    axes[0].set_title("Supervisor (estrela)", fontsize=10)

    # (b) hierárquica — árvore
    raiz = (0.5, 0.85)
    lider = [(0.27, 0.5), (0.73, 0.5)]
    folhas = [(0.13, 0.18), (0.4, 0.18), (0.6, 0.18), (0.87, 0.18)]
    aresta(axes[1], raiz, lider[0]); aresta(axes[1], raiz, lider[1])
    aresta(axes[1], lider[0], folhas[0]); aresta(axes[1], lider[0], folhas[1])
    aresta(axes[1], lider[1], folhas[2]); aresta(axes[1], lider[1], folhas[3])
    no(axes[1], *raiz, "Sup", COR_B)
    no(axes[1], *lider[0], "L1", COR_D); no(axes[1], *lider[1], "L2", COR_D)
    for i, f in enumerate(folhas, 1):
        no(axes[1], *f, f"A{i}", COR_A)
    axes[1].set_title("Hierárquica (árvore)", fontsize=10)

    # (c) group-chat — totalmente conectada
    pts = [(0.5, 0.85), (0.85, 0.55), (0.7, 0.18), (0.3, 0.18), (0.15, 0.55)]
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            aresta(axes[2], pts[i], pts[j], cor="#bbb")
    for i, p in enumerate(pts, 1):
        no(axes[2], *p, f"A{i}", COR_C)
    axes[2].set_title("Group-chat (conectada)", fontsize=10)

    fig.suptitle("Topologias multi-agente: quem fala com quem define o fluxo de coordenação",
                 fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    return _salvar(fig, SLUG_071, "topologias-multi-agente")


# ---------------------------------------------------------------------------
TODAS_AS_FIGURAS = [
    fig_062_agent_loop,
    fig_069_grafo_execucao,
    fig_071_topologias,
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
