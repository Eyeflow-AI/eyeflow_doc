---
title: "Data Augmentation"
linkTitle: "Data Augmentation"
weight: 5
description: >
  Expansão de exemplos nos treinamentos
---


<!-- <parm_table> -->


## Parâmetros para expansão de dataset

**Parâmetros para expansão de dataset**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Interpolação|enum|||linear|Interpolação para operações de redimensionamento|
|Modo de Preenchimento|enum|||constant|Preenchimento de regiões nulas|
|Valor da borda|integer|0|255|0|A cor para preencher as regiões limítrofes|
|Virada horizontal da imagem|number|0|1.0|0.3|Virada horizontal aleatória da imagem|
|Virada vertical da imagem|number|0|1.0|0.3|Virada vertical aleatória da imagem|


### Rotacionar imagem

**Rotação aleatória da imagem**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Probabilidade|number|0|1.0|0.3|Probabilidade de rotação aleatória|
|Ângulo máximo|number|0|180|60|Ângulo máximo para rotação no sentido horário|
|Angulo minimo|number|-180|0|-60|Ângulo mínimo para rotação no sentido anti-horário|
|Redimensionar imagem|boolean|||True|Se a imagem deve ser redimensionada em rotação|




### Transladar imagem

**Translação aleatória de imagem**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Probabilidade|number|0|1.0|0.3|Probabilidade de mudança de translação|
|Translação horizontal|array|||[0.03, 0.2]|Mín. E Máx. Para translação horizontal|
|Translação vertical|array|||[0.03, 0.2]|Mín. E Máx. Para translação vertical|
|Número de Tentativas|integer|1||3|Número máximo de tentativas sem degenerar caixas|




### Cortar imagem

**Deformação por cisalhamento aleatório da imagem**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Probabilidade|number|0|1.0|0.3|Probabilidade de mudança de cisalhamento|
|Mínimo de cisalhamento|number|-180|0|-10|Valor mínimo para ângulo de cisalhamento em graus|
|Cisalhamento máximo|number|0|180|10|Valor máximo para ângulo de cisalhamento em graus|




### Imagem em escala

**Escala aleatória da imagem**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Probabilidade|number|0|1.0|0.3|Probabilidade de escala aleatória|
|Escala mínima|number|0.1||0.8|Valor de proporção mínima para escala|
|Escala máxima|number|1.0||1.2|Valor de proporção máxima para escala|




### Contraste aleatório

**Mudanças aleatórias no contraste da imagem**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Probabilidade|number|0|1.0|0.3|Probabilidade de mudança de contraste|
|Contraste mínimo|number|0.1|1.0|0.8|Mudança mínima de contraste|
|Contraste máximo|number|1.0|2.0|1.2|Mudança máxima de contraste|




### Brilho aleatório

**Mudanças aleatórias no brilho da imagem**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Probabilidade|number|0|1.0|0.3|Probabilidade de mudança de brilho|
|Brilho mínimo|number|-1.0|0|-0.2|Mudança mínima de brilho|
|Brilho máximo|number|0|1.0|0.3|Mudança máxima de brilho|




### Gama aleatória

**Mudanças aleatórias na gama da imagem**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Probabilidade|number|0|1.0|0.3|Probabilidade de gama aleatória|
|Gama mínima|number|0.1|1.0|0.4|Mudança mínima de gama|
|Gama máxima|number|0|12.0|1.6|Mudança máxima de gama|




### Saturação aleatória

**Mudanças aleatórias na saturação da imagem**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Probabilidade|number|0|1.0|0.3|Probabilidade de mudança de saturação|
|Saturação mínima|number|0.1|1.0|0.95|Mudança de saturação mínima|
|Saturação máxima|number|1.0|2.0|1.05|Mudança máxima de saturação|




### Matiz aleatório

**Mudanças aleatórias no matiz da imagem**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Probabilidade|number|0|1.0|0.3|Probabilidade de matiz aleatório|
|Matiz mínimo|number|-1.0|0|-0.05|Mudança mínima de matiz|
|Matiz máximo|number|0|1.0|0.05|Mudança máxima de matiz|




### Ruído aleatório

**Inserção aleatória de ruído de imagem**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Probabilidade|number|0|1.0|0.3|Probabilidade de inserção de ruído|
|Método de ruído|enum|||gauss|Método para inserção de ruído|




### Desfoque aleatório

**Desfoque aleatório da imagem**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Probabilidade|number|0|1.0|0.3|Probabilidade de desfoque aleatório|
|Tamanho do kernel|enum|||5|O tamanho do kernel para desfocar a imagem|




<!-- </parm_table> -->


## Para onde devo ir agora?

* [Parâmetros de Treinamento](/docs/concepts/training/train_parms): Parâmetros gerais para treinamento da rede neural
* [Parâmetros de Redes Neurais](/docs/concepts/training/dnn_parms): Parâmetros específicos da rede neural
* [Parâmetros de Expansão de Dados](/docs/concepts/training/data_augmentation_parms): Parâmetros para expansão de dados - Data Augmentation
