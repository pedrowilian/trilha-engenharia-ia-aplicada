#!/usr/bin/env python3
"""Gera, de forma REPRODUTÍVEL, as figuras das lições do módulo M09 (MCP).

As figuras são artefatos de build (PNG) versionados no repositório para que a
pré-visualização local do Markdown (VS Code) as renderize offline, sem depender
de execução. Este script é a fonte da verdade dessas imagens: rodá-lo regenera
TODOS os PNGs do zero, de maneira determinística.

Princípios de reprodutibilidade:
  - Backend "Agg" (sem janela/interatividade);
  - Estilo e tamanhos fixos (sem depender de configuração do usuário);
  - Semente fixa de RNG onde há aleatoriedade.

Uso:
    python trilha/tools/figuras/gerar_figuras_m09.py

As imagens são salvas em:
    trilha/modulos/M09-mcp/assets/<NNN>-<slug>/<nome>.png
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
    "axes.grid": False,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

# --- Localização dos assets (relativa a este arquivo) -----------------------
RAIZ_TRILHA = Path(__file__).resolve().parents[2]   # .../trilha
ASSETS = RAIZ_TRILHA / "modulos" / "M09-mcp" / "assets"

COR_A = "#1f5fa8"   # azul   — host/cliente
COR_B = "#c1432a"   # vermelho— erro/decisão
COR_C = "#2e8b57"   # verde  — servidor/sucesso
COR_D = "#8e6abf"   # roxo   — raciocínio/prompt
COR_E = "#d9920a"   # âmbar  — recurso/dado
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


def _seta(ax, x0, y0, x1, y1, cor="#444", rad=0.0, estilo_linha="-"):
    estilo = dict(arrowstyle="-|>", color=cor, lw=2.0, linestyle=estilo_linha)
    if rad:
        estilo["connectionstyle"] = f"arc3,rad={rad}"
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0), arrowprops=estilo, zorder=1)


# ===========================================================================
# Lição 072 — Arquitetura cliente-servidor do MCP
# ===========================================================================
SLUG_072 = "072-mcp-fundamentos"


def fig_072_cliente_servidor():
    """Arquitetura do MCP: um host contém vários clients (1 por servidor); cada
    client fala um protocolo único com um server que expõe capacidades."""
    fig, ax = plt.subplots(figsize=(9.4, 5.2))
    ax.set_axis_off()

    # Host (caixa grande) contendo o modelo e três clients
    ax.add_patch(plt.Rectangle((0.04, 0.12), 0.40, 0.76,
                               facecolor=COR_A, alpha=0.06,
                               edgecolor=COR_A, lw=1.6, zorder=1))
    ax.text(0.24, 0.83, "Host (aplicação)", ha="center", fontsize=10.5,
            color=COR_A)
    _caixa(ax, 0.24, 0.70, 0.26, 0.12, "Modelo (LLM)", COR_D, 10)
    _caixa(ax, 0.14, 0.46, 0.16, 0.12, "Client A", COR_A, 9.5)
    _caixa(ax, 0.24, 0.30, 0.16, 0.12, "Client B", COR_A, 9.5)
    _caixa(ax, 0.34, 0.46, 0.16, 0.12, "Client C", COR_A, 9.5)

    # Servidores (fora do host)
    _caixa(ax, 0.82, 0.70, 0.26, 0.13, "Server: arquivos\n(resources)", COR_C, 9.5)
    _caixa(ax, 0.82, 0.46, 0.26, 0.13, "Server: GitHub\n(tools)", COR_C, 9.5)
    _caixa(ax, 0.82, 0.22, 0.26, 0.13, "Server: Postgres\n(tools+resources)", COR_C, 9.5)

    # Conexões 1:1 client <-> server (protocolo MCP/JSON-RPC)
    _seta(ax, 0.22, 0.46, 0.69, 0.70, cor="#555")
    _seta(ax, 0.32, 0.30, 0.69, 0.46, cor="#555")
    _seta(ax, 0.42, 0.46, 0.69, 0.22, cor="#555")
    ax.text(0.55, 0.60, "MCP / JSON-RPC", fontsize=9, color="#555",
            rotation=12, ha="center")

    ax.text(0.5, 0.97,
            "MCP: o host hospeda 1 client por servidor; cada conexão fala o mesmo protocolo",
            ha="center", fontsize=10.5)
    ax.set_xlim(0, 1)
    ax.set_ylim(0.08, 1)
    return _salvar(fig, SLUG_072, "arquitetura-cliente-servidor")


# ===========================================================================
# Lição 073 — Primitivas do MCP (resources, tools, prompts)
# ===========================================================================
SLUG_073 = "073-mcp-primitivas"


def fig_073_primitivas():
    """As três primitivas do MCP e quem controla cada uma: resources
    (controlados pela aplicação), tools (pelo modelo), prompts (pelo usuário)."""
    fig, ax = plt.subplots(figsize=(9.6, 4.4))
    ax.set_axis_off()

    _caixa(ax, 0.50, 0.86, 0.30, 0.14, "Server MCP", COR_C, 10.5)

    primitivas = [
        (0.18, "Resources\n(dados/URI)", COR_E, "controle:\naplicação"),
        (0.50, "Tools\n(ações)", COR_C, "controle:\nmodelo"),
        (0.82, "Prompts\n(templates)", COR_D, "controle:\nusuário"),
    ]
    for x, rotulo, cor, controle in primitivas:
        _caixa(ax, x, 0.48, 0.24, 0.16, rotulo, cor, 10)
        _seta(ax, 0.50, 0.79, x, 0.57, cor="#666")
        ax.text(x, 0.22, controle, ha="center", fontsize=9, color="#444")

    ax.text(0.5, 0.985,
            "Primitivas do MCP: o servidor expõe resources, tools e prompts",
            ha="center", fontsize=10.5)
    ax.set_xlim(0, 1)
    ax.set_ylim(0.05, 1.02)
    return _salvar(fig, SLUG_073, "primitivas-mcp")


# ===========================================================================
# Lição 074 — Fluxo de mensagens JSON-RPC
# ===========================================================================
SLUG_074 = "074-mcp-jsonrpc"


def fig_074_fluxo_jsonrpc():
    """Diagrama de sequência simplificado: client emite request (com id), server
    responde com result (mesmo id); uma notification não tem id nem resposta."""
    fig, ax = plt.subplots(figsize=(9.2, 5.2))
    ax.set_axis_off()

    # Duas linhas de vida
    x_cli, x_srv = 0.20, 0.80
    _caixa(ax, x_cli, 0.92, 0.22, 0.10, "Client", COR_A, 10.5)
    _caixa(ax, x_srv, 0.92, 0.22, 0.10, "Server", COR_C, 10.5)
    ax.plot([x_cli, x_cli], [0.10, 0.86], color=CINZA, lw=1.2, zorder=0)
    ax.plot([x_srv, x_srv], [0.10, 0.86], color=CINZA, lw=1.2, zorder=0)

    # request id=1 -> ; <- response id=1
    _seta(ax, x_cli, 0.74, x_srv, 0.70, cor=COR_A)
    ax.text(0.5, 0.77, 'request  id=1  method="tools/call"', ha="center",
            fontsize=9, color=COR_A)
    _seta(ax, x_srv, 0.58, x_cli, 0.54, cor=COR_C)
    ax.text(0.5, 0.61, 'response  id=1  result={...}', ha="center",
            fontsize=9, color=COR_C)

    # notification (sem id, sem resposta)
    _seta(ax, x_cli, 0.36, x_srv, 0.32, cor=COR_D, estilo_linha="--")
    ax.text(0.5, 0.39, 'notification  (sem id)  method="notifications/..."',
            ha="center", fontsize=9, color=COR_D)
    ax.text(0.5, 0.22, "notification não recebe resposta",
            ha="center", fontsize=8.5, color="#777")

    ax.text(0.5, 0.985,
            "JSON-RPC 2.0: request e response casam pelo mesmo id; notification não tem id",
            ha="center", fontsize=10.5)
    ax.set_xlim(0, 1)
    ax.set_ylim(0.08, 1.02)
    return _salvar(fig, SLUG_074, "fluxo-jsonrpc")


# ===========================================================================
# Lição 075 — Servidor e cliente MCP em Python (ciclo completo)
# ===========================================================================
SLUG_075 = "075-mcp-servidores-clientes-python"


def fig_075_ciclo_servidor_cliente():
    """Ciclo completo em Python: o client serializa a request, o transporte
    entrega a linha JSON, o server desserializa, despacha o handler e devolve a
    response serializada de volta."""
    fig, ax = plt.subplots(figsize=(9.8, 4.6))
    ax.set_axis_off()

    _caixa(ax, 0.16, 0.55, 0.20, 0.18, "Cliente\n(monta request)", COR_A, 9.5)
    _caixa(ax, 0.50, 0.78, 0.24, 0.14, "Transporte\n(linha JSON)", CINZA, 9.5)
    _caixa(ax, 0.84, 0.55, 0.22, 0.18, "Servidor\n(despacha handler)", COR_C, 9.5)
    _caixa(ax, 0.50, 0.20, 0.30, 0.14, "Handler da tool\n(executa a ação)", COR_E, 9.5)

    _seta(ax, 0.26, 0.62, 0.40, 0.74, cor=COR_A)
    ax.text(0.30, 0.72, "dumps()", fontsize=8.5, color=COR_A)
    _seta(ax, 0.60, 0.74, 0.74, 0.62, cor="#555")
    ax.text(0.70, 0.72, "loads()", fontsize=8.5, color="#555")
    _seta(ax, 0.80, 0.46, 0.62, 0.26, cor=COR_C)
    ax.text(0.74, 0.36, "chama", fontsize=8.5, color=COR_C)
    _seta(ax, 0.40, 0.22, 0.24, 0.47, cor=COR_E, rad=-0.2)
    ax.text(0.26, 0.30, "result\n(response)", fontsize=8.5, color=COR_E)

    ax.text(0.5, 0.975,
            "Ciclo MCP em Python: request → transporte → despacho → response",
            ha="center", fontsize=10.5)
    ax.set_xlim(0, 1)
    ax.set_ylim(0.06, 1.0)
    return _salvar(fig, SLUG_075, "ciclo-servidor-cliente")


# ---------------------------------------------------------------------------
TODAS_AS_FIGURAS = [
    fig_072_cliente_servidor,
    fig_073_primitivas,
    fig_074_fluxo_jsonrpc,
    fig_075_ciclo_servidor_cliente,
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
