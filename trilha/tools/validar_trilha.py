#!/usr/bin/env python3
"""Validador da Trilha de Engenharia de IA Aplicada.

Verifica as propriedades de correção do currículo sobre os artefatos
versionados (lições em Markdown + front-matter YAML, competencias.yaml,
progresso.yaml). O comportamento é de *coleta exaustiva* (não fail-fast):
acumula todas as não-conformidades e as reporta de uma vez.

Uso:
    python tools/validar_trilha.py [--trilha trilha/] [--json]

Código de saída: 0 se todas as propriedades passam; 1 caso contrário.

Códigos de violação (ver design "Error Handling"):
    METADADOS_INVALIDOS      front-matter YAML inválido/ausente
    CICLO                    dependência circular entre lições (R5.6)
    REF_PENDENTE             pré-requisito que referencia lição inexistente (R5.5)
    ARESTA_FRENTE            pré-requisito com ordinal >= ao da própria lição (R5.1/5.2)
    ORDINAL_NAO_CONTIGUO     ordinais não formam {1..N} sem lacuna/repetição (R5.4)
    TEMPLATE_NAO_CONFORME    regra estrutural do template violada (R1.12, R2, R3, R12)
    TOPICO_AUSENTE           tópico obrigatório sem lição (R1.11, R6, R7.7)
    EXEMPLO_FALHOU           exemplo/solução não executa ou diverge da saída (R4.6, R12.4)
    OUTCOME_ORFAO            resultado de aprendizagem sem exigência/lição (R8.6)
    EXIGENCIA_SEM_LICAO      exigência de mercado sem lição correspondente (R8.5)
    ROUNDTRIP_DIVERGENTE     round-trip parse->serialize->parse divergente (R3.6)
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Optional

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ERRO: pyyaml não instalado. Rode: pip install -r tools/requirements.txt", file=sys.stderr)
    raise

try:
    import networkx as nx
except ImportError:  # pragma: no cover
    nx = None


# ---------------------------------------------------------------------------
# Modelos de dados (design "Data Models")
# ---------------------------------------------------------------------------


class EstadoLicao(str, Enum):
    """Estados de conclusão de uma lição (R11.3). Default: NAO_INICIADA (R11.4)."""

    NAO_INICIADA = "nao_iniciada"
    EM_ANDAMENTO = "em_andamento"
    CONCLUIDA = "concluida"


@dataclass
class ExemploResolvido:
    codigo_python: str
    explicacoes_por_bloco: list[str]
    saida_esperada: str
    conceito_central: Optional[str] = None


@dataclass
class Exercicio:
    enunciado: str
    setup_inicial: str
    criterio_conclusao: str
    caminho_solucao: str
    caminho_saida_esperada: str
    eh_round_trip: bool = False


@dataclass
class Licao:
    id: str
    ordinal: int
    modulo: str
    titulo: str
    pre_requisitos: list[str] = field(default_factory=list)
    objetivos_de_aprendizagem: list[str] = field(default_factory=list)
    tempo_estimado_min: int = 0
    competencias: list[str] = field(default_factory=list)
    classificacao_ementa: str = ""
    conceitos_centrais: list[str] = field(default_factory=list)
    envolve_parsing_serializacao: bool = False
    exemplos_resolvidos: list[ExemploResolvido] = field(default_factory=list)
    exercicios: list[Exercicio] = field(default_factory=list)
    # metadados auxiliares para checagens textuais
    corpo: str = ""
    artefato: str = ""

    def texto_indexavel(self) -> str:
        """Concatena os campos textuais para checagem de cobertura de tópicos."""
        partes = [self.titulo, self.slug_modulo(), " ".join(self.objetivos_de_aprendizagem),
                  " ".join(self.conceitos_centrais), self.id]
        return _normalizar(" ".join(partes))

    def slug_modulo(self) -> str:
        return self.modulo or ""


@dataclass
class ResultadoAprendizagem:
    id: str
    descricao: str
    licao_id: str
    exigencias_mercado: list[str] = field(default_factory=list)


@dataclass
class ExigenciaMercado:
    id: str
    descricao: str
    categoria: str


@dataclass
class Modulo:
    id: str
    titulo: str
    temas_ementa: list[str] = field(default_factory=list)
    licoes: list[Licao] = field(default_factory=list)


@dataclass
class Violacao:
    """Não-conformidade detectada (design "Error Handling")."""

    codigo: str
    requisito: str
    artefato: str
    mensagem: str
    item_ausente: Optional[str] = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "codigo": self.codigo,
            "requisito": self.requisito,
            "artefato": self.artefato,
            "mensagem": self.mensagem,
            "item_ausente": self.item_ausente,
        }

    def __str__(self) -> str:
        base = f"[{self.codigo}] ({self.requisito}) {self.artefato}: {self.mensagem}"
        if self.item_ausente:
            base += f" | item: {self.item_ausente}"
        return base


# ---------------------------------------------------------------------------
# Utilidades de texto
# ---------------------------------------------------------------------------


def _normalizar(texto: str) -> str:
    """Normaliza para casamento de tópicos (minúsculas, acentos removidos)."""
    import unicodedata

    texto = texto.lower()
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return texto


def _extrair_front_matter(texto: str) -> tuple[Optional[str], str]:
    """Separa o front-matter YAML do corpo Markdown.

    O front-matter é o bloco YAML delimitado pelo primeiro par de linhas que
    contêm exatamente '---'. Antes dele toleramos apenas linhas em branco ou
    comentários HTML (incluindo comentários cujo texto interno contenha '-->').
    Retorna (yaml_bruto | None, corpo).
    """
    linhas = texto.splitlines(keepends=False)

    # O front-matter é delimitado pelo primeiro par de linhas que contêm
    # exatamente '---'. Comentários HTML iniciais (mesmo com '-->' embutido em
    # seu texto) nunca contêm uma linha isolada '---', então podemos localizar
    # os delimitadores diretamente.
    delimitadores = [idx for idx, ln in enumerate(linhas) if ln.strip() == "---"]
    if len(delimitadores) < 2:
        return None, texto
    inicio_yaml, fim_yaml = delimitadores[0], delimitadores[1]

    # Antes do primeiro delimitador só pode haver linhas em branco ou
    # comentários HTML (não conteúdo Markdown real).
    cabecalho = "\n".join(linhas[:inicio_yaml]).strip()
    if cabecalho and not (cabecalho.startswith("<!--")):
        return None, texto

    yaml_bruto = "\n".join(linhas[inicio_yaml + 1:fim_yaml])
    corpo = "\n".join(linhas[fim_yaml + 1:])
    return yaml_bruto, corpo


# ---------------------------------------------------------------------------
# 2.1 — Parser de front-matter e carregamento de lições
# ---------------------------------------------------------------------------

CAMPOS_OBRIGATORIOS = ["id", "ordinal", "modulo", "titulo"]


def parse_licao_de_texto(texto: str, artefato: str = "<memoria>") -> tuple[Optional[Licao], list[Violacao]]:
    """Parseia uma lição a partir do conteúdo Markdown completo.

    Front-matter inválido/ausente ou campos obrigatórios faltando viram
    violação METADADOS_INVALIDOS (R2.1). Em caso de erro retorna (None, [violações]).
    """
    violacoes: list[Violacao] = []
    yaml_bruto, corpo = _extrair_front_matter(texto)
    if yaml_bruto is None:
        violacoes.append(Violacao(
            "METADADOS_INVALIDOS", "R2.1", artefato,
            "front-matter YAML ausente ou não delimitado por '---'.",
        ))
        return None, violacoes
    try:
        meta = yaml.safe_load(yaml_bruto)
    except yaml.YAMLError as exc:
        violacoes.append(Violacao(
            "METADADOS_INVALIDOS", "R2.1", artefato,
            f"front-matter YAML inválido: {exc}",
        ))
        return None, violacoes
    if not isinstance(meta, dict):
        violacoes.append(Violacao(
            "METADADOS_INVALIDOS", "R2.1", artefato,
            "front-matter YAML não é um mapa de chaves/valores.",
        ))
        return None, violacoes

    faltando = [c for c in CAMPOS_OBRIGATORIOS if c not in meta or meta.get(c) in (None, "")]
    if faltando:
        violacoes.append(Violacao(
            "METADADOS_INVALIDOS", "R2.1", artefato,
            f"campos obrigatórios ausentes no front-matter: {', '.join(faltando)}.",
            item_ausente=", ".join(faltando),
        ))
        return None, violacoes

    try:
        ordinal = int(meta["ordinal"])
    except (ValueError, TypeError):
        violacoes.append(Violacao(
            "METADADOS_INVALIDOS", "R2.1", artefato,
            f"campo 'ordinal' não é inteiro: {meta.get('ordinal')!r}.",
            item_ausente="ordinal",
        ))
        return None, violacoes

    def _lista(chave: str) -> list[str]:
        valor = meta.get(chave) or []
        if isinstance(valor, str):
            return [valor]
        if isinstance(valor, list):
            return [str(v) for v in valor]
        return []

    exemplos, exercicios = _parsear_corpo(corpo)

    licao = Licao(
        id=str(meta["id"]),
        ordinal=ordinal,
        modulo=str(meta["modulo"]),
        titulo=str(meta["titulo"]),
        pre_requisitos=_lista("pre_requisitos"),
        objetivos_de_aprendizagem=_lista("objetivos_de_aprendizagem"),
        tempo_estimado_min=int(meta.get("tempo_estimado_min", 0) or 0),
        competencias=_lista("competencias"),
        classificacao_ementa=str(meta.get("classificacao_ementa", "")),
        conceitos_centrais=_lista("conceitos_centrais"),
        envolve_parsing_serializacao=bool(meta.get("envolve_parsing_serializacao", False)),
        exemplos_resolvidos=exemplos,
        exercicios=exercicios,
        corpo=corpo,
        artefato=artefato,
    )
    return licao, violacoes


# Estruturas auxiliares para parsear o corpo Markdown ------------------------

_RE_HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
_RE_CODE_BLOCK = re.compile(r"```(\w+)?[ \t]*\n(.*?)```", re.DOTALL)


def _fatiar_por_heading(corpo: str) -> list[tuple[int, str, int, int]]:
    """Retorna [(nivel, titulo, inicio_conteudo, fim_conteudo)] por heading.

    Ignora linhas que começam com '#' quando estão dentro de blocos de código
    cercados por ``` (evita confundir comentários Python com headings Markdown).
    O conteúdo de uma seção vai até o início da próxima linha de heading.
    """
    linhas = corpo.split("\n")
    offsets: list[int] = []
    pos = 0
    for ln in linhas:
        offsets.append(pos)
        pos += len(ln) + 1

    brutos: list[tuple[int, str, int, int]] = []  # (nivel, titulo, idx_linha, inicio_conteudo)
    em_fence = False
    for idx, ln in enumerate(linhas):
        if ln.lstrip().startswith("```"):
            em_fence = not em_fence
            continue
        if em_fence:
            continue
        m = _RE_HEADING.match(ln)
        if m:
            nivel = len(m.group(1))
            titulo = m.group(2)
            inicio_conteudo = offsets[idx] + len(ln) + 1
            brutos.append((nivel, titulo, idx, inicio_conteudo))

    secoes: list[tuple[int, str, int, int]] = []
    for k, (nivel, titulo, idx, ini) in enumerate(brutos):
        fim = offsets[brutos[k + 1][2]] if k + 1 < len(brutos) else len(corpo)
        secoes.append((nivel, titulo, ini, fim))
    return secoes


