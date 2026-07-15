#!/usr/bin/env python3
"""Gera, de forma REPRODUTIVEL, as figuras das licoes do modulo M07 (RAG e Vector DBs).

As figuras sao artefatos de build (PNG) versionados no repositorio para que a
pre-visualizacao local do Markdown (VS Code) as renderize offline, sem depender
de execucao. Este script e a fonte da verdade dessas imagens: roda-lo regenera
TODOS os PNGs do zero, de maneira deterministica.

Principios de reprodutibilidade:
  - Backend "Agg" (sem janela/interatividade);
  - Estilo e tamanhos fixos (sem depender de configuracao do usuario);
  - Semente fixa de RNG onde ha aleatoriedade.

Uso:
    python trilha/tools/figuras/gerar_figuras_m07.py

As imagens sao salvas em:
    trilha/modulos/M07-rag-vector-dbs/assets/<NNN>-<slug>/<nome>.png
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
ASSETS = RAIZ_TRILHA / "modulos" / "M07-rag-vector-dbs" / "assets"

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


def _caixa(ax, x, y, w, h, texto, cor, fontsize=10):
    ax.add_patch(plt.Rectangle((x, y), w, h, facecolor=cor, alpha=0.18,
                               edgecolor=cor, lw=1.8, zorder=2))
    ax.text(x + w / 2, y + h / 2, texto, ha="center", va="center",
            fontsize=fontsize, color="#1a1a1a", zorder=3)


def _seta(ax, x0, y0, x1, y1, cor="#444"):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", color=cor, lw=2.0))


# ===========================================================================
# Licao 055 - Fundamentos de RAG
# ===========================================================================
SLUG_055 = "055-rag-fundamentos"


def fig_055_pipeline_rag():
    """Pipeline retrieve-augment-generate: da pergunta a resposta fundamentada."""
    fig, ax = plt.subplots(figsize=(9.2, 3.6))
    ax.set_axis_off()
    y, h = 0.35, 0.30
    _caixa(ax, 0.00, y, 0.15, h, "Pergunta", CINZA)
    _caixa(ax, 0.21, y, 0.18, h, "Retrieve\n(indice/corpus)", COR_A)
    _caixa(ax, 0.45, y, 0.18, h, "Augment\n(monta prompt)", COR_C)
    _caixa(ax, 0.69, y, 0.16, h, "Generate\n(LLM)", COR_D)
    _caixa(ax, 0.88, y, 0.12, h, "Resposta\n+ fontes", COR_B)
    for x0, x1 in [(0.15, 0.21), (0.39, 0.45), (0.63, 0.69), (0.85, 0.88)]:
        _seta(ax, x0, y + h / 2, x1, y + h / 2)
    # corpus alimentando o retrieve
    _caixa(ax, 0.21, 0.80, 0.18, 0.16, "Base de documentos", CINZA, fontsize=9)
    _seta(ax, 0.30, 0.80, 0.30, y + h, COR_A)
    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(0.2, 1.05)
    ax.set_title("RAG: recuperar contexto, aumentar o prompt e gerar com fundamentacao")
    return _salvar(fig, SLUG_055, "pipeline-rag")


# ===========================================================================
# Licao 056 - Chunking e estrategias de indexacao
# ===========================================================================
SLUG_056 = "056-chunking-indexacao"


def fig_056_estrategias_chunking():
    """Compara chunking de tamanho fixo (sem sobreposicao) com janela deslizante."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9.0, 4.4))
    n = 12  # tokens do documento
    for ax in (ax1, ax2):
        ax.set_xlim(-0.3, n + 0.3)
        ax.set_ylim(0, 3)
        ax.set_yticks([])
        for i in range(n):
            ax.add_patch(plt.Rectangle((i, 1.2), 0.9, 0.6, facecolor=CINZA,
                                       alpha=0.25, edgecolor=CINZA))
            ax.text(i + 0.45, 1.5, f"t{i}", ha="center", va="center", fontsize=8)

    # Fixo: [0-3][4-7][8-11]
    cores = [COR_A, COR_C, COR_D]
    for k, ini in enumerate(range(0, n, 4)):
        ax1.add_patch(plt.Rectangle((ini - 0.05, 1.1), 4.0, 0.8, fill=False,
                                    edgecolor=cores[k % 3], lw=2.2))
    ax1.set_title("Chunking de tamanho fixo (4 tokens, sem sobreposicao)")

    # Sobreposto: [0-3][2-5][4-7][6-9][8-11], passo 2
    janelas = [(0, 4), (2, 6), (4, 8), (6, 10), (8, 12)]
    for k, (ini, fim) in enumerate(janelas):
        ax2.add_patch(plt.Rectangle((ini - 0.05, 0.6 + 0.18 * k),
                                    (fim - ini), 0.16, facecolor=cores[k % 3],
                                    alpha=0.55, edgecolor="none"))
    ax2.set_title("Janela deslizante (tamanho 4, passo 2, com sobreposicao)")

    fig.tight_layout()
    return _salvar(fig, SLUG_056, "estrategias-chunking")


