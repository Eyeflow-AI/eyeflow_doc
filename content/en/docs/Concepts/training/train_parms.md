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


## Train Parameters

**Parameters for Neural Network Training**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Epochs|int [1 - ]|5|Number of epochs for training|
|Steps per Epoch|int [50 - ]|100|Number of Steps for training in each Epoch|
|Batch Size|int [1 - 64]|10|Number of examples in each step|
|Val Size|number [0.01 - 0.9]|0.1|Percent of examples selected for Validation|
|Test Size|number [0.01 - 0.9]|0.1|Percent of examples selected for Final Test|
|Confidence Threshold|number [0.05 - 1.0]|0.6|Minimum confidence threshold for valid detection|
|IoU Detection Threshold|number [0.05 - 1.0]|0.45|Minimum threshold for IoU detection|
|Maximum Boxes|int [0 - 300]|30|Maximum number of boxes in detection|
|Expand Boxes|number [0 - 2]|0|Percent to expand size of boxes in detection|


### Input Resolution

**Input image dimensions**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Minimum Side|int [20 - ]|50|Size of the smaller side|
|Maximum Side|int [20 - ]|80|Size of the bigger side|
|Channels|choice [1, 3]|1|Color channels|




### Optimizer Parameters

**Parameters for Train Optimizer**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|beta_2|number [0.1 - 1.0]|0.999|Beta 2|
|beta_1|number [0.1 - 1.0]|0.9|Beta 1|
|Learning Rate|number [1e-06 - 0.1]|0.001|Optimizer Learning Rate|
|amsgrad|bool [True - False]|False|AMSGrad|




### Early Stopping

**Early stopping for training**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Patience|int [1 - ]|5|Num of epochs to wait for progress|
|Monitor variable|choice ['val_loss', 'loss', 'categorical_accuracy', 'val_categorical_accuracy']|val_loss|Variable to monitor progress|
|Minimum Delta|number [0 - ]|0.01|The minimum variantion in variable|
|Evaluation mode|choice ['min', 'max', 'auto']|max|Monitor decrement or increment of variable value|




### Reduce LR on plateau

**Reduce Learning Rate on plateau**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Patience|int [1 - ]|4|Num of epochs to wait for progress|
|Monitor variable|choice ['val_loss', 'loss', 'categorical_accuracy', 'val_categorical_accuracy']|val_loss|Variable to monitor for progress|
|Minimum Delta|number [0 - ]|0.01|The minimum variantion in variable|
|Reducing factor|number [0.1 - 0.9]|0.5|Ammount to reduce|
|Cooldown|number [0 - ]|0|Cool Down|




### Save Checkpoint

**Trigger to save model training progress**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Monitor variable|choice ['val_loss', 'loss', 'categorical_accuracy', 'val_categorical_accuracy']|val_loss|Variable to monitor for saving|
|Evaluation mode|choice ['min', 'max', 'auto']|min|Save on decrement or increment of variable value|




<!-- </parm_table> -->

## Para onde devo ir agora?

* [Dataset](/docs/concepts/dataset/): Anotando Datasets
* [Treinamento](/docs/concepts/training/): Treinando a rede neural
