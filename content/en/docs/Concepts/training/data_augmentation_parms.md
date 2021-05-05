---
title: "Data Augmentation"
linkTitle: "Data Augmentation"
weight: 5
description: >
 Expanding training examples
---

For a good result in neural network training, the rule is to present a large number of different examples so that the neural network can learn the pattern in the data. However, getting and writing down thousands of examples is an arduous and time-consuming task, and can consume hundreds of hours of a project.

To facilitate this process, Eyeflow.AI offers an extensive range of Data Expansion algorithms (*Data Augmentation*). It is about inserting disturbances in the images when they are being presented to the neural network in training, thus forcing the neural network to learn to recognize the patterns, without depending only on the static examples that exist in the dataset.

These are several changes such as:
- Changes in optics such as brightness, contrast, color, gamma
- Changes in the way rotations, deformations, positions
- Changes in quality such as blur and noise

{{< tooltip >}}
The changes in the images cannot be so high that the object of interest can no longer be recognized. For this, Eyeflow.AI provides an example of these changes for the operator to verify that the changes are not exaggerated. What cannot be seen in these examples, cannot be learned by the neural network.
{{< /tooltip >}}

{{< tooltip >}}
It is also useless to stress the changes and generate cases that do not happen in the real operation. It is useless to present an inverted image for the learning of the neural network, upside down, for example, if in real operation this situation will never happen.
{{< /tooltip >}}

<!-- <parm_table> -->


## Data augmentation parameters

**Parameters for Images Data Augmentation**



### Data augmentation general parameters

**General Parameters for all transformations**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Interpolation|choice ['linear', 'nearest', 'cubic', 'area', 'lanczos4']|linear|Interpolation for resize operations|
|Fill Mode|choice ['constant', 'nearest', 'reflect', 'wrap']|constant|Fill of null regions|
|Border Value|int [0 - 255]|0|The color to fill border regions|




### Rotate image

**Random rotation of image**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Probability|percent 0% - 100%|0.3|Probability of random rotation|
|Random Rotation|range from -90 to 90]|-20 to 20|Random rotation of image|
|Rescale image|bool [True - False]|True|If image must be reescaled in rotation|




### Translate image

**Random translation of image**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Probability|percent 0% - 100%|0.3|Probability of random translation|
|Horizontal translation|range from -0.4 to 0.4]|-0.2 to 0.2|Minimum & Maximum for horizontal translation|
|Vertical translation|range from -0.4 to 0.4]|-0.2 to 0.2|Minimum & Maximum for vertical translation|
|Number of trials|int [1 - 6]|3|Maximum number of trials without degeneration boxes|




### Shear image

**Random shear deformation of image**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Probability|percent 0% - 100%|0.3|Probability of random shear|
|Shear image|range from -60 to 60]|-10 to 10|Random shear deformation of image|




### Scale image

**Random scale of image**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Probability|percent 0% - 100%|0.3|Probability of random scale|
|Scale image|range from 0.4 to 1.6]|0.8 to 1.2|Random scale of image|




### Random flip of image

**Flip Parameters**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Horizontal flip of image|percent 0% - 100%|0.3|Random horizontal flip of image|
|Vertical flip of image|percent 0% - 100%|0.3|Random vertical flip of image|




### Random contrast

**Random changes in contrast of image**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Probability|percent 0% - 100%|0.3|Probability of random contrast|
|Random contrast|range from 0.4 to 2]|0.8 to 1.2|Random changes in contrast of image|




### Random brightness

**Random changes in brightness of image**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Probability|percent 0% - 100%|0.3|Probability of random brightness|
|Random brightness|range from -0.6 to 0.6]|-0.2 to 0.3|Random changes in brightness of image|




### Random gamma

**Random changes in gamma of image**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Probability|percent 0% - 100%|0.3|Probability of random gamma|
|Random gamma|range from 0.1 to 12]|0.4 to 1.6|Random changes in gamma of image|




### Random saturation

**Random changes in saturation of image**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Probability|percent 0% - 100%|0.3|Probability of random saturation|
|Random saturation|range from 0.1 to 2]|0.5 to 1.5|Random changes in saturation of image|




### Random hue

**Random changes in hue of image**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Probability|percent 0% - 100%|0.3|Probability of random hue|
|Random hue|range from -1 to 1]|-0.05 to 0.05|Random changes in hue of image|




### Random noise

**Random insert of noise of image**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Probability|percent 0% - 100%|0.3|Probability of random noise|
|Noise method|choice ['gauss', 'poisson', 'speckle']|gauss|Method for noise insertion|




### Blur

**Random blur of image**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Probability|percent 0% - 100%|0.3|Probability of random blur|
|Kernel size|choice [3, 5, 7, 9]|5|The size of kernel to blur image|




<!-- </parm_table> -->


## Where should I go now?

* [Training Parameters](/docs/concepts/training/train_parms)
* [Parameters of Neural Networks](/docs/concepts/training/dnn_parms)
* [Data Expansion Parameters](/docs/concepts/training/data_augmentation_parms)