def _bloco_secao(secoes: list[tuple[int, str, int, int]], indice: int, corpo: str) -> str:
    """Conteúdo de uma seção H_n estendido até o próximo heading de nível <= n."""
    nivel, _titulo, ini, _fim = secoes[indice]
    fim = len(corpo)
    for j in range(indice + 1, len(secoes)):
        if secoes[j][0] <= nivel:
            fim = secoes[j][2]
            # recuar até o início da linha do heading seguinte
            fim = corpo.rfind("\n", 0, fim)
            if fim < 0:
                fim = len(corpo)
            break
    return corpo[ini:fim]


def _parsear_corpo(corpo: str) -> tuple[list[ExemploResolvido], list[Exercicio]]:
    """Extrai Exemplos_Resolvidos e Exercícios do corpo Markdown."""
    secoes = _fatiar_por_heading(corpo)
    exemplos: list[ExemploResolvido] = []
    exercicios: list[Exercicio] = []

    # Mapear cada Exemplo_Resolvido ao conceito central que o antecede.
    conceito_atual: Optional[str] = None
    for (nivel, titulo, ini, fim) in secoes:
        bloco = corpo[ini:fim]
        if nivel == 3 and titulo.lower().startswith("conceito central"):
            conceito_atual = titulo
        elif "exemplo_resolvido" in titulo.lower():
            codigos = [c for (lang, c) in _RE_CODE_BLOCK.findall(bloco)
                       if (lang or "").lower() in ("python", "py", "")]
            py = next((c for (lang, c) in _RE_CODE_BLOCK.findall(bloco)
                       if (lang or "").lower() in ("python", "py")), "")
            explicacoes = _extrair_bullets_apos(bloco, "explica")
            saida = _extrair_saida_esperada(bloco)
            exemplos.append(ExemploResolvido(
                codigo_python=py,
                explicacoes_por_bloco=explicacoes,
                saida_esperada=saida,
                conceito_central=conceito_atual,
            ))
        elif nivel == 3 and titulo.lower().startswith("exerc"):
            texto = titulo + "\n" + bloco
            exercicios.append(Exercicio(
                enunciado=titulo,
                setup_inicial=_capturar_campo(texto, ["entrada inicial", "setup", "passos de execu"]),
                criterio_conclusao=_capturar_campo(texto, ["critério de conclus", "criterio de conclus"]),
                caminho_solucao=_capturar_caminho(texto, ".py"),
                caminho_saida_esperada=_capturar_caminho(texto, ".saida.txt"),
                eh_round_trip=bool(re.search(r"ida-e-volta|round-?trip", texto, re.IGNORECASE)),
            ))
    return exemplos, exercicios


