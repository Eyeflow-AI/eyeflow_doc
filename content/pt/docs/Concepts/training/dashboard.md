---
title: "Dashboard de Treinamento"
linkTitle: "Dashboard de Treinamento"
weight: 2
description: >
  Visão geral dos treinamentos
---

O Dashboard de Treinamentos dá uma visão geral de todo processo de treinamento. Nessa tela podemos acompanhar os
treinamentos em tempo real, bem como avaliar o histórico dos treinamentos anteriores e editar vários parâmetros.

![Visão Geral](/screenshots/pt-br_dashboard_overview.jpg#bordered "Visão Geral")

## Indicadores
Nesses quadros estão os indicadores do treinamento selecionado. A data que foi realizado, duração, e resultados
finais do treino.
Temos também uma barra de botões com ações como *Download* e *Publicação* do modelo, visualização dos parâmetros
e visualização das imagens de teste.

![Indicadores](/screenshots/pt-br_dashboard_kpis.jpg#bordered "Indicadores")

### Resultados finais do treino
![Resultados Finais](/screenshots/pt-br_dashboard_final_results.jpg#bordered "Resultados Finais")

### Imagem de teste de expansão de exemplos - Data Augmentation
![Teste de Expansão](/screenshots/pt-br_dashboard_test_augmentation.jpg#bordered "Teste de Expansão")

### Imagem de teste do final do treino
![Teste Final](/screenshots/pt-br_dashboard_test_final.jpg#bordered "Teste Final")

## Gráficos
Os gráficos dão uma ideia da progressão do treino, seja em tempo real ou histórico.

**Loss** e **Val Loss** indicam o erro medido no treino, e são indicadores comuns a todos os treinos. Devem ser curvas
descendentes que se aproximam de 0. Quanto menor o Loss menos a rede neural está errando.

![Gráficos](/screenshots/pt-br_dashboard_graphs.jpg#bordered "Gráficos")

Existem também gráficos de eficácia da rede neural, e para esses quanto maior melhor.
- **mAP** para datasets *ObjectDetection*. Geralmente já é considerado bom acima de 0.6.
- **Accuracy** para datasets de *Classification*. É considerado bom acima de 90%.

## Histórico de Treinamentos
É possível também verificar os treinamentos anteriores e assim ter insights sobre se as ações que foram tomadas na
construção do dataset e parametrização dos treinos surtiram efeitos positivos ou negativos.

![Histórico](/screenshots/pt-br_dashboard_history.jpg#bordered "Histórico")


## Para onde devo ir agora?

* [Dataset](/docs/concepts/dataset/): Anotando Datasets
* [Treinamento](/docs/concepts/training/): Treinando a rede neural
