---
title: "Parâmetros das Redes Neurais"
linkTitle: "Parâmetros das Redes Neurais"
weight: 4
description: >
  Controle das redes neurais
---

Nesse conjunto de parâmetros são controlados os aspectos relacionados à arquitetura das redes neurais que irão
aprender com os exemplos do dataset no treinamento.

Cada tipo de rede neural tem sua própria arquitetura, parâmetros peso e performance. O Eyeflow.AI é uma plataforma
extensível, que permite se trabalhar com as mais diversas arquiteturas. Entretanto, nossa experiência de vários
projetos já nos ensinou sobre várias arquiteturas que funcionam bem em produção, e é essa experiência que
buscamos trazer para a plataforma, e assim simplificar a vida dos usuários.

Nessa fase Beta temos 2 principais componentes que usamos para solucionar todos os problemas que temos encontrado.

<!-- <parm_table> -->


## Parâmetros de rede neural

**Parâmetros para rede neural**



### Parâmetros de Classificação

**Parâmetros de rede neural específicos de classificação**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Componente|choice ['class_cnn']|class_cnn|O componente DNN para o modelo de treinamento|
|Profundidade da Rede Neural|int [1 - ]|3|Profundidade (núm camadas) da rede neural|
|Largura da rede neural|int [5 - ]|20|Largura (núm features) da Rede Neural|
|Modo de pré-processamento|choice ['caffe', 'tf']|caffe|Função para normalizar imagem|
|Função de perda|choice ['categorical_crossentropy', 'binary_crossentropy']|categorical_crossentropy|Função de perda para uso em treinamento|
|Funções de métricas|Array of string|['categorical_accuracy']|Funções de métricas para uso em avaliação|
|Função Otimizador|choice ['adam']|adam|Funções de métricas para uso em avaliação|




### Parâmetros ObjectDetection

**Parâmetros de rede neural específicos de detecção de objeto**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Componente|choice ['objdet', 'retinanet']|objdet|O componente DNN para o modelo de treinamento|
|Largura da rede neural|int [5 - ]|20|Largura (núm features) da Rede Neural|
|Backbone de rede neural|choice ['vgg7', 'vgg16', 'vgg19', 'resnet18', 'resnet34', 'resnet50', 'resnet101', 'resnet152', 'mobilenet128', 'mobilenet160', 'mobilenet192', 'mobilenet224', 'densenet121', 'densenet169', 'densenet201']|vgg7|Arquitetura de backbone para rede neural|
|Modo de pré-processamento|choice ['caffe', 'tf']|caffe|Função para normalizar imagem|
|Sobreposição negativa IoU|number [0.05 - 1.0]|0.3|Valor para sobreposição mínima de caixas negativas|
|Sobreposição positiva IoU|number [0.05 - 1.0]|0.45|Valor para sobreposição mínima de caixas positivas|


#### Parâmetros de âncora

**Parâmetros para âncoras de caixas**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Tamanhos de caixas|Array of integer|[12, 24, 48, 96, 192]|Tamanho das caixas em cada camada|
|Boxes strides|Array of integer|[8, 16, 32, 64, 128]|Strides de caixas em cada camada|
|Razões das caixas|Array of number|[0.5, 1, 2]|Proporções (altura / largura) das caixas candidatas|
|Escalas de caixas|Array of number|[1, 1.2, 1.5]|Escalas de caixas candidatas|






<!-- </parm_table> -->


## Para onde devo ir agora?

* [Parâmetros de Treinamento](/docs/concepts/training/train_parms): Parâmetros gerais para treinamento da rede neural
* [Parâmetros de Redes Neurais](/docs/concepts/training/dnn_parms): Parâmetros específicos da rede neural
* [Parâmetros de Expansão de Dados](/docs/concepts/training/data_augmentation_parms): Parâmetros para expansão de dados - Data Augmentation