def _extrair_bullets_apos(bloco: str, marcador: str) -> list[str]:
    """Extrai itens de lista (bullets) que aparecem após um marcador textual."""
    idx = _normalizar(bloco).find(_normalizar(marcador))
    if idx < 0:
        return []
    trecho = bloco[idx:]
    bullets = re.findall(r"^[ \t]*[-*]\s+(.*\S)\s*$", trecho, re.MULTILINE)
    return bullets


def _extrair_saida_esperada(bloco: str) -> str:
    """Captura o conteúdo do bloco de código que segue 'Saída esperada'."""
    norm = _normalizar(bloco)
    idx = norm.find(_normalizar("saída esperada"))
    if idx < 0:
        idx = norm.find(_normalizar("saida esperada"))
    if idx < 0:
        return ""
    trecho = bloco[idx:]
    m = _RE_CODE_BLOCK.search(trecho)
    return m.group(2) if m else ""


def _capturar_campo(texto: str, marcadores: list[str]) -> str:
    norm = _normalizar(texto)
    for mk in marcadores:
        if _normalizar(mk) in norm:
            return mk
    return ""


def _capturar_caminho(texto: str, sufixo: str) -> str:
    candidatos = re.findall(r"`([^`]*?" + re.escape(sufixo) + r")`", texto)
    if not candidatos:
        candidatos = re.findall(r"(\S+" + re.escape(sufixo) + r")", texto)
    # Descarta um eventual prefixo de comando dentro do backtick (ex.:
    # "python trilha/.../solucao_1.py" -> "trilha/.../solucao_1.py").
    limpos = [c.strip().split()[-1] for c in candidatos if c.strip()]
    if not limpos:
        return ""
    # Prefere o caminho da solução de referência (em solucoes/) sobre qualquer
    # outro caminho .py citado nos passos (ex.: o comando de execução da prática).
    for c in limpos:
        if "solucoes/" in c:
            return c
    return limpos[0]


def carregar_licoes(trilha_dir: Path) -> tuple[list[Licao], list[Violacao]]:
    """Carrega todas as lições de `trilha_dir/modulos/**/NNN-*.md`.

    Retorna (licoes_validas, violacoes_de_metadados). Front-matter inválido
    em qualquer arquivo vira violação METADADOS_INVALIDOS (não aborta).
    """
    trilha_dir = Path(trilha_dir)
    modulos_dir = trilha_dir / "modulos"
    licoes: list[Licao] = []
    violacoes: list[Violacao] = []
    if not modulos_dir.exists():
        return licoes, violacoes
    arquivos = sorted(modulos_dir.glob("**/*.md"))
    for arq in arquivos:
        # Apenas arquivos de lição: prefixo numérico NNN-...
        if not re.match(r"^\d{3}-", arq.name):
            continue
        texto = arq.read_text(encoding="utf-8")
        rel = str(arq.relative_to(trilha_dir))
        licao, vs = parse_licao_de_texto(texto, rel)
        violacoes.extend(vs)
        if licao is not None:
            licoes.append(licao)
    return licoes, violacoes


# ---------------------------------------------------------------------------
# 2.2 — Checagens de DAG e ordenação (R5)
# ---------------------------------------------------------------------------


def construir_dag(licoes: list[Licao]) -> dict[str, list[str]]:
    """Constrói o grafo de pré-requisitos: id -> lista de ids de pré-requisitos."""
    return {licao.id: list(licao.pre_requisitos) for licao in licoes}


def checar_aciclicidade(dag: dict[str, list[str]]) -> list[list[str]]:
    """Detecta ciclos no grafo de pré-requisitos. Retorna a lista de ciclos."""
    ciclos: list[list[str]] = []
    if nx is not None:
        g = nx.DiGraph()
        for no, prereqs in dag.items():
            g.add_node(no)
            for p in prereqs:
                if p in dag:  # ignora refs pendentes aqui (tratadas em outra checagem)
                    g.add_edge(no, p)
        try:
            for ciclo in nx.simple_cycles(g):
                ciclos.append(ciclo)
        except Exception:
            pass
        return ciclos
    # Fallback sem networkx: DFS de detecção de ciclo.
    BRANCO, CINZA, PRETO = 0, 1, 2
    cor = {n: BRANCO for n in dag}
    pilha: list[str] = []

    def visitar(n: str) -> None:
        cor[n] = CINZA
        pilha.append(n)
        for p in dag.get(n, []):
            if p not in dag:
                continue
            if cor[p] == CINZA:
                inicio = pilha.index(p)
                ciclos.append(pilha[inicio:].copy())
            elif cor[p] == BRANCO:
                visitar(p)
        pilha.pop()
        cor[n] = PRETO

    for n in dag:
        if cor[n] == BRANCO:
            visitar(n)
    return ciclos


def checar_ordem_topologica(licoes: list[Licao]) -> list[Violacao]:
    """Verifica refs apenas para trás (R5.1, R5.2) e refs pendentes (R5.5)."""
    violacoes: list[Violacao] = []
    por_id = {licao.id: licao for licao in licoes}
    for licao in licoes:
        for prereq in licao.pre_requisitos:
            alvo = por_id.get(prereq)
            if alvo is None:
                violacoes.append(Violacao(
                    "REF_PENDENTE", "R5.5", licao.artefato or licao.id,
                    f"pré-requisito '{prereq}' da lição '{licao.id}' não corresponde a nenhuma lição existente.",
                    item_ausente=prereq,
                ))
            elif alvo.ordinal >= licao.ordinal:
                violacoes.append(Violacao(
                    "ARESTA_FRENTE", "R5.1", licao.artefato or licao.id,
                    f"pré-requisito '{prereq}' (ordinal {alvo.ordinal}) não é anterior à lição "
                    f"'{licao.id}' (ordinal {licao.ordinal}).",
                    item_ausente=prereq,
                ))
    return violacoes


