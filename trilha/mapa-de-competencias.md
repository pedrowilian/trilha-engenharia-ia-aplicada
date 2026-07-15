# Mapa de Competências

Este mapa liga cada **resultado de aprendizagem** da trilha — derivado dos
`objetivos_de_aprendizagem` das 104 lições — a ao menos uma **exigência do cargo
de AI Engineer**. A fonte estruturada e validável é [`competencias.yaml`](competencias.yaml);
esta página é a visão legível gerada a partir dela.

As exigências dividem-se em duas categorias: as **8 exigências de mercado**
(`mercado-8`) e os **4 fundamentos clássicos de ML cobrados em entrevista**
(`ml-classico-4`). O validador (`tools/validar_trilha.py`) garante que não há
resultados órfãos e que todas as 12 exigências são entregues por ao menos uma lição.

## Exigências do cargo

| Exigência | Descrição | Categoria |
|-----------|-----------|-----------|
| `req-llm-apps` | Desenvolvimento de aplicações LLM | mercado-8 |
| `req-rag` | Engenharia de pipelines RAG | mercado-8 |
| `req-agentes` | Construção de agentes | mercado-8 |
| `req-prompt` | Prompt engineering | mercado-8 |
| `req-deploy-prod` | Deploy em produção | mercado-8 |
| `req-evals` | Frameworks de avaliação | mercado-8 |
| `req-custo-inferencia` | Gerenciamento de custo de inferência sob alto volume concorrente | mercado-8 |
| `req-verificacao-saidas` | Verificação de saídas | mercado-8 |
| `req-vies-variancia` | Viés-variância | ml-classico-4 |
| `req-calibracao` | Calibração | ml-classico-4 |
| `req-data-leakage` | Data leakage | ml-classico-4 |
| `req-gradient-explosion` | Gradient explosion | ml-classico-4 |

## Resultados de aprendizagem por lição

