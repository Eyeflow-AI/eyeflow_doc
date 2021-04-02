---
title: "Training Parameters"
linkTitle: "Training Parameters"
weight: 3
description: >
 Training control
---

## Iterations
The training process is iterative, that is, carried out in cycles. Each cycle is called **Season**. In each epoch all examples are presented for the neural network, so that the patterns are learned. The training algorithm will then measure the error (*Loss*) and adjust the neural network to minimize it.

It is common to think that with more times the network will learn more, but in practice it is not exactly like that. Depending on the quantity / quality of the examples, a point is reached where the error no longer decreases and learning stagnates. Another common occurrence is that the error (*Loss*) continues to decrease, but the *Val Loss*starts to increase. This phenomenon is known as* Overfitting * and it means that the neural network has become addicted to the training examples and is no longer able to generalize to new examples.

The recommendation is to set 5 training periods in the beginning while the dataset has less than 100 examples, and then go up.

In the sequence, we have several other parameters that govern the training process and all can influence positively or negatively on the final result of the network learning. Do not be frightened by the quantity, nor by the complexity of them, it is natural to take a long time to acquire mastery over the whole process.

Rest assured, Eyeflow.AI has a great set of defaults for the parameters that solve the needs of most of the needs. In addition, our team is available to answer questions and give tips in our Forum.

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

## Where should I go now?

* [Training Parameters](/docs/concepts/training/train_parms)
* [Parameters of Neural Networks](/docs/concepts/training/dnn_parms)
* [Data Expansion Parameters](/docs/concepts/training/data_augmentation_parms)