def checar_ordinais_contiguos(licoes: list[Licao]) -> list[Violacao]:
    """Verifica que os ordinais formam {1..N} sem lacuna nem repetição (R5.4)."""
    violacoes: list[Violacao] = []
    if not licoes:
        return violacoes
    ordinais = [licao.ordinal for licao in licoes]
    n = len(ordinais)
    esperado = set(range(1, n + 1))
    obtido = set(ordinais)

    # Repetições
    vistos: dict[int, list[str]] = {}
    for licao in licoes:
        vistos.setdefault(licao.ordinal, []).append(licao.id)
    for ordv, ids in sorted(vistos.items()):
        if len(ids) > 1:
            violacoes.append(Violacao(
                "ORDINAL_NAO_CONTIGUO", "R5.4", "trilha",
                f"ordinal {ordv} repetido nas lições: {', '.join(ids)}.",
                item_ausente=str(ordv),
            ))

    if obtido != esperado:
        faltando = sorted(esperado - obtido)
        extras = sorted(obtido - esperado)
        msg = []
        if faltando:
            msg.append(f"ordinais ausentes (lacuna): {faltando}")
        if extras:
            msg.append(f"ordinais fora de 1..{n}: {extras}")
        if msg:
            violacoes.append(Violacao(
                "ORDINAL_NAO_CONTIGUO", "R5.4", "trilha",
                "; ".join(msg) + f" (esperado o conjunto contíguo 1..{n}).",
                item_ausente=str(faltando[0]) if faltando else (str(extras[0]) if extras else None),
            ))
    return violacoes


def checar_primeira_licao_sem_prereq(licoes: list[Licao]) -> list[Violacao]:
    """A lição de ordinal 1 deve existir e não ter pré-requisitos (R5.3)."""
    violacoes: list[Violacao] = []
    if not licoes:
        return violacoes
    primeira = min(licoes, key=lambda l: l.ordinal)
    if primeira.ordinal == 1 and primeira.pre_requisitos:
        violacoes.append(Violacao(
            "ARESTA_FRENTE", "R5.3", primeira.artefato or primeira.id,
            f"a primeira lição (ordinal 1, '{primeira.id}') deve representar o fundamento absoluto "
            f"e não ter pré-requisitos, mas declara: {primeira.pre_requisitos}.",
        ))
    return violacoes


def checar_dag_completo(licoes: list[Licao]) -> list[Violacao]:
    """Executa todas as checagens de grafo/ordenação (Property 1)."""
    violacoes: list[Violacao] = []
    dag = construir_dag(licoes)
    for ciclo in checar_aciclicidade(dag):
        violacoes.append(Violacao(
            "CICLO", "R5.6", "trilha",
            f"dependência circular detectada entre lições: {' -> '.join(ciclo)} -> {ciclo[0]}.",
            item_ausente=", ".join(ciclo),
        ))
    violacoes.extend(checar_ordem_topologica(licoes))
    violacoes.extend(checar_ordinais_contiguos(licoes))
    violacoes.extend(checar_primeira_licao_sem_prereq(licoes))
    return violacoes


def ordenacao_valida(licoes: list[Licao]) -> bool:
    """True sse a trilha possui uma ordem de estudo válida (Property 1)."""
    return len(checar_dag_completo(licoes)) == 0


# ---------------------------------------------------------------------------
# 2.4 — Conformidade de template (R1.10, R1.12, R2, R3, R4, R12)
# ---------------------------------------------------------------------------


def _violacao_template(licao: Licao, subcodigo: str, requisito: str, mensagem: str) -> Violacao:
    return Violacao(
        "TEMPLATE_NAO_CONFORME", requisito, licao.artefato or licao.id,
        f"[{subcodigo}] {mensagem}",
        item_ausente=subcodigo,
    )


