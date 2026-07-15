#!/usr/bin/env python3
"""Gerador do índice navegável da Trilha (R11.1, R11.2).

Regenera, em `trilha/README.md`:
  • a tabela de lições (uma linha por lição, na ordem de estudo 001→104), entre
    os marcadores INICIO-LINHAS-LICOES / FIM-LINHAS-LICOES;
  • a linha "▶ Retomar em", a partir do ponto de retomada calculado sobre
    progresso.yaml (R11.6).

As lições são parseadas com o mesmo carregador do validador
(`carregar_licoes`), de modo que a tabela permaneça consistente com a fonte da
verdade do front-matter. O nome legível do módulo (ex.: "M01 — Fundamentos de
ML") é extraído da linha "> **Módulo:** ..." do corpo da lição.

Uso:
    python tools/gerar_indice.py [--trilha trilha/] [--check]

    --check  não escreve; apenas verifica se o README já está atualizado
             (código de saída 1 se houver diferença).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Permite rodar como script (`python tools/gerar_indice.py`) ou como módulo.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from validar_trilha import (  # noqa: E402
    EstadoLicao,
    Licao,
    calcular_ponto_de_retomada,
    carregar_licoes,
    estado_da_licao,
    ler_progresso,
)

MARCADOR_INICIO = "<!-- INICIO-LINHAS-LICOES (gerado na tarefa 26) -->"
MARCADOR_FIM = "<!-- FIM-LINHAS-LICOES -->"

# Rótulos de estado exibidos no índice (R11.3).
SIMBOLO_ESTADO = {
    EstadoLicao.NAO_INICIADA: "☐ não iniciada",
    EstadoLicao.EM_ANDAMENTO: "◐ em andamento",
    EstadoLicao.CONCLUIDA: "☑ concluída",
}

_RE_MODULO_CORPO = re.compile(r">\s*\*\*Módulo:\*\*\s*(.+?)\s*(?:·|$)", re.MULTILINE)


def _nome_modulo(licao: Licao) -> str:
    """Nome legível do módulo (ex.: "M01 — Fundamentos de ML").

    Preferimos a linha "> **Módulo:** ..." do corpo (forma legível). Como
    fallback, usamos o prefixo Mxx do campo `modulo` do front-matter.
    """
    m = _RE_MODULO_CORPO.search(licao.corpo)
    if m:
        return m.group(1).strip()
    return licao.modulo


def _link_relativo(licao: Licao) -> str:
    """Caminho do arquivo da lição relativo ao README (raiz da Trilha)."""
    # `artefato` já é relativo à raiz da Trilha (ex.: modulos/M00-.../001-....md).
    return licao.artefato.replace("\\", "/")


def _prereqs_ordinais(licao: Licao, por_id: dict[str, Licao]) -> str:
    """Lista de ordinais dos pré-requisitos (ex.: "007, 012") ou "—"."""
    ordinais = []
    for pid in licao.pre_requisitos:
        alvo = por_id.get(pid)
        if alvo is not None:
            ordinais.append(alvo.ordinal)
    if not ordinais:
        return "—"
    return ", ".join(f"{o:03d}" for o in sorted(ordinais))


def gerar_linhas_tabela(licoes: list[Licao],
                        progresso: dict[str, EstadoLicao]) -> list[str]:
    """Gera as linhas da tabela (uma por lição) na ordem de estudo 001→N."""
    por_id = {l.id: l for l in licoes}
    ordenadas = sorted(licoes, key=lambda l: l.ordinal)
    linhas: list[str] = []
    for l in ordenadas:
        ordinal = f"{l.ordinal:03d}"
        link = _link_relativo(l)
        modulo = _nome_modulo(l)
        titulo = l.titulo
        prereqs = _prereqs_ordinais(l, por_id)
        estado = SIMBOLO_ESTADO[estado_da_licao(l.ordinal, progresso)]
        linhas.append(
            f"| [{ordinal}]({link}) | {modulo} | {titulo} | {prereqs} | {estado} |"
        )
    return linhas


def gerar_linha_retomada(licoes: list[Licao],
                         progresso: dict[str, EstadoLicao]) -> str:
    """Linha "▶ Retomar em" a partir do ponto de retomada (R11.6)."""
    ponto = calcular_ponto_de_retomada(licoes, progresso)
    if ponto is None:
        if licoes:
            return "▶ **Trilha completa** — todas as lições foram concluídas. 🎉"
        return "▶ _Nenhuma lição encontrada na Trilha._"
    link = _link_relativo(ponto)
    return f"▶ **Retomar em:** [#{ponto.ordinal:03d} — {ponto.titulo}]({link})"


def _substituir_tabela(conteudo: str, linhas: list[str]) -> str:
    inicio = conteudo.find(MARCADOR_INICIO)
    fim = conteudo.find(MARCADOR_FIM)
    if inicio < 0 or fim < 0 or fim < inicio:
        raise SystemExit(
            f"ERRO: marcadores '{MARCADOR_INICIO}' / '{MARCADOR_FIM}' não "
            "encontrados no README.md."
        )
    bloco = MARCADOR_INICIO + "\n" + "\n".join(linhas) + "\n" + MARCADOR_FIM
    return conteudo[:inicio] + bloco + conteudo[fim + len(MARCADOR_FIM):]


def _substituir_retomada(conteudo: str, linha: str) -> str:
    # Substitui a primeira linha de corpo que começa com "▶ " (não o heading
    # "## ▶ Retomar em").
    novo, n = re.subn(r"^▶ .*$", lambda _m: linha, conteudo, count=1, flags=re.MULTILINE)
    if n == 0:
        raise SystemExit("ERRO: marcador de retomada ('▶ ...') não encontrado no README.md.")
    return novo


def gerar_readme(conteudo: str, licoes: list[Licao],
                 progresso: dict[str, EstadoLicao]) -> str:
    linhas = gerar_linhas_tabela(licoes, progresso)
    conteudo = _substituir_tabela(conteudo, linhas)
    conteudo = _substituir_retomada(conteudo, gerar_linha_retomada(licoes, progresso))
    return conteudo


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Gera o índice navegável da Trilha.")
    parser.add_argument("--trilha", default=None, type=Path,
                        help="diretório raiz da Trilha (default: detectado a partir de tools/).")
    parser.add_argument("--check", action="store_true",
                        help="não escreve; verifica se o README já está atualizado.")
    args = parser.parse_args(argv)

    trilha_dir = args.trilha or Path(__file__).resolve().parent.parent
    readme = trilha_dir / "README.md"
    progresso_yaml = trilha_dir / "progresso.yaml"

    licoes, violacoes = carregar_licoes(trilha_dir)
    if violacoes:
        for v in violacoes:
            print(f"AVISO (metadados): {v}", file=sys.stderr)
    if not licoes:
        print("ERRO: nenhuma lição encontrada em modulos/.", file=sys.stderr)
        return 1

    progresso = ler_progresso(progresso_yaml)
    original = readme.read_text(encoding="utf-8")
    atualizado = gerar_readme(original, licoes, progresso)

    if args.check:
        if original != atualizado:
            print("README.md desatualizado: rode `python tools/gerar_indice.py`.", file=sys.stderr)
            return 1
        print("README.md está atualizado.")
        return 0

    readme.write_text(atualizado, encoding="utf-8")
    print(f"OK: índice regenerado com {len(licoes)} lições.")
    print(gerar_linha_retomada(licoes, progresso))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
