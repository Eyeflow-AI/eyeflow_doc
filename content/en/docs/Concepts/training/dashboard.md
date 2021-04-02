---
title: "Training Dashboard"
linkTitle: "Training Dashboard"
weight: 2
description: >
 Training overview
---

The Training Dashboard gives an overview of the entire training process. On this screen we can monitor the training in real time, as well as evaluate the history of previous training and edit various parameters.

![Overview](/screenshots/pt-br_dashboard_overview.jpg#bordered "Visão Geral")

## Indicators
In these tables are the indicators of the selected training. The date that was performed, duration, and final results of the training. We also have a button bar with actions such as *Download*and* Publication * of the model, visualization of parameters and visualization of test images.

![Indicators](/screenshots/pt-br_dashboard_kpis.jpg#bordered "Indicadores")

### Final training results
![Resultados Finais](/screenshots/pt-br_dashboard_final_results.jpg#bordered "Resultados Finais")
### Sample expansion test image - Data Augmentation
![Teste de Expansão](/screenshots/pt-br_dashboard_test_augmentation.jpg#bordered "Teste de Expansão")
### End of training test image
![Teste Final](/screenshots/pt-br_dashboard_test_final.jpg#bordered "Teste Final")
## Graphics
The graphs give an idea of the training progression, either in real time or in history.

**Loss**and**Val Loss** indicate the error measured in the training, and are common indicators for all training. They must be descending curves that approach 0. The lower the Loss, the less the neural network is missing.

![Graphics](/screenshots/pt-br_dashboard_graphs.jpg#bordered "Gráficos")

There are also graphs of neural network efficacy, and for these, the bigger the better.
- **mAP**for*ObjectDetection* datasets. It is generally considered good above 0.6.
- **Accuracy**for*Classification* datasets. It is considered good above 90%.

## Training History
It is also possible to check the previous trainings and thus have insights on whether the actions that were taken in the construction of the dataset and parameterization of the training had positive or negative effects.

![Histórico](/screenshots/pt-br_dashboard_history.jpg#bordered "Histórico")


## Where should I go now?

* [Dataset](/docs/concepts/dataset/)
* [Training](/docs/concepts/training/)