# ===========================================================================
# Licao 057 - Pipeline RAG basico
# ===========================================================================
SLUG_057 = "057-pipeline-rag-basico"


def fig_057_scores_topk():
    """Pontuacoes de similaridade por documento; os top-k recuperados em destaque."""
    docs = [f"d{i}" for i in range(1, 9)]
    scores = np.array([0.81, 0.22, 0.74, 0.10, 0.65, 0.31, 0.05, 0.48])
    k = 3
    ordem = np.argsort(-scores)
    topk = set(ordem[:k].tolist())
    cores = [COR_C if i in topk else CINZA for i in range(len(docs))]

    fig, ax = plt.subplots(figsize=(8.0, 4.2))
    ax.bar(docs, scores, color=cores, edgecolor="white")
    corte = scores[ordem[k - 1]]
    ax.axhline(corte, color=COR_B, ls="--", lw=1.5)
    ax.text(len(docs) - 0.5, corte + 0.02, f"corte top-{k}", color=COR_B,
            ha="right", fontsize=9)
    ax.set_ylabel("similaridade com a consulta")
    ax.set_ylim(0, 1.0)
    ax.set_title("Pipeline RAG: ordena por similaridade e recupera os top-k")
    return _salvar(fig, SLUG_057, "scores-topk")


# ===========================================================================
# Licao 058 - Vector databases
# ===========================================================================
SLUG_058 = "058-vector-databases"


def fig_058_flat_vs_particionado():
    """Indice flat (varre tudo) vs indice particionado (varre so a particao probada)."""
    rng = np.random.default_rng(13)
    centros = np.array([[2, 2], [7, 3], [4, 7]])
    pts = np.vstack([c + rng.normal(0, 0.7, size=(12, 2)) for c in centros])
    consulta = np.array([7.2, 3.1])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 4.6))
    for ax in (ax1, ax2):
        ax.set_aspect("equal")
        ax.set_xlim(-0.5, 9.5)
        ax.set_ylim(-0.5, 9.5)
        ax.scatter([consulta[0]], [consulta[1]], marker="*", s=200,
                   color=COR_B, edgecolor="black", zorder=5)

    ax1.scatter(pts[:, 0], pts[:, 1], s=45, color=COR_A, zorder=3)
    for p in pts:
        ax1.plot([consulta[0], p[0]], [consulta[1], p[1]], color=CINZA,
                 lw=0.5, alpha=0.6, zorder=2)
    ax1.set_title("Flat: compara a consulta com TODOS os vetores")

    cores = [COR_A, COR_C, COR_D]
    probada = int(np.argmin(np.linalg.norm(centros - consulta, axis=1)))
    for ci in range(3):
        bloco = pts[ci * 12:(ci + 1) * 12]
        alpha = 1.0 if ci == probada else 0.25
        ax2.scatter(bloco[:, 0], bloco[:, 1], s=45, color=cores[ci], alpha=alpha,
                    zorder=3)
        ax2.scatter([centros[ci, 0]], [centros[ci, 1]], marker="X", s=90,
                    color=cores[ci], edgecolor="black", zorder=4)
        if ci == probada:
            for p in bloco:
                ax2.plot([consulta[0], p[0]], [consulta[1], p[1]], color=CINZA,
                         lw=0.5, alpha=0.6, zorder=2)
    ax2.set_title("Particionado: varre so a particao mais proxima")

    fig.tight_layout()
    return _salvar(fig, SLUG_058, "flat-vs-particionado")


