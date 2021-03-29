---
title: "Parâmetros do Treinamento"
linkTitle: "Parâmetros do Treinamento"
weight: 3
description: >
  Controle do treinamento
---

## Iterações
O processo de treinamento é iterativo, ou seja, realizado em ciclos. Cada ciclo é chamado de **Época**.
Em cada época todos os exemplos são apresentados para a rede neural, para que sejam aprendidos os padrões. O
algoritmo de treinamento vai então medindo o erro (*Loss*) e ajustando a rede neural para ir minizando o mesmo.

É comum se pensar de que com mais épocas a rede irá aprender mais, mas na prática não é exatamente assim. De acordo
com a quantidade/qualidade dos exemplos chega-se a um ponto em que o erro não diminui mais e o aprendizado estagna. Outra
ocorrência comum é o erro (*Loss*) continuar diminuindo, mas o *Val Loss* começar a aumentar. Esse fenômeno é conhecido
como *Overfitting* e significa que a rede neural ficou viciada nos exemplos do treinamento e não está mais conseguindo
generalizar para novos exemplos.

A recomendação é no início setar 5 épocas para o treino enquanto o dataset tiver menos de 100 exemplos, e daí ir subindo.

<!-- <parm_table> -->


## Parâmetros de treinamento

**Parâmetros para treinamento de rede neural**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Épocas|integer|1||5|Número de épocas para treinamento|
|Etapas por época|integer|50||100|Número de passos para treinamento em cada época|
|Tamanho do lote|integer|1|64|10|Número de exemplos em cada passo|
|Tamanho do Val|number|0.01|0.9|0.1|Porcentagem de exemplos selecionados para validação|
|Tamanho do Teste|number|0.01|0.9|0.1|Porcentagem de exemplos selecionados para o teste final|
|Limiar de confiança|number|0.05|1.0|0.6|Limite mínimo de confiança para detecção válida|
|Limite de detecção de IoU|number|0.05|1.0|0.45|Limite mínimo para detecção de IoU|
|Máximo de caixas|integer|0|300|30|Número máximo de caixas em detecção|
|Caixas de expansão|number|0|2|0|Porcentagem para expandir o tamanho das caixas na detecção|


### Resolução de entrada

**Dimensões da imagem de entrada**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Lado mínimo|integer|20||50|Tamanho do lado menor|
|Lado máximo|integer|20||80|Tamanho do lado maior|
|Canais|enum|||1|Canais de cor|




### Parâmetros do Otimizador

**Parâmetros para Train Optimizer**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|beta_2|number|0.1|1.0|0.999|Beta 2|
|beta_1|number|0.1|1.0|0.9|Beta 1|
|Taxa de Aprendizagem|number|1e-06|0.1|0.001|Taxa de aprendizagem do otimizador|
|amsgrad|boolean|||False|amsgrad|




### Parada Antecipada

**Parada antecipada para treinamento**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Paciência|integer|1||5|Número de épocas para esperar pelo progresso|
|Variável de monitoramento|enum|||val_loss|Variável para monitorar o progresso|
|Delta Mínimo|number|0||0.01|A variação mínima na variável|
|Modo de avaliação|enum|||max|Monitor do decréscimo ou incremento do valor da variável|




### Reduzir LR no platô

**Reduza a taxa de aprendizagem no platô**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Paciência|integer|1||4|Número de épocas para esperar pelo progresso|
|Variável de monitoramento|enum|||val_loss|Variável para monitorar o progresso|
|Delta Mínimo|number|0||0.01|A variação mínima na variável|
|Fator de redução|number|0.1|0.9|0.5|Quantidade a reduzir|
|Esfriar|number|0||0|Esfriar|




### Salvar ponto de verificação

**Gatilho para salvar o progresso do treinamento do modelo**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Variável de monitoramento|enum|||val_loss|Variável para monitorar para salvar|
|Modo de avaliação|enum|||min|Salvar ao diminuir ou aumentar o valor da variável|




<!-- </parm_table> -->

## Para onde devo ir agora?

* [Parâmetros de Treinamento](/docs/concepts/training/train_parms): Parâmetros gerais para treinamento da rede neural
* [Parâmetros de Redes Neurais](/docs/concepts/training/dnn_parms): Parâmetros específicos da rede neural
* [Parâmetros de Expansão de Dados](/docs/concepts/training/data_augmentation_parms): Parâmetros para expansão de dados - Data Augmentation