def checar_conformidade_template(licao: Licao) -> list[Violacao]:
    """Verifica todas as regras estruturais do template (Property 2)."""
    violacoes: list[Violacao] = []
    corpo = licao.corpo
    secoes = _fatiar_por_heading(corpo)

    # --- Objetivos de aprendizagem: 1..5 (R2.6) ---
    n_obj = len(licao.objetivos_de_aprendizagem)
    if n_obj < 1 or n_obj > 5:
        violacoes.append(_violacao_template(
            licao, "OBJETIVOS_FORA_INTERVALO", "R2.6",
            f"a lição deve ter de 1 a 5 objetivos de aprendizagem (tem {n_obj}).",
        ))

    # --- Tempo estimado <= 60 (R2.3) ---
    if licao.tempo_estimado_min > 60:
        violacoes.append(_violacao_template(
            licao, "TEMPO_EXCEDE", "R2.3",
            f"tempo_estimado_min deve ser <= 60 (tem {licao.tempo_estimado_min}).",
        ))

    # --- Seções: exatamente uma Seção_Teórica seguida de uma Seção_Prática (R2.2, R3.1) ---
    indices_h2 = [i for i, (nivel, _t, _ini, _fim) in enumerate(secoes) if nivel == 2]
    idx_teorica = [i for i in indices_h2
                   if "secao_teorica" in _normalizar(secoes[i][1])]
    idx_pratica = [i for i in indices_h2
                   if "secao_pratica" in _normalizar(secoes[i][1])]

    if len(idx_teorica) != 1:
        violacoes.append(_violacao_template(
            licao, "UMA_SECAO_TEORICA", "R2.2",
            f"deve haver exatamente uma Seção_Teórica (encontradas {len(idx_teorica)}).",
        ))
    if len(idx_pratica) != 1:
        violacoes.append(_violacao_template(
            licao, "UMA_SECAO_PRATICA", "R3.1",
            f"deve haver exatamente uma Seção_Prática (encontradas {len(idx_pratica)}).",
        ))
    if len(idx_teorica) == 1 and len(idx_pratica) == 1:
        if idx_teorica[0] > idx_pratica[0]:
            violacoes.append(_violacao_template(
                licao, "ORDEM_SECOES", "R2.2",
                "a Seção_Teórica deve preceder integralmente a Seção_Prática.",
            ))
        # Seção_Prática deve ser a última seção H2 (R3.1)
        if idx_pratica[0] != indices_h2[-1]:
            violacoes.append(_violacao_template(
                licao, "PRATICA_NAO_FINAL", "R3.1",
                "a Seção_Prática deve ser a última seção da lição.",
            ))

    # --- Conteúdo da Seção_Teórica ---
    if len(idx_teorica) == 1:
        teorica = _bloco_secao(secoes, idx_teorica[0], corpo)
        norm_t = _normalizar(teorica)
        if "motivacao" not in norm_t:
            violacoes.append(_violacao_template(
                licao, "MOTIVACAO_AUSENTE", "R1.10",
                "a Seção_Teórica deve conter a subseção 'Motivação'.",
            ))
        if "principio de funcionamento" not in norm_t:
            violacoes.append(_violacao_template(
                licao, "PRINCIPIO_AUSENTE", "R1.10",
                "a Seção_Teórica deve conter a subseção 'Princípio de funcionamento'.",
            ))

    # --- Exemplos_Resolvidos (R12.1, R12.2, R12.3, R12.5) ---
    exemplos = licao.exemplos_resolvidos
    if len(exemplos) < 3:
        violacoes.append(_violacao_template(
            licao, "EXEMPLOS_INSUFICIENTES", "R12.1",
            f"a Seção_Teórica deve ter >= 3 Exemplos_Resolvidos (tem {len(exemplos)}).",
        ))
    for i, ex in enumerate(exemplos, 1):
        if not ex.codigo_python.strip():
            violacoes.append(_violacao_template(
                licao, "EXEMPLO_SEM_CODIGO", "R12.2",
                f"Exemplo_Resolvido #{i} não tem bloco de código Python.",
            ))
        if not ex.explicacoes_por_bloco:
            violacoes.append(_violacao_template(
                licao, "EXEMPLO_SEM_EXPLICACAO", "R12.2",
                f"Exemplo_Resolvido #{i} não tem explicação por bloco lógico.",
            ))
        if not ex.saida_esperada.strip():
            violacoes.append(_violacao_template(
                licao, "EXEMPLO_SEM_SAIDA", "R12.3",
                f"Exemplo_Resolvido #{i} não exibe a saída esperada.",
            ))

    # --- >= 1 Exemplo_Resolvido por conceito central (R12.1) ---
    if licao.conceitos_centrais:
        conceitos_com_exemplo = {ex.conceito_central for ex in exemplos if ex.conceito_central}
        headings_conceito = [t for (nivel, t, _, _) in secoes
                             if nivel == 3 and t.lower().startswith("conceito central")]
        if len(headings_conceito) < len(licao.conceitos_centrais):
            violacoes.append(_violacao_template(
                licao, "CONCEITO_SEM_EXEMPLO", "R12.1",
                f"há {len(licao.conceitos_centrais)} conceitos centrais declarados, mas apenas "
                f"{len(headings_conceito)} seções 'Conceito central' no corpo.",
            ))
        for h in headings_conceito:
            if h not in conceitos_com_exemplo:
                violacoes.append(_violacao_template(
                    licao, "CONCEITO_SEM_EXEMPLO", "R12.1",
                    f"o conceito central '{h}' não possui ao menos um Exemplo_Resolvido.",
                ))

    # --- Exercícios da Seção_Prática (R3.2, R3.3, R3.4, R3.5, R4.1) ---
    exercicios = licao.exercicios
    if len(exercicios) < 3:
        violacoes.append(_violacao_template(
            licao, "EXERCICIOS_INSUFICIENTES", "R4.1",
            f"a Seção_Prática deve ter >= 3 exercícios em Python (tem {len(exercicios)}).",
        ))
    for i, ex in enumerate(exercicios, 1):
        if not ex.criterio_conclusao:
            violacoes.append(_violacao_template(
                licao, "EXERCICIO_SEM_CRITERIO", "R3.3",
                f"Exercício #{i} não declara critério de conclusão binário.",
            ))
        if not ex.caminho_solucao:
            violacoes.append(_violacao_template(
                licao, "EXERCICIO_SEM_SOLUCAO", "R3.4",
                f"Exercício #{i} não referencia a solução de referência (.py).",
            ))
        if not ex.caminho_saida_esperada:
            violacoes.append(_violacao_template(
                licao, "EXERCICIO_SEM_SAIDA", "R3.4",
                f"Exercício #{i} não referencia a saída esperada (.saida.txt).",
            ))
        if not ex.setup_inicial:
            violacoes.append(_violacao_template(
                licao, "EXERCICIO_SEM_SETUP", "R3.5",
                f"Exercício #{i} não especifica entradas iniciais/passos de execução.",
            ))

    # --- JavaScript não marcado no conteúdo principal (R4.3, R4.4) ---
    violacoes.extend(_checar_javascript_nao_marcado(licao))

    return violacoes


_RE_JS_BLOCK = re.compile(r"```(javascript|js|jsx|typescript|ts)\b", re.IGNORECASE)
_MARCADOR_JS = "complemento opcional"


def _checar_javascript_nao_marcado(licao: Licao) -> list[Violacao]:
    """Detecta blocos JavaScript sem o marcador de complemento opcional (R4.4)."""
    violacoes: list[Violacao] = []
    corpo = licao.corpo
    norm = _normalizar(corpo)
    for m in _RE_JS_BLOCK.finditer(corpo):
        # Procura o marcador "complemento opcional" antes do bloco JS.
        prefixo = _normalizar(corpo[:m.start()])
        if _MARCADOR_JS not in prefixo:
            violacoes.append(_violacao_template(
                licao, "JS_NAO_MARCADO", "R4.4",
                "há bloco JavaScript no conteúdo principal sem o marcador "
                "'Complemento opcional (JavaScript)' que o anteceda.",
            ))
            break
    return violacoes


def template_conforme(licao: Licao) -> bool:
    """True sse a lição satisfaz todas as regras do template (Property 2)."""
    return len(checar_conformidade_template(licao)) == 0


# ---------------------------------------------------------------------------
# 2.6 — Round-trip de parsing/serialização (R3.6, Property 3)
# ---------------------------------------------------------------------------


def round_trip_igual(estrutura: Any,
                     serializar: Callable[[Any], str],
                     parsear: Callable[[str], Any]) -> bool:
    """Property 3: parse -> serialize -> parse == parse (igualdade exata).

    `estrutura` é a estrutura de entrada; aplica serialização e parsing
    duas vezes e confirma que o resultado do 2º parse iguala o do 1º.
    """
    primeiro = parsear(serializar(estrutura))
    segundo = parsear(serializar(primeiro))
    return primeiro == segundo


