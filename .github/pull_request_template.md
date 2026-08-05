<!-- Obrigado por contribuir. Preencha o que se aplica e apague o resto. -->

## O que muda

<!-- Uma ou duas frases. Se corrige uma lição, cite o <NNN>-<slug>. -->

## Por quê

<!-- O problema que isso resolve. Se há issue, referencie: Closes #123 -->

## Tipo de mudança

- [ ] Correção de conteúdo (teoria, exemplo, exercício ou solução)
- [ ] Lição nova ou reestruturação do currículo
- [ ] Tooling (validador, índice, progresso, capstone)
- [ ] Documentação / README / branding
- [ ] CI ou infraestrutura do repositório

## Verificação

Rode os quatro comandos do CI localmente e marque o que passou:

- [ ] `python3 trilha/tools/validar_trilha.py` — sem não-conformidades
- [ ] `python3 -m pytest trilha/tools/tests/` — verde
- [ ] `python3 -m pytest trilha/capstone/tests/` — verde
- [ ] `python3 trilha/tools/gerar_indice.py --check` — índice em dia

<!-- Se algum comando não se aplica à sua mudança, diga aqui qual e por quê. Não
     marque caixa de comando que você não rodou. -->

## Notas para a revisão

<!-- Opcional: decisão de gosto que você tomou, alternativa que descartou, ou
     ponto em que quer opinião. -->
