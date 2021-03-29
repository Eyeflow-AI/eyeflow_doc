---
title: "Data Augmentation"
linkTitle: "Data Augmentation"
weight: 5
description: >
  Expansão de exemplos nos treinamentos
---

<!-- <parm_table> -->


## Data augmentation parameters

**Parameters for Images Data Augmentation**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Interpolation|enum|||linear|Interpolation for resize operations|
|Fill Mode|enum|||constant|Fill of null regions|
|Border Value|integer|0|255|0|The color to fill border regions|
|Horizontal flip of image|number|0|1.0|0.3|Random horizontal flip of image|
|Vertical flip of image|number|0|1.0|0.3|Random vertical flip of image|


### Rotate image

**Random rotation of image**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Probability|number|0|1.0|0.3|Probability of random rotation|
|Maximum angle|number|0|180|60|Maximum angle for rotation clockwise|
|Minimum angle|number|-180|0|-60|Minimum angle for rotation counter-clockwise|
|Rescale image|boolean|||True|If image must be reescaled in rotation|




### Translate image

**Random translation of image**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Probability|number|0|1.0|0.3|Probability of random translation|
|Horizontal translation|array|||[0.03, 0.2]|Minimum & Maximum for horizontal translation|
|Vertical translation|array|||[0.03, 0.2]|Minimum & Maximum for vertical translation|
|Number of trials|integer|1||3|Maximum number of trials without degeneration boxes|




### Shear image

**Random shear deformation of image**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Probability|number|0|1.0|0.3|Probability of random shear|
|Shear Minimum|number|-180|0|-10|Minimum value for shear angle in degrees|
|Shear Maximum|number|0|180|10|Maximum value for shear angle in degrees|




### Scale image

**Random scale of image**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Probability|number|0|1.0|0.3|Probability of random scale|
|Minimum scale|number|0.1||0.8|Minimum proportion value for scale|
|Maximum scale|number|1.0||1.2|Maximum proportion value for scale|




### Random contrast

**Random changes in contrast of image**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Probability|number|0|1.0|0.3|Probability of random contrast|
|Minimum contrast|number|0.1|1.0|0.8|Minimum contrast change|
|Maximum contrast|number|1.0|2.0|1.2|Maximum contrast change|




### Random brightness

**Random changes in brightness of image**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Probability|number|0|1.0|0.3|Probability of random brightness|
|Minimum brightness|number|-1.0|0|-0.2|Minimum brightness change|
|Maximum brightness|number|0|1.0|0.3|Maximum brightness change|




### Random gamma

**Random changes in gamma of image**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Probability|number|0|1.0|0.3|Probability of random gamma|
|Minimum gamma|number|0.1|1.0|0.4|Minimum gamma change|
|Maximum gamma|number|0|12.0|1.6|Maximum gamma change|




### Random saturation

**Random changes in saturation of image**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Probability|number|0|1.0|0.3|Probability of random saturation|
|Minimum saturation|number|0.1|1.0|0.95|Minimum saturation change|
|Maximum saturation|number|1.0|2.0|1.05|Maximum saturation change|




### Random hue

**Random changes in hue of image**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Probability|number|0|1.0|0.3|Probability of random hue|
|Minimum hue|number|-1.0|0|-0.05|Minimum hue change|
|Maximum hue|number|0|1.0|0.05|Maximum hue change|




### Random noise

**Random insert of noise of image**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Probability|number|0|1.0|0.3|Probability of random noise|
|Noise method|enum|||gauss|Method for noise insertion|




### Random blur

**Random blur of image**

|Parameter|type|Min|Max|Default|Description|
|---------|----|---|---|-------|-----------|
|Probability|number|0|1.0|0.3|Probability of random blur|
|Kernel size|enum|||5|The size of kernel to blur image|




<!-- </parm_table> -->


## Para onde devo ir agora?

* [Dataset](/docs/concepts/dataset/): Anotando Datasets
* [Treinamento](/docs/concepts/training/): Treinando a rede neural
