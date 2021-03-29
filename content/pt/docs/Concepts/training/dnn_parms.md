---
title: "Parâmetros das Redes Neurais"
linkTitle: "Parâmetros das Redes Neurais"
weight: 4
description: >
  Controle das redes neurais
---

<!-- <parm_table> -->


## Parâmetros de rede neural

**Parâmetros para rede neural**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|


### Parâmetros de Classificação

**Parâmetros de rede neural específicos de classificação**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Componente|enum|||class_cnn|O componente DNN para o modelo de treinamento|
|Profundidade da Rede Neural|integer|1||3|Profundidade (núm camadas) da rede neural|
|Largura da rede neural|integer|5||20|Largura (núm features) da Rede Neural|
|Modo de pré-processamento|enum|||caffe|Função para normalizar imagem|
|Função de perda|enum|||categorical_crossentropy|Função de perda para uso em treinamento|
|Funções de métricas|array|||['categorical_accuracy']|Funções de métricas para uso em avaliação|
|Função Otimizador|enum|||adam|Funções de métricas para uso em avaliação|




### Parâmetros ObjectDetection

**Parâmetros de rede neural específicos de detecção de objeto**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Componente|enum|||objdet|O componente DNN para o modelo de treinamento|
|Largura da rede neural|integer|5||20|Largura (núm features) da Rede Neural|
|Backbone de rede neural|enum|||vgg7|Arquitetura de backbone para rede neural|
|Modo de pré-processamento|enum|||caffe|Função para normalizar imagem|
|Sobreposição negativa IoU|number|0.05|1.0|0.3|Valor para sobreposição mínima de caixas negativas|
|Sobreposição positiva IoU|number|0.05|1.0|0.45|Valor para sobreposição mínima de caixas positivas|


#### Parâmetros de âncora

**Parâmetros para âncoras de caixas**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Tamanhos de caixas|array|||[12, 24, 48, 96, 192]|Tamanho das caixas em cada camada|
|Boxes strides|array|||[8, 16, 32, 64, 128]|Strides de caixas em cada camada|
|Razões das caixas|array|||[0.5, 1, 2]|Proporções (altura / largura) das caixas candidatas|
|Escalas de caixas|array|||[1, 1.2, 1.5]|Escalas de caixas candidatas|






<!-- </parm_table> -->


## Para onde devo ir agora?

* [Parâmetros de Treinamento](/docs/concepts/training/train_parms): Parâmetros gerais para treinamento da rede neural
* [Parâmetros de Redes Neurais](/docs/concepts/training/dnn_parms): Parâmetros específicos da rede neural
* [Parâmetros de Expansão de Dados](/docs/concepts/training/data_augmentation_parms): Parâmetros para expansão de dados - Data Augmentation