# ===========================================================================
# Licao 059 - RAG hibrido (denso + esparso)
# ===========================================================================
SLUG_059 = "059-rag-hibrido"


def fig_059_fusao_hibrida():
    """Fusao de duas listas ranqueadas (densa e esparsa) em um ranking unico."""
    densa = ["d3", "d1", "d5", "d2"]
    esparsa = ["d1", "d4", "d3", "d6"]
    fundida = ["d1", "d3", "d4", "d5"]

    fig, ax = plt.subplots(figsize=(8.6, 4.8))
    ax.set_axis_off()
    colunas = [(0.10, densa, COR_A, "Densa\n(cosseno)"),
               (0.45, esparsa, COR_C, "Esparsa\n(BM25)"),
               (0.80, fundida, COR_B, "Fusao\n(RRF)")]
    pos = {}
    for x, lista, cor, titulo in colunas:
        ax.text(x + 0.06, 0.92, titulo, ha="center", va="center", fontsize=10,
                fontweight="bold", color=cor)
        for r, did in enumerate(lista):
            yy = 0.78 - r * 0.16
            _caixa(ax, x, yy, 0.12, 0.11, f"{r+1}. {did}", cor, fontsize=9)
            pos[(titulo, did)] = (x + 0.12, yy + 0.055)
            pos.setdefault(("in", did), []) if False else None
    # setas das listas de origem para a fusao (quando o doc sobrevive)
    origem = {"d1": [("Densa\n(cosseno)", 1), ("Esparsa\n(BM25)", 0)],
              "d3": [("Densa\n(cosseno)", 0), ("Esparsa\n(BM25)", 2)],
              "d5": [("Densa\n(cosseno)", 2)],
              "d4": [("Esparsa\n(BM25)", 1)]}
    destino = {did: (0.80, 0.78 - r * 0.16 + 0.055) for r, did in enumerate(fundida)}
    for did, fontes in origem.items():
        for titulo, _r in fontes:
            x0, y0 = pos[(titulo, did)]
            x1, y1 = destino[did]
            ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                        arrowprops=dict(arrowstyle="-|>", color=CINZA, lw=1.2,
                                        alpha=0.8))
    ax.set_xlim(0, 1.0)
    ax.set_ylim(0.05, 1.0)
    ax.set_title("RAG hibrido: duas listas ranqueadas fundidas em um ranking unico")
    return _salvar(fig, SLUG_059, "fusao-hibrida")


# ===========================================================================
# Licao 060 - RAG multi-index e re-ranking
# ===========================================================================
SLUG_060 = "060-rag-multi-index-reranking"