| Resultado de aprendizagem | Lição | Módulo | Exigência(s) | Categoria |
|---------------------------|-------|--------|--------------|-----------|
| Representar dados do mundo real como vetores e operar soma e multiplicação por escalar | 001 | M00 | Desenvolvimento de aplicações LLM | mercado-8 |
| Decidir se um vetor é combinação linear de outros e calcular os coeficientes | 001 | M00 | Desenvolvimento de aplicações LLM | mercado-8 |
| Verificar independência linear e expressar um vetor em coordenadas de uma base | 001 | M00 | Desenvolvimento de aplicações LLM | mercado-8 |
| Construir matrizes, identificar sua forma e calcular a transposta e a identidade | 002 | M00 | Desenvolvimento de aplicações LLM | mercado-8 |
| Multiplicar matrizes e matriz por vetor, reconhecendo a não-comutatividade | 002 | M00 | Desenvolvimento de aplicações LLM | mercado-8 |
| Calcular a inversa e usá-la para resolver um sistema linear A x = b | 002 | M00 | Desenvolvimento de aplicações LLM | mercado-8 |
| Interpretar a multiplicação matriz-vetor como uma transformação linear do espaço e verificar a propriedade de linearidade em Python | 003 | M00 | Desenvolvimento de aplicações LLM | mercado-8 |
| Reconhecer rotação, escala e cisalhamento a partir da matriz e aplicá-las a pontos do plano | 003 | M00 | Desenvolvimento de aplicações LLM | mercado-8 |
| Compor transformações via produto de matrizes e explicar por que a ordem importa | 003 | M00 | Desenvolvimento de aplicações LLM | mercado-8 |
| Explicar autovalores e autovetores como as direções invariantes de uma transformação linear e verificar a equação A·v = λ·v em Python | 004 | M00 | Desenvolvimento de aplicações LLM; Engenharia de pipelines RAG | mercado-8 |
| Descrever a intuição da SVD como decomposição em rotação–escala–rotação e medir o erro de aproximação de baixo posto | 004 | M00 | Desenvolvimento de aplicações LLM; Engenharia de pipelines RAG | mercado-8 |
| Aplicar PCA para reduzir a dimensionalidade preservando a maior variância e relacionar isso à compressão de embeddings | 004 | M00 | Desenvolvimento de aplicações LLM; Engenharia de pipelines RAG | mercado-8 |
| Calcular as normas L1, L2 e L-infinito de um vetor e normalizá-lo pela norma L2 | 005 | M00 | Desenvolvimento de aplicações LLM | mercado-8 |
| Calcular o produto interno e a similaridade do cosseno e interpretar o ângulo entre vetores | 005 | M00 | Desenvolvimento de aplicações LLM | mercado-8 |
| Comparar distância euclidiana e similaridade do cosseno e justificar o uso do cosseno em busca semântica | 005 | M00 | Desenvolvimento de aplicações LLM | mercado-8 |
| Calcular a taxa de variação média de uma função em um intervalo | 006 | M00 | Gradient explosion | ml-classico-4 |
| Aproximar a derivada de uma função como o limite da razão incremental e compará-la à derivada analítica | 006 | M00 | Gradient explosion | ml-classico-4 |
| Interpretar a derivada como taxa de variação instantânea e explicar o que significa otimizar uma função | 006 | M00 | Gradient explosion | ml-classico-4 |
| Calcular derivadas parciais de funções de várias variáveis fixando as demais | 007 | M00 | Gradient explosion | ml-classico-4 |
| Construir o vetor gradiente e interpretá-lo como a direção de maior crescimento | 007 | M00 | Gradient explosion | ml-classico-4 |
| Aplicar a regra da cadeia a funções compostas e relacioná-la à base do backpropagation | 007 | M00 | Gradient explosion | ml-classico-4 |
| Calcular probabilidades de eventos usando os axiomas e a regra da soma (inclusão-exclusão) | 008 | M00 | Calibração | ml-classico-4 |
| Distinguir variáveis aleatórias discretas e contínuas e calcular esperança e variância a partir da distribuição | 008 | M00 | Calibração | ml-classico-4 |
| Aplicar o teorema de Bayes para atualizar uma crença a priori diante de uma evidência observada | 008 | M00 | Calibração | ml-classico-4 |
| Explicar por que modelos de Machine Learning produzem saídas probabilísticas em vez de respostas determinísticas | 008 | M00 | Calibração | ml-classico-4 |
| Calcular medidas de tendência central e de dispersão (média, mediana, variância e desvio padrão) de uma amostra | 009 | M00 | Frameworks de avaliação | mercado-8 |
| Distinguir variância populacional de variância amostral e justificar o divisor n-1 | 009 | M00 | Frameworks de avaliação | mercado-8 |
| Estimar o erro padrão da média e construir um intervalo de confiança de 95% via aproximação normal | 009 | M00 | Frameworks de avaliação | mercado-8 |
| Conduzir um teste de hipótese de duas proporções e interpretar o p-valor em um teste A/B | 009 | M00 | Frameworks de avaliação | mercado-8 |
| Calcular a log-verossimilhança de um conjunto de dados e encontrar o estimador de máxima verossimilhança (MLE) | 010 | M00 | Calibração | ml-classico-4 |
| Calcular a entropia de uma distribuição e a entropia cruzada entre duas distribuições | 010 | M00 | Calibração | ml-classico-4 |
| Calcular a divergência KL e demonstrar numericamente a identidade H(p,q) = H(p) + KL(p\|\|q) | 010 | M00 | Calibração | ml-classico-4 |
| Explicar como verossimilhança, entropia cruzada e KL dão origem às funções de perda modernas de ML | 010 | M00 | Calibração | ml-classico-4 |
| Definir machine learning e distinguir os paradigmas supervisionado, não-supervisionado e por reforço | 011 | M01 | Viés-variância | ml-classico-4 |
| Implementar em Python um exemplo mínimo de cada paradigma (1-NN, k-means, bandit) | 011 | M01 | Viés-variância | ml-classico-4 |
| Escolher o paradigma adequado a partir do formato dos dados e do objetivo | 011 | M01 | Viés-variância | ml-classico-4 |
| Definir função de perda e seu papel no treinamento supervisionado | 012 | M01 | Viés-variância | ml-classico-4 |
| Implementar MSE para regressão e cross-entropy (binária e multiclasse) para classificação | 012 | M01 | Viés-variância | ml-classico-4 |
| Justificar a escolha da perda a partir do tipo de problema e da conexão com verossimilhança | 012 | M01 | Viés-variância | ml-classico-4 |
| Derivar a regra de atualização de parâmetros do gradient descent | 013 | M01 | Viés-variância; Gradient explosion | ml-classico-4 |
| Implementar batch, mini-batch e SGD em Python e comparar a convergência | 013 | M01 | Viés-variância; Gradient explosion | ml-classico-4 |
| Diagnosticar o efeito da taxa de aprendizado sobre a convergência | 013 | M01 | Viés-variância; Gradient explosion | ml-classico-4 |
| Explicar backpropagation como aplicação da regra da cadeia em um grafo computacional | 014 | M01 | Viés-variância | ml-classico-4 |
| Calcular gradientes via forward e backward pass em Python para um grafo e um neurônio | 014 | M01 | Viés-variância | ml-classico-4 |
| Validar gradientes analíticos contra a aproximação numérica (gradient checking) | 014 | M01 | Viés-variância | ml-classico-4 |
| Explicar como a regularização combate o overfitting penalizando a complexidade | 015 | M01 | Viés-variância | ml-classico-4 |
| Implementar regularização L2 (ridge) e L1 (esparsidade via soft-thresholding) em Python | 015 | M01 | Viés-variância | ml-classico-4 |
| Aplicar dropout e early stopping como técnicas de regularização no treinamento | 015 | M01 | Viés-variância | ml-classico-4 |
| Enunciar a decomposição do erro esperado em viés², variância e ruído irredutível | 016 | M01 | Viés-variância | ml-classico-4 |
| Relacionar complexidade do modelo a viés (underfitting) e variância (overfitting) | 016 | M01 | Viés-variância | ml-classico-4 |
| Estimar empiricamente viés e variância em Python e identificar a complexidade ótima | 016 | M01 | Viés-variância | ml-classico-4 |
| Diagnosticar overfitting e underfitting a partir dos erros de treino e validação | 017 | M01 | Viés-variância | ml-classico-4 |
| Implementar validação cruzada k-fold do zero para selecionar hiperparâmetros | 017 | M01 | Viés-variância | ml-classico-4 |
| Interpretar curvas de aprendizado para decidir entre mais dados e mais/menos capacidade | 017 | M01 | Viés-variância | ml-classico-4 |
| Definir calibração e distinguir acurácia de confiabilidade das probabilidades | 018 | M01 | Calibração; Viés-variância | ml-classico-4 |
| Construir um diagrama de confiabilidade e calcular o Expected Calibration Error (ECE) | 018 | M01 | Calibração; Viés-variância | ml-classico-4 |
| Aplicar temperature scaling para recalibrar um modelo superconfiante | 018 | M01 | Calibração; Viés-variância | ml-classico-4 |
| Explicar por que a acurácia engana sob forte desbalanceamento de classes | 019 | M01 | Viés-variância | ml-classico-4 |
| Calcular precision, recall e F1 a partir da matriz de confusão | 019 | M01 | Viés-variância | ml-classico-4 |
| Ajustar o limiar de decisão para equilibrar precision e recall em dados desbalanceados | 019 | M01 | Viés-variância | ml-classico-4 |
| Definir data leakage e reconhecer target leakage, vazamento de pré-processamento e vazamento temporal | 020 | M01 | Data leakage; Viés-variância | ml-classico-4 |
| Demonstrar em Python como o leakage infla artificialmente as métricas | 020 | M01 | Data leakage; Viés-variância | ml-classico-4 |
| Aplicar separação treino/teste correta e splits temporais para evitar vazamento | 020 | M01 | Data leakage; Viés-variância | ml-classico-4 |
| Desenhar um experimento A/B com grupos de controle e tratamento randomizados | 021 | M01 | Viés-variância | ml-classico-4 |
| Aplicar um teste de hipótese para duas proporções e interpretar o p-valor | 021 | M01 | Viés-variância | ml-classico-4 |
| Reconhecer armadilhas como peeking e o efeito do tamanho de amostra na significância | 021 | M01 | Viés-variância | ml-classico-4 |
| Descrever o neurônio artificial como soma ponderada, viés e função de ativação | 022 | M02 | Viés-variância | ml-classico-4 |
| Implementar a regra de aprendizado do perceptron em Python e observar a convergência | 022 | M02 | Viés-variância | ml-classico-4 |
| Explicar por que um perceptron só separa classes linearmente separáveis (limite do XOR) | 022 | M02 | Viés-variância | ml-classico-4 |
| Explicar por que redes precisam de funções de ativação não lineares | 023 | M02 | Viés-variância | ml-classico-4 |
| Implementar sigmoid, tanh, ReLU e GELU em Python com suas derivadas | 023 | M02 | Viés-variância | ml-classico-4 |
| Comparar saturação, esparsidade e o problema do neurônio morto entre ativações | 023 | M02 | Viés-variância | ml-classico-4 |
| Descrever um MLP como camadas densas alternadas com ativações não lineares | 024 | M02 | Viés-variância | ml-classico-4 |
| Implementar o forward pass de um MLP com multiplicação matriz-vetor em Python | 024 | M02 | Viés-variância | ml-classico-4 |
| Mostrar que uma camada oculta resolve o XOR e treinar um MLP do zero com backprop | 024 | M02 | Viés-variância | ml-classico-4 |
| Explicar por que inicializar pesos com zeros impede o aprendizado (simetria) | 025 | M02 | Viés-variância | ml-classico-4 |
| Derivar o escalonamento de variância das inicializações de Xavier e He | 025 | M02 | Viés-variância | ml-classico-4 |
| Demonstrar em Python que a inicialização correta mantém a variância das ativações estável | 025 | M02 | Viés-variância | ml-classico-4 |
| Explicar por que normalizar ativações estabiliza e acelera o treino | 026 | M02 | Viés-variância | ml-classico-4 |
| Implementar batch normalization com parâmetros γ e β em Python | 026 | M02 | Viés-variância | ml-classico-4 |
| Contrastar batch norm e layer norm quanto ao eixo de normalização | 026 | M02 | Viés-variância | ml-classico-4 |
| Explicar por que gradientes desaparecem ou explodem em redes profundas | 027 | M02 | Viés-variância; Gradient explosion | ml-classico-4 |
| Quantificar em Python o encolhimento do gradiente com ativações saturantes | 027 | M02 | Viés-variância; Gradient explosion | ml-classico-4 |
| Aplicar gradient clipping por norma como mitigação do exploding gradient | 027 | M02 | Viés-variância; Gradient explosion | ml-classico-4 |
| Explicar como o momentum acumula velocidade para acelerar a convergência | 028 | M02 | Viés-variância | ml-classico-4 |
| Descrever a taxa de aprendizado adaptativa por parâmetro do RMSProp | 028 | M02 | Viés-variância | ml-classico-4 |
| Implementar o passo do Adam com correção de bias em Python | 028 | M02 | Viés-variância | ml-classico-4 |
| Explicar a convolução 2D como detector de padrões com pesos compartilhados | 029 | M02 | Viés-variância | ml-classico-4 |
| Implementar convolução e pooling do zero em Python | 029 | M02 | Viés-variância | ml-classico-4 |
| Calcular o tamanho do mapa de saída e comparar o custo de parâmetros com camadas densas | 029 | M02 | Viés-variância | ml-classico-4 |
| Descrever a recorrência de uma RNN e seu estado oculto como memória | 030 | M02 | Viés-variância | ml-classico-4 |
| Explicar por que RNNs simples sofrem vanishing gradient ao longo do tempo | 030 | M02 | Viés-variância | ml-classico-4 |
| Implementar o gating de LSTM/GRU em Python e mostrar como preserva memória | 030 | M02 | Viés-variância | ml-classico-4 |
| Explicar como conexões residuais viabilizam o treino de redes muito profundas | 031 | M02 | Viés-variância | ml-classico-4 |
| Descrever transfer learning: feature extraction e fine-tuning | 031 | M02 | Viés-variância | ml-classico-4 |
| Quantificar em Python a economia de parâmetros treináveis e o ganho de features pré-treinadas | 031 | M02 | Viés-variância | ml-classico-4 |
| Explicar por que texto precisa virar vetores numéricos antes de alimentar um modelo de ML | 032 | M03 | Desenvolvimento de aplicações LLM | mercado-8 |
| Implementar bag-of-words, TF-IDF e n-grams do zero em Python | 032 | M03 | Desenvolvimento de aplicações LLM | mercado-8 |
| Contrastar representações esparsas (BoW/TF-IDF) e densas (embeddings) quanto a dimensionalidade e semântica | 032 | M03 | Desenvolvimento de aplicações LLM | mercado-8 |
| Explicar o papel da tokenização em subpalavras e por que ela equilibra tamanho de vocabulário e cobertura | 033 | M03 | Desenvolvimento de aplicações LLM | mercado-8 |
| Implementar o treino de merges do BPE e a segmentação greedy do WordPiece em Python | 033 | M03 | Desenvolvimento de aplicações LLM | mercado-8 |
| Construir um tokenizador reversível (estilo SentencePiece) e provar a igualdade exata na ida-e-volta texto → ids → texto | 033 | M03 | Desenvolvimento de aplicações LLM | mercado-8 |
| Explicar a hipótese distribucional e por que embeddings densos capturam semântica que o bag-of-words não captura | 034 | M03 | Engenharia de pipelines RAG | mercado-8 |
| Implementar busca por vizinho mais próximo e analogias vetoriais sobre uma tabela de embeddings em Python | 034 | M03 | Engenharia de pipelines RAG | mercado-8 |
| Distinguir embeddings estáticos (word2vec/GloVe) de embeddings contextuais e demonstrar a dependência do contexto | 034 | M03 | Engenharia de pipelines RAG | mercado-8 |
| Calcular produto interno, distância euclidiana e similaridade do cosseno entre embeddings em Python | 035 | M03 | Engenharia de pipelines RAG | mercado-8 |
| Explicar quando os rankings por cosseno e por L2 discordam e o papel da magnitude | 035 | M03 | Engenharia de pipelines RAG | mercado-8 |
| Justificar por que normalizar embeddings torna o produto interno equivalente ao cosseno na busca vetorial | 035 | M03 | Engenharia de pipelines RAG | mercado-8 |
| Implementar busca vetorial exata por varredura linear e recuperar os k vizinhos mais próximos em Python | 036 | M03 | Engenharia de pipelines RAG | mercado-8 |
| Explicar o papel da métrica de distância na ordenação dos resultados de k-NN | 036 | M03 | Engenharia de pipelines RAG | mercado-8 |
| Analisar o custo O(n·d) da busca exata e justificar por que ele motiva a busca aproximada | 036 | M03 | Engenharia de pipelines RAG | mercado-8 |
| Definir busca aproximada de vizinhos (ANN) e medir sua qualidade pelo recall@k contra o k-NN exato | 037 | M03 | Engenharia de pipelines RAG | mercado-8 |
| Implementar um índice IVF didático que examina apenas clusters próximos da consulta | 037 | M03 | Engenharia de pipelines RAG | mercado-8 |
| Analisar o trade-off recall × latência variando o esforço de busca (nprobe) | 037 | M03 | Engenharia de pipelines RAG | mercado-8 |
| Implementar busca greedy em um grafo de vizinhança navegável e explicar quando ela fica presa em ótimos locais | 038 | M03 | Engenharia de pipelines RAG | mercado-8 |
| Explicar como as camadas hierárquicas do HNSW reduzem o número de saltos até o vizinho | 038 | M03 | Engenharia de pipelines RAG | mercado-8 |
| Analisar o efeito do parâmetro ef sobre recall e custo na busca em grafo do HNSW | 038 | M03 | Engenharia de pipelines RAG | mercado-8 |
| Explicar por que o estado oculto de tamanho fixo de uma RNN é um gargalo para sequências longas | 039 | M04 | Desenvolvimento de aplicações LLM | mercado-8 |
| Quantificar o decaimento da influência de entradas distantes e relacioná-lo ao comprimento do caminho de informação | 039 | M04 | Desenvolvimento de aplicações LLM | mercado-8 |
| Contrastar o custo sequencial da RNN com o acesso direto e paralelizável da atenção | 039 | M04 | Desenvolvimento de aplicações LLM | mercado-8 |
| Projetar embeddings em Query, Key e Value e explicar o papel de cada um | 040 | M04 | Desenvolvimento de aplicações LLM | mercado-8 |
| Implementar scaled dot-product attention do zero em numpy, incluindo a softmax estável | 040 | M04 | Desenvolvimento de aplicações LLM | mercado-8 |
| Justificar a divisão por raiz de d_k e interpretar a saída como média ponderada dos Values | 040 | M04 | Desenvolvimento de aplicações LLM | mercado-8 |
| Explicar por que o self-attention é invariante à ordem e precisa de informação posicional | 041 | M04 | Desenvolvimento de aplicações LLM | mercado-8 |
| Implementar o positional encoding sinusoidal em numpy e somá-lo aos embeddings | 041 | M04 | Desenvolvimento de aplicações LLM | mercado-8 |
| Justificar a propriedade de deslocamento relativo das funções seno/cosseno | 041 | M04 | Desenvolvimento de aplicações LLM | mercado-8 |
| Dividir as projeções em h cabeças de dimensão d_k = d_model / h e remontá-las | 042 | M04 | Desenvolvimento de aplicações LLM | mercado-8 |
| Implementar multi-head attention do zero em numpy, com atenção paralela por cabeça | 042 | M04 | Desenvolvimento de aplicações LLM | mercado-8 |
| Explicar por que múltiplas cabeças capturam relações complementares na mesma sequência | 042 | M04 | Desenvolvimento de aplicações LLM | mercado-8 |
| Descrever o fluxo de um bloco Transformer: atenção, FFN, conexões residuais e normalização | 043 | M04 | Desenvolvimento de aplicações LLM | mercado-8 |
| Implementar conexão residual + LayerNorm e a feed-forward position-wise em numpy | 043 | M04 | Desenvolvimento de aplicações LLM | mercado-8 |
| Compor as sub-camadas num bloco de encoder completo que preserva a forma da entrada | 043 | M04 | Desenvolvimento de aplicações LLM | mercado-8 |
| Explicar o que é um LLM como um modelo de linguagem que estima a probabilidade do próximo token e fatoriza a probabilidade de uma sequência pela regra da cadeia | 044 | M05 | Desenvolvimento de aplicações LLM | mercado-8 |
| Calcular cross-entropy e perplexidade de um modelo de linguagem sobre uma sequência em Python | 044 | M05 | Desenvolvimento de aplicações LLM | mercado-8 |
| Interpretar leis de escala (loss como lei de potência em parâmetros/dados/compute) e prever o efeito de aumentar o tamanho do modelo | 044 | M05 | Desenvolvimento de aplicações LLM | mercado-8 |
| Explicar o objetivo auto-supervisionado de pré-treino (next-token / teacher forcing) e por que não exige rótulos humanos | 045 | M05 | Desenvolvimento de aplicações LLM | mercado-8 |
| Calcular a perda média de pré-treino sobre um corpus e estimar passos de treino a partir do volume de tokens em Python | 045 | M05 | Desenvolvimento de aplicações LLM | mercado-8 |
| Estimar o custo de compute de um pré-treino pela regra C ≈ 6·N·D e interpretar a alocação compute-ótima (Chinchilla) | 045 | M05 | Desenvolvimento de aplicações LLM | mercado-8 |
| Explicar por que um modelo pré-treinado precisa de instruction tuning para seguir instruções e como o formato instrução-resposta estrutura os dados | 046 | M05 | Desenvolvimento de aplicações LLM | mercado-8 |
| Implementar a perda mascarada do SFT (cross-entropy apenas sobre os tokens da resposta) em Python | 046 | M05 | Desenvolvimento de aplicações LLM | mercado-8 |
| Comparar a perda do SFT com a do pré-treino e explicar o efeito da máscara sobre o gradiente | 046 | M05 | Desenvolvimento de aplicações LLM | mercado-8 |
| Explicar as três etapas do RLHF (SFT, reward model, otimização por RL) e por que o sinal de preferência humana substitui um rótulo de resposta ideal | 047 | M05 | Desenvolvimento de aplicações LLM | mercado-8 |
| Implementar a perda de preferência de um reward model (Bradley-Terry) e a recompensa com penalidade KL em Python | 047 | M05 | Desenvolvimento de aplicações LLM | mercado-8 |
| Calcular o objetivo clipado do PPO e explicar como o clipping estabiliza a atualização da política | 047 | M05 | Desenvolvimento de aplicações LLM | mercado-8 |
| Explicar a perda do DPO e como ela otimiza preferências diretamente, sem treinar um reward model nem rodar RL online | 048 | M05 | Desenvolvimento de aplicações LLM | mercado-8 |
| Implementar a perda do DPO a partir de log-probabilidades da política e da referência em Python | 048 | M05 | Desenvolvimento de aplicações LLM | mercado-8 |
| Comparar DPO e PPO em pipeline, custo, estabilidade e quando preferir cada um (relevante em entrevista) | 048 | M05 | Desenvolvimento de aplicações LLM | mercado-8 |
| Explicar como a temperatura reescala os logits e controla o trade-off entre diversidade e determinismo na geração | 049 | M05 | Desenvolvimento de aplicações LLM | mercado-8 |
| Implementar filtragem top-k e top-p (nucleus) sobre a distribuição do próximo token em Python | 049 | M05 | Desenvolvimento de aplicações LLM | mercado-8 |
| Amostrar tokens de forma reprodutível de uma distribuição truncada e interpretar o efeito de cada hiperparâmetro | 049 | M05 | Desenvolvimento de aplicações LLM | mercado-8 |
| Distinguir modelos generativos de discriminativos e descrever o que torna a IA generativa diferente | 050 | M06 | Desenvolvimento de aplicações LLM | mercado-8 |
| Explicar como modalidades distintas (texto, imagem, áudio) são convertidas em tokens para um modelo multimodal | 050 | M06 | Desenvolvimento de aplicações LLM | mercado-8 |
| Calcular similaridade no espaço de embedding compartilhado para recuperar a melhor correspondência entre modalidades | 050 | M06 | Desenvolvimento de aplicações LLM | mercado-8 |
| Montar o corpo de uma requisição de chat no formato de mensagens com papéis usado pelas APIs de LLM | 051 | M06 | Desenvolvimento de aplicações LLM; Gerenciamento de custo de inferência sob alto volume concorrente | mercado-8 |
| Aplicar autenticação por bearer token mascarando a chave de API em logs e saídas | 051 | M06 | Desenvolvimento de aplicações LLM; Gerenciamento de custo de inferência sob alto volume concorrente | mercado-8 |
| Estimar tokens de entrada/saída e calcular o custo de uma chamada com preços por 1k tokens | 051 | M06 | Desenvolvimento de aplicações LLM; Gerenciamento de custo de inferência sob alto volume concorrente | mercado-8 |
| Identificar as partes anatômicas de um prompt e montá-las na ordem de leitura correta | 052 | M06 | Prompt engineering; Desenvolvimento de aplicações LLM | mercado-8 |
| Renderizar prompts reutilizáveis a partir de templates com variáveis nomeadas | 052 | M06 | Prompt engineering; Desenvolvimento de aplicações LLM | mercado-8 |
| Aplicar delimitadores e instruções claras para separar instrução de dados do usuário | 052 | M06 | Prompt engineering; Desenvolvimento de aplicações LLM | mercado-8 |
| Construir prompts few-shot e prever um rótulo por similaridade aos exemplos fornecidos | 053 | M06 | Prompt engineering | mercado-8 |
| Aplicar chain-of-thought registrando passos intermediários explícitos até a resposta | 053 | M06 | Prompt engineering | mercado-8 |
| Decompor uma tarefa complexa em subtarefas e combinar seus resultados | 053 | M06 | Prompt engineering | mercado-8 |
| Instruir o modelo a produzir JSON conforme um schema e parsear a saída estruturada | 054 | M06 | Verificação de saídas | mercado-8 |
| Validar objetos parseados contra um schema, detectando chaves ausentes e tipos inválidos | 054 | M06 | Verificação de saídas | mercado-8 |
| Garantir o round-trip dict → JSON → dict com igualdade exata | 054 | M06 | Verificação de saídas | mercado-8 |
| Explicar a limitação do conhecimento paramétrico de um LLM e por que a recuperação não-paramétrica a complementa | 055 | M07 | Engenharia de pipelines RAG; Desenvolvimento de aplicações LLM | mercado-8 |
| Implementar o fluxo retrieve-augment-generate mínimo em Python puro | 055 | M07 | Engenharia de pipelines RAG; Desenvolvimento de aplicações LLM | mercado-8 |
| Anexar atribuição de fontes a uma resposta gerada a partir de documentos recuperados | 055 | M07 | Engenharia de pipelines RAG; Desenvolvimento de aplicações LLM | mercado-8 |
| Particionar um documento em chunks de tamanho fixo e em janelas deslizantes com sobreposição | 056 | M07 | Engenharia de pipelines RAG | mercado-8 |
| Explicar o trade-off entre granularidade do chunk e preservação de contexto na borda | 056 | M07 | Engenharia de pipelines RAG | mercado-8 |
| Construir um índice invertido (termo → chunks) e resolver buscas por interseção de postings | 056 | M07 | Engenharia de pipelines RAG | mercado-8 |
| Representar consulta e documentos como vetores e medir relevância pela similaridade do cosseno | 057 | M07 | Engenharia de pipelines RAG; Desenvolvimento de aplicações LLM | mercado-8 |
| Recuperar os top-k documentos por cosseno com desempate determinístico | 057 | M07 | Engenharia de pipelines RAG; Desenvolvimento de aplicações LLM | mercado-8 |
| Montar o prompt aumentado e gerar a resposta, integrando as três etapas num pipeline executável | 057 | M07 | Engenharia de pipelines RAG; Desenvolvimento de aplicações LLM | mercado-8 |
| Implementar um índice flat de busca exata e contar suas comparações | 058 | M07 | Engenharia de pipelines RAG | mercado-8 |
| Construir um índice particionado tipo IVF e explicar o trade-off entre comparações e recall | 058 | M07 | Engenharia de pipelines RAG | mercado-8 |
| Combinar filtragem por metadados com busca vetorial, no modelo do pgvector | 058 | M07 | Engenharia de pipelines RAG | mercado-8 |
| Implementar o score BM25 e explicar o papel de IDF, saturação (k1) e normalização por comprimento (b) | 059 | M07 | Engenharia de pipelines RAG | mercado-8 |
| Demonstrar a complementaridade entre recuperação densa (semântica) e esparsa (lexical) | 059 | M07 | Engenharia de pipelines RAG | mercado-8 |
| Fundir rankings densos e esparsos com Reciprocal Rank Fusion (RRF) | 059 | M07 | Engenharia de pipelines RAG | mercado-8 |
| Consultar múltiplos índices especializados e unir os candidatos num pool único | 060 | M07 | Engenharia de pipelines RAG | mercado-8 |
| Estruturar recuperação em duas etapas (recall amplo seguido de precisão) e justificar o custo | 060 | M07 | Engenharia de pipelines RAG | mercado-8 |
| Implementar um re-ranker que reordena candidatos olhando o par consulta-documento em conjunto | 060 | M07 | Engenharia de pipelines RAG | mercado-8 |
| Implementar a decisão de recuperar (quando buscar vs responder direto) | 061 | M07 | Engenharia de pipelines RAG; Construção de agentes | mercado-8 |
| Reformular a consulta e iterar a recuperação quando o resultado é insuficiente | 061 | M07 | Engenharia de pipelines RAG; Construção de agentes | mercado-8 |
| Avaliar a suficiência do contexto e parar o laço com um limite de iterações | 061 | M07 | Engenharia de pipelines RAG; Construção de agentes | mercado-8 |
| Descrever o laço de controle de um agente (percepção, raciocínio, ação, feedback) | 062 | M08 | Construção de agentes; Desenvolvimento de aplicações LLM | mercado-8 |
| Implementar em Python um laço de agente determinístico com planner, executor, memória e toolbox | 062 | M08 | Construção de agentes; Desenvolvimento de aplicações LLM | mercado-8 |
| Garantir a terminação do laço com uma condição de parada e um limite de iterações | 062 | M08 | Construção de agentes; Desenvolvimento de aplicações LLM | mercado-8 |
| Explicar o padrão ReAct e o ciclo Thought → Action → Observation | 063 | M08 | Construção de agentes | mercado-8 |
| Parsear a ação emitida por um agente no formato ferramenta[args] | 063 | M08 | Construção de agentes | mercado-8 |
| Implementar um laço ReAct determinístico que termina em uma resposta final | 063 | M08 | Construção de agentes | mercado-8 |
| Distinguir Plan-Execute de ReAct e justificar quando planejar antecipadamente | 064 | M08 | Construção de agentes | mercado-8 |
| Implementar um planner que gera um plano ordenado e um executor sequencial | 064 | M08 | Construção de agentes | mercado-8 |
| Implementar replanejamento determinístico quando um passo falha | 064 | M08 | Construção de agentes | mercado-8 |
| Explicar o padrão Reflection e o papel do crítico na auto-revisão | 065 | M08 | Construção de agentes | mercado-8 |
| Implementar um ciclo gerar → criticar → revisar determinístico | 065 | M08 | Construção de agentes | mercado-8 |
| Definir um critério de aceitação por qualidade e por limite de iterações | 065 | M08 | Construção de agentes | mercado-8 |
| Descrever um esquema de ferramenta (nome, descrição, parâmetros) e serializá-lo | 066 | M08 | Construção de agentes; Verificação de saídas | mercado-8 |
| Despachar uma tool-call para a função registrada correspondente | 066 | M08 | Construção de agentes; Verificação de saídas | mercado-8 |
| Garantir o round-trip tool-call → JSON → tool-call com igualdade exata | 066 | M08 | Construção de agentes; Verificação de saídas | mercado-8 |
| Distinguir memória de curto prazo, de longo prazo e episódica em agentes | 067 | M08 | Construção de agentes; Engenharia de pipelines RAG | mercado-8 |
| Implementar um buffer de curto prazo de tamanho fixo e uma memória episódica com embeddings | 067 | M08 | Construção de agentes; Engenharia de pipelines RAG | mercado-8 |
| Recuperar episódios relevantes por similaridade do cosseno (top-k) | 067 | M08 | Construção de agentes; Engenharia de pipelines RAG | mercado-8 |
| Estimar o consumo de tokens de um histórico e compará-lo ao orçamento da janela | 068 | M08 | Construção de agentes | mercado-8 |
| Aplicar truncamento por recência preservando a mensagem de sistema | 068 | M08 | Construção de agentes | mercado-8 |
| Reduzir tokens por sumarização do histórico antigo | 068 | M08 | Construção de agentes | mercado-8 |
| Modelar um agente como um grafo de estado com nós e arestas | 069 | M08 | Construção de agentes | mercado-8 |
| Implementar um motor que percorre o grafo a partir de um estado compartilhado | 069 | M08 | Construção de agentes | mercado-8 |
| Usar arestas condicionais para criar laços e ramificações de controle | 069 | M08 | Construção de agentes | mercado-8 |
| Instrumentar um agente com um traço de execução para observabilidade | 070 | M08 | Construção de agentes; Deploy em produção | mercado-8 |
| Aplicar guardrails e human-in-the-loop para conter ações perigosas | 070 | M08 | Construção de agentes; Deploy em produção | mercado-8 |
| Prevenir laços descontrolados por limite de passos e detecção de repetição | 070 | M08 | Construção de agentes; Deploy em produção | mercado-8 |
| Distinguir os padrões de orquestração multi-agente (Supervisor, Hierárquico, Group-chat, Delegação) | 071 | M08 | Construção de agentes | mercado-8 |
| Implementar um supervisor que delega tarefas a agentes especializados | 071 | M08 | Construção de agentes | mercado-8 |
| Agregar e reconciliar resultados de múltiplos agentes de forma determinística | 071 | M08 | Construção de agentes | mercado-8 |
| Explicar o problema de integração M×N que o MCP resolve | 072 | M09 | Construção de agentes | mercado-8 |
| Descrever os papéis de host, client e server na arquitetura do MCP | 072 | M09 | Construção de agentes | mercado-8 |
| Modelar a negociação de capacidades (handshake) entre cliente e servidor | 072 | M09 | Construção de agentes | mercado-8 |
| Distinguir as três primitivas do MCP e quem controla cada uma | 073 | M09 | Construção de agentes | mercado-8 |
| Listar e ler resources identificados por URI | 073 | M09 | Construção de agentes | mercado-8 |
| Descrever e invocar tools e renderizar prompts a partir de templates | 073 | M09 | Construção de agentes | mercado-8 |
| Montar e serializar uma request JSON-RPC 2.0 de forma canônica | 074 | M09 | Construção de agentes; Verificação de saídas | mercado-8 |
| Distinguir response de sucesso, response de erro e notification | 074 | M09 | Construção de agentes; Verificação de saídas | mercado-8 |
| Garantir o round-trip request → JSON → request com igualdade exata | 074 | M09 | Construção de agentes; Verificação de saídas | mercado-8 |
| Implementar um servidor MCP que registra handlers e despacha por método | 075 | M09 | Construção de agentes | mercado-8 |
| Implementar um cliente MCP que numera requests e casa respostas pelo id | 075 | M09 | Construção de agentes | mercado-8 |
| Executar o ciclo completo tools/list seguido de tools/call | 075 | M09 | Construção de agentes | mercado-8 |
| Aplicar uma pipeline de limpeza (normalização, remoção de vazios e deduplicação) sobre um dataset cru em Python | 076 | M10 | Desenvolvimento de aplicações LLM | mercado-8 |
| Balancear classes de um dataset por subamostragem de forma reprodutível | 076 | M10 | Desenvolvimento de aplicações LLM | mercado-8 |
| Serializar e parsear exemplos no formato JSONL de chat com round-trip exato | 076 | M10 | Desenvolvimento de aplicações LLM | mercado-8 |
| Decidir entre RAG, fine-tuning, ambos ou prompt engineering a partir das características do problema | 077 | M10 | Desenvolvimento de aplicações LLM | mercado-8 |
| Estimar a memória de treino do fine-tuning completo (pesos, gradientes e estados do otimizador) | 077 | M10 | Desenvolvimento de aplicações LLM | mercado-8 |
| Aplicar uma matriz de decisão ponderada para comparar RAG e fine-tuning | 077 | M10 | Desenvolvimento de aplicações LLM | mercado-8 |
| Construir a atualização de baixo posto ΔW = B·A e verificar seu posto em Python | 078 | M10 | Desenvolvimento de aplicações LLM | mercado-8 |
| Comparar o número de parâmetros treináveis do LoRA, r·(d+k), com o da matriz cheia, d·k | 078 | M10 | Desenvolvimento de aplicações LLM | mercado-8 |
| Aplicar o fator de escala alpha/r e medir seu efeito na saída da camada adaptada | 078 | M10 | Desenvolvimento de aplicações LLM | mercado-8 |
| Fazer upload e validar um arquivo JSONL de treino usando um cliente simulado | 079 | M10 | Desenvolvimento de aplicações LLM | mercado-8 |
| Criar um job de fine-tuning com hiperparâmetros e estimar o número de passos de treino | 079 | M10 | Desenvolvimento de aplicações LLM | mercado-8 |
| Monitorar a progressão do treino e usar o nome do modelo ajustado resultante | 079 | M10 | Desenvolvimento de aplicações LLM | mercado-8 |
| Calcular métricas de avaliação (acurácia e taxa de formato válido) sobre um conjunto de teste | 080 | M10 | Frameworks de avaliação | mercado-8 |
| Conduzir um teste A/B entre o modelo base e o ajustado e quantificar o lift | 080 | M10 | Frameworks de avaliação | mercado-8 |
| Detectar overfitting comparando as curvas de perda de treino e validação e indicar early stopping | 080 | M10 | Frameworks de avaliação | mercado-8 |
| Decidir, num design AI-first, quando usar IA e quando usar regras determinísticas | 081 | M11 | Desenvolvimento de aplicações LLM; Deploy em produção | mercado-8 |
| Quantificar o trade-off entre precisão, latência e custo ao escolher uma solução | 081 | M11 | Desenvolvimento de aplicações LLM; Deploy em produção | mercado-8 |
| Projetar degradação graciosa com limiar de confiança e fallback determinístico | 081 | M11 | Desenvolvimento de aplicações LLM; Deploy em produção | mercado-8 |
| Quantificar o custo de coordenação adicional de uma arquitetura multi-agente | 082 | M11 | Construção de agentes | mercado-8 |
| Comparar a latência sequencial (single) com a latência paralela (multi) | 082 | M11 | Construção de agentes | mercado-8 |
| Decidir entre single-agent e multi-agente a partir de especialização, latência e orçamento | 082 | M11 | Construção de agentes | mercado-8 |
| Implementar um model router que despacha requisições ao tier adequado | 083 | M11 | Desenvolvimento de aplicações LLM; Gerenciamento de custo de inferência sob alto volume concorrente | mercado-8 |
| Implementar um semantic cache que responde por similaridade de cosseno acima de um limiar | 083 | M11 | Desenvolvimento de aplicações LLM; Gerenciamento de custo de inferência sob alto volume concorrente | mercado-8 |
| Aplicar human-in-the-loop e approval gates combinando confiança e risco | 083 | M11 | Desenvolvimento de aplicações LLM; Gerenciamento de custo de inferência sob alto volume concorrente | mercado-8 |
| Modelar o fluxo de uma requisição pelas camadas gateway → orquestração → serviços | 084 | M11 | Deploy em produção; Gerenciamento de custo de inferência sob alto volume concorrente | mercado-8 |
| Implementar model tiering que escolhe o tier mais forte dentro do SLA de latência | 084 | M11 | Deploy em produção; Gerenciamento de custo de inferência sob alto volume concorrente | mercado-8 |
| Agregar métricas de observabilidade (p50, p95 e taxa de erro) de uma janela de requisições | 084 | M11 | Deploy em produção; Gerenciamento de custo de inferência sob alto volume concorrente | mercado-8 |
| Descrever a anatomia de um eval (dataset, sistema sob teste, scorer e agregação) e implementá-la em Python | 085 | M12 | Frameworks de avaliação; Verificação de saídas | mercado-8 |
| Agregar resultados por accuracy e por taxa de aprovação em relação a um limiar | 085 | M12 | Frameworks de avaliação; Verificação de saídas | mercado-8 |
| Comparar duas versões de um sistema de forma pareada e decidir, de modo binário, se houve regressão | 085 | M12 | Frameworks de avaliação; Verificação de saídas | mercado-8 |
| Calcular precisão, revocação e F1 a partir de TP/FP/FN para tarefas de recuperação/classificação | 086 | M12 | Frameworks de avaliação; Verificação de saídas | mercado-8 |
| Implementar um LLM-as-judge determinístico por rubrica e agregar suas notas | 086 | M12 | Frameworks de avaliação; Verificação de saídas | mercado-8 |
| Distinguir métricas offline (dataset rotulado) de métricas online (sinal de usuário) e medir a lacuna entre elas | 086 | M12 | Frameworks de avaliação; Verificação de saídas | mercado-8 |
| Modelar o custo de uma requisição LLM a partir de tokens de entrada/saída e projetar custo diário e mensal | 087 | M12 | Gerenciamento de custo de inferência sob alto volume concorrente; Deploy em produção | mercado-8 |
| Quantificar a economia de um cache em função da taxa de acerto (hit rate) | 087 | M12 | Gerenciamento de custo de inferência sob alto volume concorrente; Deploy em produção | mercado-8 |
| Explicar como o batching amortiza o overhead fixo e calcular o custo por requisição por tamanho de lote | 087 | M12 | Gerenciamento de custo de inferência sob alto volume concorrente; Deploy em produção | mercado-8 |
| Decompor a latência total em TTFT mais geração e quantificar o ganho percebido do streaming | 088 | M12 | Gerenciamento de custo de inferência sob alto volume concorrente; Deploy em produção | mercado-8 |
| Calcular percentis p50/p95/p99 de latência pelo método nearest-rank e explicar por que a média engana | 088 | M12 | Gerenciamento de custo de inferência sob alto volume concorrente; Deploy em produção | mercado-8 |
| Aplicar a Lei de Little para dimensionar a concorrência necessária a um alvo de vazão | 088 | M12 | Gerenciamento de custo de inferência sob alto volume concorrente; Deploy em produção | mercado-8 |
| Agregar um trace de prompt em latência e custo totais e identificar o span gargalo | 089 | M12 | Deploy em produção; Frameworks de avaliação | mercado-8 |
| Calcular métricas operacionais (taxa de erro e p95) sobre uma janela e verificar SLOs de forma binária | 089 | M12 | Deploy em produção; Frameworks de avaliação | mercado-8 |
| Decidir promover ou reverter um rollout canary comparando-o ao baseline com margens | 089 | M12 | Deploy em produção; Frameworks de avaliação | mercado-8 |
| Calcular a atribuição de features de uma predição em um modelo linear ($w_i x_i$) e ordená-la por importância | 090 | M13 | Frameworks de avaliação; Verificação de saídas | mercado-8 |
| Estimar a importância de cada feature por permutação, medindo o aumento do erro | 090 | M13 | Frameworks de avaliação; Verificação de saídas | mercado-8 |
| Distinguir explicação local (uma instância) de explicação global (média sobre o conjunto) | 090 | M13 | Frameworks de avaliação; Verificação de saídas | mercado-8 |
| Medir a paridade demográfica como diferença entre taxas de seleção por grupo | 091 | M13 | Frameworks de avaliação; Verificação de saídas | mercado-8 |
| Calcular TPR e FPR por grupo para avaliar equalized odds | 091 | M13 | Frameworks de avaliação; Verificação de saídas | mercado-8 |
| Aplicar a regra dos 80% (disparate impact) para classificar uma decisão como justa ou não | 091 | M13 | Frameworks de avaliação; Verificação de saídas | mercado-8 |
| Detectar tentativas de prompt injection por casamento de padrões na entrada | 092 | M13 | Verificação de saídas; Deploy em produção | mercado-8 |
| Pontuar o risco de jailbreak por acúmulo de sinais e aplicar um limiar de bloqueio | 092 | M13 | Verificação de saídas; Deploy em produção | mercado-8 |
| Redigir PII (e-mails e telefones) de um texto antes de logá-lo ou enviá-lo ao modelo | 092 | M13 | Verificação de saídas; Deploy em produção | mercado-8 |
| Classificar um sistema de IA por nível de risco usando regras explícitas | 093 | M13 | Deploy em produção; Verificação de saídas | mercado-8 |
| Pontuar a conformidade de um sistema contra um checklist de requisitos | 093 | M13 | Deploy em produção; Verificação de saídas | mercado-8 |
| Verificar a completude de um model card antes de publicá-lo | 093 | M13 | Deploy em produção; Verificação de saídas | mercado-8 |
| Projetar e comparar o custo mensal de diferentes níveis de modelo sob um mesmo volume | 094 | M13 | Gerenciamento de custo de inferência sob alto volume concorrente; Deploy em produção | mercado-8 |
| Estimar a pegada energética (kWh) e de carbono (kg CO2) de uma carga de inferência | 094 | M13 | Gerenciamento de custo de inferência sob alto volume concorrente; Deploy em produção | mercado-8 |
| Quantificar a redução de custo acumulada por múltiplas alavancas de otimização | 094 | M13 | Gerenciamento de custo de inferência sob alto volume concorrente; Deploy em produção | mercado-8 |
| Explicar como um copiloto de IaC gera e valida configuração contra políticas | 095 | M14 | Deploy em produção | mercado-8 |
| Implementar detecção de anomalias robusta (AIOps) em Python puro | 095 | M14 | Deploy em produção | mercado-8 |
| Modelar um laço de troubleshooting estilo ReAct sobre uma base de conhecimento | 095 | M14 | Deploy em produção | mercado-8 |
| Implementar um scan de compliance que emite achados com severidade | 096 | M14 | Deploy em produção | mercado-8 |
| Projetar previsão de custo (FinOps) por ajuste linear sobre o histórico | 096 | M14 | Deploy em produção | mercado-8 |
| Combinar RAG sobre runbooks com auto-remediação protegida por guardrails | 096 | M14 | Deploy em produção | mercado-8 |
| Converter uma especificação textual de UI numa árvore de componentes (text-to-UI) | 097 | M14 | Desenvolvimento de aplicações LLM | mercado-8 |
| Gerar e pontuar variantes de layout na prototipação assistida | 097 | M14 | Desenvolvimento de aplicações LLM | mercado-8 |
| Validar fluxos de navegação por alcançabilidade em um grafo de telas | 097 | M14 | Desenvolvimento de aplicações LLM | mercado-8 |
| Priorizar backlog com scores RICE e WSJF de forma reprodutível | 098 | M14 | Construção de agentes | mercado-8 |
| Estimar prazos por simulação de Monte Carlo com percentis p50/p85 | 098 | M14 | Construção de agentes | mercado-8 |
| Agregar um backlog por MoSCoW e calcular progresso em um relatório | 098 | M14 | Construção de agentes | mercado-8 |
| Definir escopo e critérios de conclusão verificáveis por componente do Micro-SaaS | 099 | M15 | Engenharia de pipelines RAG; Construção de agentes; Desenvolvimento de aplicações LLM | mercado-8 |
| Modelar a arquitetura em camadas (cliente/servidor MCP → agente → RAG) e derivar a ordem de montagem | 099 | M15 | Engenharia de pipelines RAG; Construção de agentes; Desenvolvimento de aplicações LLM | mercado-8 |
| Especificar o contrato de evidência observável que torna a integração verificável | 099 | M15 | Engenharia de pipelines RAG; Construção de agentes; Desenvolvimento de aplicações LLM | mercado-8 |
| Implementar um RAG mínimo determinístico por similaridade de cosseno | 100 | M15 | Engenharia de pipelines RAG; Construção de agentes; Desenvolvimento de aplicações LLM | mercado-8 |
| Implementar um agente que seleciona e invoca ferramentas por política explícita | 100 | M15 | Engenharia de pipelines RAG; Construção de agentes; Desenvolvimento de aplicações LLM | mercado-8 |
| Integrar MCP + agente + RAG e verificar a conclusão por evidência observável | 100 | M15 | Engenharia de pipelines RAG; Construção de agentes; Desenvolvimento de aplicações LLM | mercado-8 |
| Caracterizar o papel do AI Engineer e diferenciá-lo de Data Scientist e ML Engineer | 101 | M16 | Desenvolvimento de aplicações LLM; Deploy em produção | mercado-8 |
| Mapear os níveis de senioridade (Junior a Principal) por autonomia, escopo e impacto | 101 | M16 | Desenvolvimento de aplicações LLM; Deploy em produção | mercado-8 |
| Avaliar e priorizar sinais de qualidade de um portfólio no GitHub | 101 | M16 | Desenvolvimento de aplicações LLM; Deploy em produção | mercado-8 |
| Responder questões de entrevista sobre viés-variância com argumentação quantitativa | 102 | M16 | Viés-variância; Calibração; Data leakage; Gradient explosion | ml-classico-4 |
| Diagnosticar má calibração calculando o ECE de previsões probabilísticas | 102 | M16 | Viés-variância; Calibração; Data leakage; Gradient explosion | ml-classico-4 |
| Identificar data leakage e explicar gradient descent/backprop em contexto de entrevista | 102 | M16 | Viés-variância; Calibração; Data leakage; Gradient explosion | ml-classico-4 |
| Avaliar um retriever de RAG calculando precision@k, recall@k e MRR | 103 | M16 | Engenharia de pipelines RAG; Construção de agentes; Frameworks de avaliação; Gerenciamento de custo de inferência sob alto volume concorrente | mercado-8 |
| Raciocinar sobre orçamento e parada de loops de agentes em entrevista | 103 | M16 | Engenharia de pipelines RAG; Construção de agentes; Frameworks de avaliação; Gerenciamento de custo de inferência sob alto volume concorrente | mercado-8 |
| Escolher arquiteturas de IA sob restrições de custo, latência e qualidade | 103 | M16 | Engenharia de pipelines RAG; Construção de agentes; Frameworks de avaliação; Gerenciamento de custo de inferência sob alto volume concorrente | mercado-8 |
| Resolver exercícios de live coding com strings e contagem usando estruturas adequadas | 104 | M16 | Desenvolvimento de aplicações LLM; Verificação de saídas | mercado-8 |
| Aplicar tabelas hash para reduzir complexidade de O(n²) para O(n) | 104 | M16 | Desenvolvimento de aplicações LLM; Verificação de saídas | mercado-8 |
| Implementar primitivas numéricas de ML (softmax estável, cosseno) corretamente | 104 | M16 | Desenvolvimento de aplicações LLM; Verificação de saídas | mercado-8 |

## Cobertura das exigências

Número de resultados de aprendizagem que entregam cada exigência:

| Exigência | Categoria | Nº de resultados |
|-----------|-----------|------------------|
| `req-llm-apps` | mercado-8 | 105 |
| `req-rag` | mercado-8 | 51 |
| `req-agentes` | mercado-8 | 60 |
| `req-prompt` | mercado-8 | 6 |
| `req-deploy-prod` | mercado-8 | 36 |
| `req-evals` | mercado-8 | 25 |
| `req-custo-inferencia` | mercado-8 | 21 |
| `req-verificacao-saidas` | mercado-8 | 30 |
| `req-vies-variancia` | ml-classico-4 | 66 |
| `req-calibracao` | ml-classico-4 | 14 |
| `req-data-leakage` | ml-classico-4 | 6 |
| `req-gradient-explosion` | ml-classico-4 | 15 |
