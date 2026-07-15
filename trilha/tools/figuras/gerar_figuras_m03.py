#!/usr/bin/env python3
"""Gera, de forma REPRODUTÍVEL, as figuras das lições do módulo M03.

As figuras são artefatos de build (PNG) versionados no repositório para que a
pré-visualização local do Markdown (VS Code) as renderize offline, sem depender
de execução. Este script é a fonte da verdade dessas imagens: rodá-lo regenera
TODOS os PNGs do zero, de maneira determinística.

Princípios de reprodutibilidade:
  - Backend "Agg" (sem janela/interatividade);
  - Estilo e tamanhos fixos (sem depender de configuração do usuário);
  - Semente fixa de RNG onde há aleatoriedade (nuvens de pontos, amostragem).

Uso:
    python trilha/tools/figuras/gerar_figuras_m03.py

As imagens são salvas em:
    trilha/modulos/M03-nlp-tokenizacao-embeddings-busca-vetorial/assets/<NNN>-<slug>/<nome>.png
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
ASSETS = RAIZ_TRILHA / "modulos" / "M03-nlp-tokenizacao-embeddings-busca-vetorial" / "assets"

COR_A = "#1f5fa8"
COR_B = "#c1432a"
COR_C = "#2e8b57"
COR_D = "#8e6abf"
CINZA = "#9aa7b5"


def _salvar(fig, slug: str, nome: str) -> Path:
    """Salva a figura em assets/<slug>/<nome>.png e fecha a figura."""
    destino = ASSETS / slug / f"{nome}.png"
    destino.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(destino, bbox_inches="tight")
    plt.close(fig)
    return destino


# ===========================================================================
# Lição 032 — Fundamentos de NLP e representação de texto
# ===========================================================================
SLUG_032 = "032-nlp-fundamentos"


def fig_032_esparso_vs_denso():
    """Compara a representação esparsa (bag-of-words, vocabulário grande,
    quase tudo zero) com a representação densa (embedding curto e contínuo)."""
    rng = np.random.default_rng(7)
    # Bag-of-words: vetor longo (40 dims) com pouquíssimas posições não-nulas.
    V = 40
    esparso = np.zeros(V)
    posicoes = [3, 11, 18, 27, 34]
    contagens = [2, 1, 3, 1, 1]
    for p, c in zip(posicoes, contagens):
        esparso[p] = c
    # Embedding denso: vetor curto (8 dims), todas as posições ativas.
    denso = rng.normal(0, 1, size=8).round(2)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8.2, 5.2))
    ax1.bar(np.arange(V), esparso, color=COR_A, width=0.8)
    ax1.set_title("Esparso — bag-of-words (40 dims, 5 não-nulas)")
    ax1.set_xlabel("índice do vocabulário")
    ax1.set_ylabel("contagem")
    ax1.set_ylim(0, 3.5)

    ax2.bar(np.arange(len(denso)), denso, color=COR_C, width=0.6)
    ax2.set_title("Denso — embedding (8 dims, todas ativas)")
    ax2.set_xlabel("dimensão latente")
    ax2.set_ylabel("valor")
    ax2.axhline(0, color="black", lw=0.8)

    fig.tight_layout()
    return _salvar(fig, SLUG_032, "esparso-vs-denso")


# ===========================================================================
# Lição 033 — Tokenização: BPE, WordPiece, SentencePiece
# ===========================================================================
SLUG_033 = "033-tokenizacao"


def fig_033_merges_bpe():
    """Ilustra a sequência de merges do BPE: de caracteres soltos a subpalavras."""
    estagios = [
        ("início (caracteres)", ["l", "o", "w", "e", "r", " ", "l", "o", "w"]),
        ("merge 1:  l+o → lo", ["lo", "w", "e", "r", " ", "lo", "w"]),
        ("merge 2:  lo+w → low", ["low", "e", "r", " ", "low"]),
        ("merge 3:  e+r → er", ["low", "er", " ", "low"]),
    ]
    fig, ax = plt.subplots(figsize=(8.4, 4.4))
    ax.set_axis_off()
    y = len(estagios)
    for rotulo, tokens in estagios:
        ax.text(-0.02, y, rotulo, ha="right", va="center", fontsize=10,
                color="#333", fontweight="bold")
        x = 0.0
        for tok in tokens:
            largura = 0.045 * len(tok) + 0.045
            cor = COR_B if len(tok) > 1 else COR_A
            ax.add_patch(plt.Rectangle((x, y - 0.28), largura, 0.56,
                                       facecolor=cor, alpha=0.20,
                                       edgecolor=cor, lw=1.4))
            ax.text(x + largura / 2, y, repr(tok).strip("'") if tok != " " else "␣",
                    ha="center", va="center", fontsize=11)
            x += largura + 0.012
        y -= 1
    ax.set_xlim(-0.18, 1.05)
    ax.set_ylim(0.4, len(estagios) + 0.6)
    ax.set_title("BPE: merges sucessivos do par mais frequente formam subpalavras")
    return _salvar(fig, SLUG_033, "merges-bpe")


# ===========================================================================
# Lição 034 — Embeddings: word2vec, GloVe, contextuais
# ===========================================================================
SLUG_034 = "034-embeddings"


def fig_034_clusters_semanticos():
    """Espaço de embeddings 2D com clusters semânticos (animais, realeza, frutas)."""
    rng = np.random.default_rng(42)
    centros = {
        "animais": (np.array([-2.2, 1.8]), COR_A,
                    ["gato", "cachorro", "leão", "cavalo"]),
        "realeza": (np.array([2.0, 2.0]), COR_B,
                    ["rei", "rainha", "príncipe", "trono"]),
        "frutas": (np.array([0.0, -2.2]), COR_C,
                   ["maçã", "banana", "uva", "manga"]),
    }
    fig, ax = plt.subplots(figsize=(6.6, 6.0))
    for nome, (centro, cor, palavras) in centros.items():
        pts = centro + rng.normal(0, 0.45, size=(len(palavras), 2))
        ax.scatter(pts[:, 0], pts[:, 1], s=70, color=cor, label=nome,
                   edgecolor="white", zorder=3)
        for (px, py), pal in zip(pts, palavras):
            ax.annotate(pal, (px, py), textcoords="offset points",
                        xytext=(6, 4), fontsize=9, color=cor)
    ax.axhline(0, color="black", lw=0.6, alpha=0.4)
    ax.axvline(0, color="black", lw=0.6, alpha=0.4)
    ax.set_aspect("equal")
    ax.legend(loc="upper center", fontsize=9, ncol=3)
    ax.set_title("Embeddings agrupam palavras de significado próximo")
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4.4)
    return _salvar(fig, SLUG_034, "clusters-semanticos")


# ===========================================================================
# Lição 035 — Métricas de distância e similaridade
# ===========================================================================
SLUG_035 = "035-metricas-distancia-similaridade"


def fig_035_cosseno_vs_euclidiana():
    """Mostra que o cosseno mede ângulo (direção) e a L2 mede separação (posição)."""
    q = np.array([1.0, 1.0])
    a = np.array([2.0, 2.0])   # mesma direção de q, mais longe
    b = np.array([1.4, 0.2])   # perto em L2, mas direção diferente
    fig, ax = plt.subplots(figsize=(6.4, 5.6))

    def seta(vec, cor, rot):
        ax.annotate("", xy=(vec[0], vec[1]), xytext=(0, 0),
                    arrowprops=dict(arrowstyle="-|>", color=cor, lw=2.2))
        ax.text(vec[0] * 1.04, vec[1] * 1.04, rot, color=cor,
                fontsize=12, fontweight="bold")

    seta(q, COR_A, r"$q$")
    seta(a, COR_B, r"$a$ (mesma direção)")
    seta(b, COR_C, r"$b$ (perto em L2)")
    # distância L2 de q a b
    ax.plot([q[0], b[0]], [q[1], b[1]], "--", color=COR_C, alpha=0.7)
    ax.text((q[0] + b[0]) / 2 + 0.05, (q[1] + b[1]) / 2, "L2 pequena",
            color=COR_C, fontsize=9)
    # arco do ângulo entre q e b
    ang_q = np.arctan2(q[1], q[0])
    ang_b = np.arctan2(b[1], b[0])
    ts = np.linspace(ang_b, ang_q, 40)
    ax.plot(0.5 * np.cos(ts), 0.5 * np.sin(ts), color="#444", lw=1.2)
    ax.text(0.6, 0.32, r"$\theta$", fontsize=13)
    ax.set_aspect("equal")
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(0, color="black", lw=0.8)
    ax.set_xlim(-0.3, 2.6)
    ax.set_ylim(-0.3, 2.6)
    ax.set_title("Cosseno mede ângulo; distância euclidiana mede separação")
    return _salvar(fig, SLUG_035, "cosseno-vs-euclidiana")


# ===========================================================================
# Lição 036 — Busca vetorial e k-NN exato
# ===========================================================================
SLUG_036 = "036-busca-vetorial-knn-exato"


def fig_036_knn_query():
    """Consulta k-NN: ponto de consulta e seus k=3 vizinhos mais próximos."""
    rng = np.random.default_rng(3)
    base = rng.uniform(0, 10, size=(40, 2))
    consulta = np.array([5.0, 5.0])
    dists = np.linalg.norm(base - consulta, axis=1)
    ordem = np.argsort(dists)
    k = 3
    vizinhos = ordem[:k]
    raio = dists[ordem[k - 1]]

    fig, ax = plt.subplots(figsize=(6.4, 6.0))
    ax.scatter(base[:, 0], base[:, 1], s=40, color=CINZA, label="documentos",
               zorder=2)
    ax.scatter(base[vizinhos, 0], base[vizinhos, 1], s=90, color=COR_C,
               edgecolor="black", label=f"{k} vizinhos mais próximos", zorder=4)
    ax.scatter([consulta[0]], [consulta[1]], s=160, color=COR_B, marker="*",
               edgecolor="black", label="consulta", zorder=5)
    circ = plt.Circle(consulta, raio, color=COR_B, fill=False, ls="--", lw=1.5)
    ax.add_patch(circ)
    for i in vizinhos:
        ax.plot([consulta[0], base[i, 0]], [consulta[1], base[i, 1]],
                color=COR_C, lw=1.0, alpha=0.7, zorder=3)
    ax.set_aspect("equal")
    ax.legend(loc="upper left", fontsize=9)
    ax.set_title("k-NN exato: varre todos os pontos e retorna os k mais próximos")
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-0.5, 11.0)
    return _salvar(fig, SLUG_036, "knn-query")


# ===========================================================================
# Lição 037 — Busca aproximada (ANN) e trade-offs recall/latência
# ===========================================================================
SLUG_037 = "037-busca-aproximada-ann"


def fig_037_recall_latencia():
    """Curva de trade-off: mais esforço de busca eleva o recall e a latência."""
    esforco = np.linspace(1, 100, 200)
    recall = 1 - np.exp(-esforco / 18.0)          # satura perto de 1
    latencia = 0.2 + 0.06 * esforco               # cresce linearmente (ms)

    fig, ax1 = plt.subplots(figsize=(7.0, 4.8))
    ax1.plot(esforco, recall, color=COR_A, lw=2.2, label="recall")
    ax1.set_xlabel("esforço de busca (nós visitados / ef)")
    ax1.set_ylabel("recall@k", color=COR_A)
    ax1.tick_params(axis="y", labelcolor=COR_A)
    ax1.set_ylim(0, 1.05)

    ax2 = ax1.twinx()
    ax2.plot(esforco, latencia, color=COR_B, lw=2.2, ls="--", label="latência")
    ax2.set_ylabel("latência (ms)", color=COR_B)
    ax2.tick_params(axis="y", labelcolor=COR_B)
    ax2.grid(False)

    # ponto "joelho" da curva (bom equilíbrio)
    idx = np.argmin(np.abs(recall - 0.95))
    ax1.scatter([esforco[idx]], [recall[idx]], color=COR_C, s=70, zorder=5)
    ax1.annotate("joelho (~0.95 recall)", (esforco[idx], recall[idx]),
                 textcoords="offset points", xytext=(10, -22), fontsize=9,
                 color=COR_C)
    ax1.set_title("ANN: recall e latência crescem juntos com o esforço de busca")
    return _salvar(fig, SLUG_037, "recall-latencia")


# ===========================================================================
# Lição 038 — HNSW por dentro
# ===========================================================================
SLUG_038 = "038-hnsw"


def fig_038_camadas_hnsw():
    """Grafo hierárquico navegável: camadas esparsas no topo, densas na base."""
    rng = np.random.default_rng(11)
    fig, ax = plt.subplots(figsize=(7.4, 5.6))
    ax.set_axis_off()

    camadas = [
        (2.6, [0.2, 0.8], "Camada 2 (esparsa)"),
        (1.4, [0.1, 0.45, 0.8], "Camada 1"),
        (0.2, np.linspace(0.06, 0.94, 7), "Camada 0 (todos os nós)"),
    ]
    coords = []
    for y, xs, rotulo in camadas:
        xs = np.array(xs)
        ax.text(-0.04, y, rotulo, ha="right", va="center", fontsize=9,
                color="#333")
        linha = []
        for x in xs:
            ax.add_patch(plt.Circle((x, y), 0.03, color=COR_A, zorder=4))
            linha.append((x, y))
        # arestas dentro da camada (vizinhos consecutivos)
        for i in range(len(linha) - 1):
            ax.plot([linha[i][0], linha[i + 1][0]],
                    [linha[i][1], linha[i + 1][1]],
                    color=CINZA, lw=1.0, zorder=2)
        coords.append(linha)

    # arestas verticais entre camadas (mesmo nó descendo)
    for cima, baixo in [(coords[0], coords[1]), (coords[1], coords[2])]:
        for (x, y) in cima:
            alvo = min(baixo, key=lambda p: abs(p[0] - x))
            ax.plot([x, alvo[0]], [y, alvo[1]], color=COR_B, lw=1.2,
                    ls=":", zorder=3)

    # caminho de busca (greedy) do topo até a base
    entrada = coords[0][1]
    ax.scatter([entrada[0]], [entrada[1]], s=120, color=COR_C,
               edgecolor="black", zorder=6)
    ax.annotate("entrada", entrada, textcoords="offset points",
                xytext=(8, 8), fontsize=9, color=COR_C)
    ax.set_xlim(-0.22, 1.05)
    ax.set_ylim(-0.1, 3.0)
    ax.set_title("HNSW: camadas hierárquicas — saltos longos no topo, refino na base")
    return _salvar(fig, SLUG_038, "camadas-hnsw")


# ---------------------------------------------------------------------------
TODAS_AS_FIGURAS = [
    fig_032_esparso_vs_denso,
    fig_033_merges_bpe,
    fig_034_clusters_semanticos,
    fig_035_cosseno_vs_euclidiana,
    fig_036_knn_query,
    fig_037_recall_latencia,
    fig_038_camadas_hnsw,
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
