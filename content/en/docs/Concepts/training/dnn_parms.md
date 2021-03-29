---
title: "Parâmetros das Redes Neurais"
linkTitle: "Parâmetros das Redes Neurais"
weight: 4
description: >
  Controle das redes neurais
---

<!-- <parm_table> -->


## Neural Network Parameters

**Parameters for Neural Network**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|


### Classification Parameters

**Classification Specific Neural Network Parameters**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Component|enum|||class_cnn|The DNN component for train model|
|Neural Network Depth|integer|1||3|Depth (num layers) of Neural Network|
|Neural Network Width|integer|5||20|Wide (num features) of Neural Network|
|Preprocess Mode|enum|||caffe|Function for image normalize|
|Loss Function|enum|||categorical_crossentropy|Loss function for use in training|
|Metrics Functions|array|||['categorical_accuracy']|Metrics functions for use in evaluation|
|Optimizer Function|enum|||adam|Optimizer function for use in training|




### ObjectDetection Parameters

**ObjectDetection Specific Neural Network Parameters**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Component|enum|||objdet|The DNN component for train model|
|Neural Network Width|integer|5||20|Wide (num features) of Neural Network|
|Neural Network backbone|enum|||vgg7|Backbone architecture to Neural Network|
|Preprocess Mode|enum|||caffe|Function for image normalize|
|IoU negative overlap|number|0.05|1.0|0.3|Value for minimum overlap of negative boxes|
|IoU positive overlap|number|0.05|1.0|0.45|Value for minimum overlap of positive boxes|


#### Anchor parmeters

**Parameters for boxes anchors**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Boxes sizes|array|||[12, 24, 48, 96, 192]|Size of boxes in each layer|
|Boxes strides|array|||[8, 16, 32, 64, 128]|Strides of boxes in each layer|
|Boxes ratios|array|||[0.5, 1, 2]|Ratios (height / width) of candidate boxes|
|Boxes scales|array|||[1, 1.2, 1.5]|Scales of candidate boxes|






<!-- </parm_table> -->


## Para onde devo ir agora?

* [Dataset](/docs/concepts/dataset/): Anotando Datasets
* [Treinamento](/docs/concepts/training/): Treinando a rede neural
