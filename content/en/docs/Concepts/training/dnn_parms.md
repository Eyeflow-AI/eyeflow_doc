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



### Classification Parameters

**Classification Specific Neural Network Parameters**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Component|choice ['class_cnn']|class_cnn|The DNN component for train model|
|Neural Network Depth|int [1 - ]|3|Depth (num layers) of Neural Network|
|Neural Network Width|int [5 - ]|20|Wide (num features) of Neural Network|
|Preprocess Mode|choice ['caffe', 'tf']|caffe|Function for image normalize|
|Loss Function|choice ['categorical_crossentropy', 'binary_crossentropy']|categorical_crossentropy|Loss function for use in training|
|Metrics Functions|Array of string|['categorical_accuracy']|Metrics functions for use in evaluation|
|Optimizer Function|choice ['adam']|adam|Optimizer function for use in training|




### ObjectDetection Parameters

**ObjectDetection Specific Neural Network Parameters**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Component|choice ['objdet', 'retinanet']|objdet|The DNN component for train model|
|Neural Network Width|int [5 - ]|20|Wide (num features) of Neural Network|
|Neural Network backbone|choice ['vgg7', 'vgg16', 'vgg19', 'resnet18', 'resnet34', 'resnet50', 'resnet101', 'resnet152', 'mobilenet128', 'mobilenet160', 'mobilenet192', 'mobilenet224', 'densenet121', 'densenet169', 'densenet201']|vgg7|Backbone architecture to Neural Network|
|Preprocess Mode|choice ['caffe', 'tf']|caffe|Function for image normalize|
|IoU negative overlap|number [0.05 - 1.0]|0.3|Value for minimum overlap of negative boxes|
|IoU positive overlap|number [0.05 - 1.0]|0.45|Value for minimum overlap of positive boxes|


#### Anchor parmeters

**Parameters for boxes anchors**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Boxes sizes|Array of integer|[12, 24, 48, 96, 192]|Size of boxes in each layer|
|Boxes strides|Array of integer|[8, 16, 32, 64, 128]|Strides of boxes in each layer|
|Boxes ratios|Array of number|[0.5, 1, 2]|Ratios (height / width) of candidate boxes|
|Boxes scales|Array of number|[1, 1.2, 1.5]|Scales of candidate boxes|






<!-- </parm_table> -->


## Para onde devo ir agora?

* [Dataset](/docs/concepts/dataset/): Anotando Datasets
* [Treinamento](/docs/concepts/training/): Treinando a rede neural