def fig_060_funil_rerank():
    """Funil de duas etapas: recuperacao ampla (recall) -> re-ranking preciso."""
    fig, ax = plt.subplots(figsize=(8.4, 4.6))
    ax.set_axis_off()
    # Etapa 1: muitos candidatos
    ax.add_patch(plt.Polygon([(0.05, 0.85), (0.55, 0.85), (0.42, 0.45),
                              (0.18, 0.45)], closed=True, facecolor=COR_A,
                             alpha=0.18, edgecolor=COR_A, lw=1.8))
    ax.text(0.30, 0.65, "Etapa 1: recuperacao ampla\n(barata, alto recall)\n~50 candidatos",
            ha="center", va="center", fontsize=10, color=COR_A)
    # Etapa 2: poucos, re-ranqueados
    ax.add_patch(plt.Polygon([(0.18, 0.40), (0.42, 0.40), (0.36, 0.12),
                              (0.24, 0.12)], closed=True, facecolor=COR_B,
                             alpha=0.18, edgecolor=COR_B, lw=1.8))
    ax.text(0.30, 0.26, "Etapa 2: re-ranking\n(caro, alta precisao)\ntop-3",
            ha="center", va="center", fontsize=10, color=COR_B)
    _seta(ax, 0.30, 0.45, 0.30, 0.40, "#444")
    # multi-index alimentando a etapa 1
    _caixa(ax, 0.68, 0.72, 0.27, 0.13, "Indice A (FAQ)", COR_C, fontsize=9)
    _caixa(ax, 0.68, 0.54, 0.27, 0.13, "Indice B (docs)", COR_D, fontsize=9)
    _seta(ax, 0.68, 0.785, 0.55, 0.72, COR_C)
    _seta(ax, 0.68, 0.605, 0.52, 0.62, COR_D)
    ax.set_xlim(0, 1.0)
    ax.set_ylim(0.05, 0.95)
    ax.set_title("Multi-index + re-ranking: recuperar muito, depois refinar pouco")
    return _salvar(fig, SLUG_060, "funil-rerank")


# ===========================================================================
# Licao 061 - Agentic RAG
# ===========================================================================
SLUG_061 = "061-agentic-rag"


def fig_061_loop_agentic():
    """Laco do Agentic RAG: decidir, recuperar, avaliar e iterar ou responder."""
    fig, ax = plt.subplots(figsize=(7.8, 5.0))
    ax.set_axis_off()
    centros = {
        "Decidir\n(buscar?)": (0.50, 0.82, COR_A),
        "Recuperar": (0.82, 0.50, COR_C),
        "Avaliar\nsuficiencia": (0.50, 0.20, COR_D),
        "Refinar\nconsulta": (0.18, 0.50, COR_E),
    }
    pts = {}
    for txt, (x, y, cor) in centros.items():
        ax.add_patch(plt.Circle((x, y), 0.13, facecolor=cor, alpha=0.18,
                                edgecolor=cor, lw=1.8, zorder=2))
        ax.text(x, y, txt, ha="center", va="center", fontsize=9.5, zorder=3)
        pts[txt] = (x, y)
    ciclo = ["Decidir\n(buscar?)", "Recuperar", "Avaliar\nsuficiencia",
             "Refinar\nconsulta", "Decidir\n(buscar?)"]
    for a, b in zip(ciclo, ciclo[1:]):
        xa, ya = pts[a]
        xb, yb = pts[b]
        dx, dy = xb - xa, yb - ya
        norm = (dx ** 2 + dy ** 2) ** 0.5
        ux, uy = dx / norm, dy / norm
        ax.annotate("", xy=(xb - 0.13 * ux, yb - 0.13 * uy),
                    xytext=(xa + 0.13 * ux, ya + 0.13 * uy),
                    arrowprops=dict(arrowstyle="-|>", color="#555", lw=1.8,
                                    connectionstyle="arc3,rad=0.18"))
    # saida: responder
    _caixa(ax, 0.40, 0.00, 0.20, 0.08, "Responder + fontes", COR_B, fontsize=9)
    _seta(ax, 0.50, 0.07, 0.50, 0.08, COR_B)
    ax.text(0.66, 0.10, "suficiente", fontsize=8, color=COR_B)
    ax.set_xlim(0, 1.0)
    ax.set_ylim(-0.02, 1.0)
    ax.set_title("Agentic RAG: o agente decide buscar, avalia e itera ate responder")
    return _salvar(fig, SLUG_061, "loop-agentic-rag")


# ---------------------------------------------------------------------------
TODAS_AS_FIGURAS = [
    fig_055_pipeline_rag,
    fig_056_estrategias_chunking,
    fig_057_scores_topk,
    fig_058_flat_vs_particionado,
    fig_059_fusao_hibrida,
    fig_060_funil_rerank,
    fig_061_loop_agentic,
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