# Serializadores/parsers de referência usados nos exercícios e testes -------


def serializar_json(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True)


def parsear_json(texto: str) -> Any:
    return json.loads(texto)


def tokenizar(texto: str) -> list[str]:
    """Tokenizador de referência reversível: separa palavras e espaços
    preservando a sequência exata (round-trip exato via destokenizar)."""
    return re.findall(r"\s+|\S+", texto)


def destokenizar(tokens: list[str]) -> str:
    return "".join(tokens)


def validar_round_trip(licao: Licao) -> list[Violacao]:
    """Para lições com envolve_parsing_serializacao=true, exige um exercício
    de ida-e-volta com igualdade exata (R3.6)."""
    violacoes: list[Violacao] = []
    if not licao.envolve_parsing_serializacao:
        return violacoes
    tem_round_trip = any(ex.eh_round_trip for ex in licao.exercicios)
    if not tem_round_trip:
        violacoes.append(Violacao(
            "ROUNDTRIP_DIVERGENTE", "R3.6", licao.artefato or licao.id,
            "a lição marca envolve_parsing_serializacao=true mas não possui exercício "
            "de ida-e-volta (parse -> serialize -> parse) com igualdade exata.",
        ))
    return violacoes


# ---------------------------------------------------------------------------
# 2.8 — Cobertura de tópicos obrigatórios e mapa de competências (R1/R6/R7/R8)
# ---------------------------------------------------------------------------

# Cada item: (id, requisito, [termos sinônimos]). A cobertura é satisfeita se
# QUALQUER lição contém QUALQUER um dos termos no seu texto indexável.
TOPICOS_OBRIGATORIOS: list[tuple[str, str, list[str]]] = [
    # R1.1 — fundamentos matemáticos
    ("algebra-linear", "R1.1", ["algebra linear", "vetor", "matriz"]),
    ("calculo", "R1.1", ["derivada", "gradiente", "calculo"]),
    ("probabilidade-estatistica", "R1.1", ["probabilidade", "estatistica"]),
    # R1.2 / R6.1 — fundamentos de ML
    ("gradient-descent", "R1.2", ["gradient descent", "descida do gradiente"]),
    ("backpropagation", "R1.2", ["backpropagation", "retropropagacao"]),
    ("funcoes-de-perda", "R1.2", ["funcao de perda", "funcoes de perda", "loss", "cross-entropy", "mse"]),
    ("regularizacao", "R1.2", ["regularizacao", "dropout", "early stopping"]),
    ("vies-variancia", "R1.2", ["vies-variancia", "vies variancia", "bias-variance"]),
    ("overfitting", "R1.2", ["overfitting", "underfitting", "validacao cruzada"]),
    ("calibracao", "R1.2", ["calibracao"]),
    ("desbalanceamento", "R1.2", ["desbalanceamento", "classes desbalanceadas"]),
    ("data-leakage", "R1.2", ["data leakage", "vazamento de dados"]),
    ("experimentacao-ab", "R1.2", ["teste a/b", "testes a-b", "experimentacao", "teste a-b"]),
    # R1.3 — redes neurais / deep learning
    ("perceptron", "R1.3", ["perceptron"]),
    ("deep-learning", "R1.3", ["deep learning", "rede neural", "redes profundas", "mlp"]),
    # R1.4 / R6.4 — NLP e busca vetorial
    ("tokenizacao", "R1.4", ["tokenizacao", "tokenizer", "bpe", "wordpiece", "sentencepiece"]),
    ("embeddings", "R1.4", ["embedding", "word2vec", "glove"]),
    ("metricas-distancia", "R1.4", ["metrica de distancia", "metricas de distancia", "cosseno", "distancia"]),
    ("ann", "R1.4", ["busca aproximada", "ann", "approximate nearest"]),
    ("hnsw", "R1.4", ["hnsw"]),
    # R1.5 / R6.2 — transformers
    ("self-attention", "R1.5", ["self-attention", "self attention", "query/key/value", "q/k/v"]),
    ("positional-encoding", "R1.5", ["positional encoding", "codificacao posicional"]),
    ("multi-head", "R1.5", ["multi-head", "multi head", "multihead"]),
    # R1.6 / R6.5 — pipeline LLM
    ("pre-treinamento", "R1.6", ["pre-treinamento", "pre treinamento", "pretraining"]),
    ("sft", "R1.6", ["instruction tuning", "sft", "fine-tuning supervisionado"]),
    ("dpo-ppo", "R1.6", ["dpo", "ppo", "rlhf", "otimizacao por preferencia"]),
    # R1.7 — GenAI
    ("llms", "R1.7", ["llm", "modelo de linguagem"]),
    ("sampling", "R1.7", ["sampling", "temperature", "top-p", "top p"]),
    ("rag", "R1.7", ["rag", "retrieval augmented", "retrieval-augmented"]),
    ("agentes", "R1.7", ["agente", "react", "tool use", "function calling"]),
    ("fine-tuning", "R1.7", ["fine-tuning", "fine tuning", "lora", "peft"]),
    ("multimodal", "R1.7", ["multimodal", "multimodais"]),
    # R1.8 — arquitetura / segurança / mlops
    ("arquitetura-sistemas", "R1.8", ["arquitetura de sistemas", "ai-first", "design ai"]),
    ("seguranca-governanca", "R1.8", ["seguranca", "governanca", "prompt injection", "ia responsavel"]),
    ("mlops-llmops", "R1.8", ["mlops", "llmops", "observabilidade"]),
    # R1.9 / R6.6 — custo/latencia/evals
    ("custo-inferencia", "R1.9", ["custo de inferencia", "custo inferencia"]),
    ("latencia-inferencia", "R1.9", ["latencia de inferencia", "latencia inferencia"]),
    ("evals", "R1.9", ["evals", "avaliacao de sistemas llm", "metodologia de avaliacao"]),
]


def checar_cobertura_topicos(licoes: list[Licao]) -> list[Violacao]:
    """Verifica que cada tópico obrigatório é coberto por >= 1 lição (R1/R6/R7)."""
    violacoes: list[Violacao] = []
    textos = [licao.texto_indexavel() for licao in licoes]
    blob = " || ".join(textos)
    for (tid, requisito, termos) in TOPICOS_OBRIGATORIOS:
        termos_norm = [_normalizar(t) for t in termos]
        if not any(t in blob for t in termos_norm):
            violacoes.append(Violacao(
                "TOPICO_AUSENTE", requisito, "trilha",
                f"nenhuma lição cobre o tópico obrigatório '{tid}' "
                f"(termos esperados: {', '.join(termos)}).",
                item_ausente=tid,
            ))
    return violacoes


def carregar_competencias(caminho: Path) -> tuple[list[ExigenciaMercado], list[ResultadoAprendizagem], list[Violacao]]:
    """Carrega competencias.yaml (exigências + resultados de aprendizagem)."""
    violacoes: list[Violacao] = []
    caminho = Path(caminho)
    if not caminho.exists():
        violacoes.append(Violacao(
            "METADADOS_INVALIDOS", "R8.1", str(caminho),
            "arquivo competencias.yaml não encontrado.",
        ))
        return [], [], violacoes
    try:
        dados = yaml.safe_load(caminho.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as exc:
        violacoes.append(Violacao(
            "METADADOS_INVALIDOS", "R8.1", str(caminho),
            f"competencias.yaml inválido: {exc}",
        ))
        return [], [], violacoes

    exigencias = [
        ExigenciaMercado(id=str(e["id"]), descricao=str(e.get("descricao", "")),
                         categoria=str(e.get("categoria", "")))
        for e in (dados.get("exigencias_mercado") or [])
        if isinstance(e, dict) and e.get("id")
    ]
    resultados = [
        ResultadoAprendizagem(
            id=str(r["id"]), descricao=str(r.get("descricao", "")),
            licao_id=str(r.get("licao", "")),
            exigencias_mercado=[str(x) for x in (r.get("exigencias") or [])],
        )
        for r in (dados.get("resultados_de_aprendizagem") or [])
        if isinstance(r, dict) and r.get("id")
    ]
    return exigencias, resultados, violacoes


def checar_mapa_competencias(licoes: list[Licao],
                             exigencias: list[ExigenciaMercado],
                             resultados: list[ResultadoAprendizagem]) -> list[Violacao]:
    """Verifica o mapa de competências (R8): sem órfãos, cobertura das exigências."""
    violacoes: list[Violacao] = []
    ids_licoes = {l.id for l in licoes}
    exigencias_atendidas: set[str] = set()
    ids_exigencias = {e.id for e in exigencias}

    # Outcomes órfãos: sem exigência, ou apontando para lição inexistente (R8.6).
    for r in resultados:
        if not r.exigencias_mercado:
            violacoes.append(Violacao(
                "OUTCOME_ORFAO", "R8.6", "competencias.yaml",
                f"resultado de aprendizagem '{r.id}' não está mapeado a nenhuma exigência.",
                item_ausente=r.id,
            ))
        else:
            for ex_id in r.exigencias_mercado:
                if ex_id in ids_exigencias:
                    exigencias_atendidas.add(ex_id)
                else:
                    violacoes.append(Violacao(
                        "OUTCOME_ORFAO", "R8.6", "competencias.yaml",
                        f"resultado '{r.id}' referencia exigência inexistente '{ex_id}'.",
                        item_ausente=ex_id,
                    ))
        if r.licao_id and ids_licoes and r.licao_id not in ids_licoes:
            violacoes.append(Violacao(
                "OUTCOME_ORFAO", "R8.6", "competencias.yaml",
                f"resultado '{r.id}' referencia lição inexistente '{r.licao_id}'.",
                item_ausente=r.licao_id,
            ))

    # Exigências sem lição/resultado correspondente (R8.5, R8.2, R8.3).
    for e in exigencias:
        if e.id not in exigencias_atendidas:
            violacoes.append(Violacao(
                "EXIGENCIA_SEM_LICAO", "R8.5", "competencias.yaml",
                f"a exigência '{e.id}' ({e.descricao}) não é entregue por nenhum "
                f"resultado de aprendizagem.",
                item_ausente=e.id,
            ))
    return violacoes


# ---------------------------------------------------------------------------
# 2.10 — Progresso e ponto de retomada (R11)
# ---------------------------------------------------------------------------


def ler_progresso(caminho: Path) -> dict[str, EstadoLicao]:
    """Lê progresso.yaml -> {ordinal_3dig: EstadoLicao}. Ausência => não iniciada."""
    caminho = Path(caminho)
    if not caminho.exists():
        return {}
    dados = yaml.safe_load(caminho.read_text(encoding="utf-8")) or {}
    licoes = dados.get("licoes") or {}
    progresso: dict[str, EstadoLicao] = {}
    if isinstance(licoes, dict):
        for chave, valor in licoes.items():
            try:
                progresso[str(chave)] = EstadoLicao(str(valor))
            except ValueError:
                # estado inválido é ignorado (tratado como não iniciada)
                continue
    return progresso


def _ordinal_chave(ordinal: int) -> str:
    return f"{ordinal:03d}"


def estado_da_licao(ordinal: int, progresso: dict[str, EstadoLicao]) -> EstadoLicao:
    """Estado de uma lição; ausência de registro => NAO_INICIADA (R11.4)."""
    return progresso.get(_ordinal_chave(ordinal), EstadoLicao.NAO_INICIADA)


def calcular_ponto_de_retomada(licoes: list[Licao],
                               progresso: dict[str, EstadoLicao]) -> Optional[Licao]:
    """Ponto de retomada (R11.6): menor ordinal em_andamento; senão menor
    nao_iniciada; senão None (trilha completa)."""
    ordenadas = sorted(licoes, key=lambda l: l.ordinal)
    for licao in ordenadas:
        if estado_da_licao(licao.ordinal, progresso) == EstadoLicao.EM_ANDAMENTO:
            return licao
    for licao in ordenadas:
        if estado_da_licao(licao.ordinal, progresso) == EstadoLicao.NAO_INICIADA:
            return licao
    return None


# ---------------------------------------------------------------------------
# 2.12 — Runner de execução de exemplos e soluções (R4.5, R4.6, R12.4)
# ---------------------------------------------------------------------------


def executar_codigo_python(codigo: str, timeout: float = 30.0) -> tuple[bool, str, str]:
    """Executa código Python em subprocesso isolado. Retorna (ok, stdout, erro)."""
    try:
        proc = subprocess.run(
            [sys.executable, "-c", codigo],
            capture_output=True, text=True, timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return False, "", f"timeout após {timeout}s"
    if proc.returncode != 0:
        return False, proc.stdout, proc.stderr.strip() or f"exit code {proc.returncode}"
    return True, proc.stdout, ""


def _normalizar_saida(s: str) -> str:
    return s.replace("\r\n", "\n").rstrip("\n")


def executar_exemplo(exemplo: ExemploResolvido, artefato: str = "<exemplo>",
                     timeout: float = 30.0) -> list[Violacao]:
    """Executa um Exemplo_Resolvido e compara stdout com a saída esperada."""
    violacoes: list[Violacao] = []
    if not exemplo.codigo_python.strip():
        return violacoes
    ok, stdout, erro = executar_codigo_python(exemplo.codigo_python, timeout)
    if not ok:
        violacoes.append(Violacao(
            "EXEMPLO_FALHOU", "R4.6", artefato,
            f"o Exemplo_Resolvido não executou sem erros: {erro}",
        ))
        return violacoes
    if _normalizar_saida(stdout) != _normalizar_saida(exemplo.saida_esperada):
        violacoes.append(Violacao(
            "EXEMPLO_FALHOU", "R12.4", artefato,
            "a saída do Exemplo_Resolvido diverge da saída esperada.\n"
            f"  esperado: {_normalizar_saida(exemplo.saida_esperada)!r}\n"
            f"  obtido:   {_normalizar_saida(stdout)!r}",
        ))
    return violacoes


def executar_solucao(caminho_solucao: Path, caminho_saida: Path,
                     timeout: float = 30.0) -> list[Violacao]:
    """Executa uma solução de referência .py e compara com a .saida.txt."""
    violacoes: list[Violacao] = []
    # Resolve para caminhos absolutos: assim a execução independe de o
    # --trilha ter sido passado como caminho relativo (cwd=parent + arg
    # relativo duplicaria o caminho e quebraria a abertura do arquivo).
    caminho_solucao = Path(caminho_solucao).resolve()
    caminho_saida = Path(caminho_saida).resolve()
    if not caminho_solucao.exists():
        violacoes.append(Violacao(
            "EXEMPLO_FALHOU", "R4.6", str(caminho_solucao),
            "arquivo de solução de referência não encontrado.",
        ))
        return violacoes
    try:
        proc = subprocess.run(
            [sys.executable, str(caminho_solucao)],
            capture_output=True, text=True, timeout=timeout,
            cwd=str(caminho_solucao.parent),
        )
    except subprocess.TimeoutExpired:
        violacoes.append(Violacao(
            "EXEMPLO_FALHOU", "R4.6", str(caminho_solucao),
            f"timeout após {timeout}s.",
        ))
        return violacoes
    if proc.returncode != 0:
        violacoes.append(Violacao(
            "EXEMPLO_FALHOU", "R4.6", str(caminho_solucao),
            f"a solução não executou sem erros: {proc.stderr.strip()}",
        ))
        return violacoes
    if caminho_saida.exists():
        esperado = caminho_saida.read_text(encoding="utf-8")
        if _normalizar_saida(proc.stdout) != _normalizar_saida(esperado):
            violacoes.append(Violacao(
                "EXEMPLO_FALHOU", "R12.4", str(caminho_solucao),
                "a saída da solução diverge do arquivo .saida.txt.",
            ))
    return violacoes


# ---------------------------------------------------------------------------
# 2.14 — CLI e relatório de violações (coleta exaustiva, não fail-fast)
# ---------------------------------------------------------------------------


def validar_trilha(trilha_dir: Path, executar_exemplos: bool = False) -> list[Violacao]:
    """Executa TODAS as checagens e acumula todas as violações (não fail-fast)."""
    trilha_dir = Path(trilha_dir)
    violacoes: list[Violacao] = []

    licoes, vs_meta = carregar_licoes(trilha_dir)
    violacoes.extend(vs_meta)

    # Property 1 — DAG/ordenação
    violacoes.extend(checar_dag_completo(licoes))

    # Property 2 — conformidade de template
    for licao in licoes:
        violacoes.extend(checar_conformidade_template(licao))

    # Property 3 — round-trip
    for licao in licoes:
        violacoes.extend(validar_round_trip(licao))

    # Property 4 — cobertura de tópicos e mapa de competências
    violacoes.extend(checar_cobertura_topicos(licoes))
    exigencias, resultados, vs_comp = carregar_competencias(trilha_dir / "competencias.yaml")
    violacoes.extend(vs_comp)
    violacoes.extend(checar_mapa_competencias(licoes, exigencias, resultados))

    # Property 6 — execução de exemplos/soluções (opcional; custoso)
    if executar_exemplos:
        for licao in licoes:
            for ex in licao.exemplos_resolvidos:
                violacoes.extend(executar_exemplo(ex, licao.artefato or licao.id))
            for exr in licao.exercicios:
                if exr.caminho_solucao:
                    sol = trilha_dir / exr.caminho_solucao.replace("trilha/", "", 1)
                    saida = trilha_dir / exr.caminho_saida_esperada.replace("trilha/", "", 1)
                    violacoes.extend(executar_solucao(sol, saida))

    return violacoes


def gerar_relatorio_texto(violacoes: list[Violacao], n_licoes: int) -> str:
    if not violacoes:
        return f"✓ Trilha conforme: {n_licoes} lição(ões) verificada(s), nenhuma não-conformidade."
    linhas = [f"✗ {len(violacoes)} não-conformidade(s) detectada(s):", ""]
    por_codigo: dict[str, int] = {}
    for v in violacoes:
        por_codigo[v.codigo] = por_codigo.get(v.codigo, 0) + 1
        linhas.append(f"  {v}")
    linhas.append("")
    resumo = ", ".join(f"{c}={n}" for c, n in sorted(por_codigo.items()))
    linhas.append(f"Resumo: {resumo}")
    return "\n".join(linhas)


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Valida as propriedades de correção da Trilha de Engenharia de IA Aplicada.")
    parser.add_argument("--trilha", default="trilha", type=Path,
                        help="diretório raiz da Trilha (default: trilha/).")
    parser.add_argument("--json", action="store_true",
                        help="emite o relatório em JSON.")
    parser.add_argument("--executar-exemplos", action="store_true",
                        help="executa os Exemplos_Resolvidos e soluções (Property 6).")
    args = parser.parse_args(argv)

    licoes, _ = carregar_licoes(args.trilha)
    violacoes = validar_trilha(args.trilha, executar_exemplos=args.executar_exemplos)

    if args.json:
        saida = {
            "conforme": len(violacoes) == 0,
            "n_licoes": len(licoes),
            "n_violacoes": len(violacoes),
            "violacoes": [v.to_dict() for v in violacoes],
        }
        print(json.dumps(saida, ensure_ascii=False, indent=2))
    else:
        print(gerar_relatorio_texto(violacoes, len(licoes)))

    return 0 if not violacoes else 1


if __name__ == "__main__":
    raise SystemExit(main())
