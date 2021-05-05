---
title: "Data Augmentation"
linkTitle: "Data Augmentation"
weight: 5
description: >
  Expansão de exemplos nos treinamentos
---

Para um bom resultado em um treinamento de redes neurais a regra é apresentar um grande número de exemplos diferentes
para que a rede neural possa aprender o padrão nos dados.
Porém, conseguir e anotar milhares de exemplos é uma tarefa árdua e demorada, podendo consumir centenas de horas de um
projeto.

Para facilitar esse processo o Eyeflow.AI oferece uma extensa gama de algorítmos de Expansão de Dados (*Data Augmentation*).
Trata-se de inserir perturbações nas imagens na hora em que estão sendo apresentadas para a rede neural no treinamento,
forçando assim que a rede neural aprenda a reconhecer os padrões, sem ficar dependendo somente dos exemplos estáticos
que existem no dataset.

Trata-se de alterações diversas como:
- Alterações na óptica como brilho, contraste, cor, gama
- Alterações na forma como rotações, deformações, posições
- Alterações na qualidade como desfoque e ruído

{{< tooltip >}}
As alterações nas imagens não podem ser muito altas a ponto de o objeto de interesse não poder ser mais reconhecido.
Para isso o Eyeflow.AI disponibiliza um exemplo dessas alterações para que o operador verifique se as alterações não
estão exageradas. O que não puder ser visto nesses exemplos, não poderá ser aprendido pela rede neural.
{{< /tooltip >}}

{{< tooltip >}}
Também não adianta estressar as mudanças e gerar casos que não acontecem na operação real.
De nada adianta apresentar pro aprendizado da rede neural uma imagem invertida, de cabeça para baixo, por exemplo, se
na operação real essa situação nunca irá acontecer.
{{< /tooltip >}}

<!-- <parm_table> -->


## Parâmetros para expansão de dataset

**Parâmetros para expansão de dataset**



### Parâmetros gerais de aumento de dados

**Parâmetros gerais para todas as transformações**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Interpolação|choice ['linear', 'nearest', 'cubic', 'area', 'lanczos4']|linear|Interpolação para operações de redimensionamento|
|Modo de Preenchimento|choice ['constant', 'nearest', 'reflect', 'wrap']|constant|Preenchimento de regiões nulas|
|Valor da borda|int [0 - 255]|0|A cor para preencher as regiões limítrofes|




### Rotacionar imagem

**Rotação aleatória da imagem**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Probabilidade|percent 0% - 100%|0.3|Probabilidade de rotação aleatória|
|Ângulo mínimo e máximo para rotação|range from -90 to 90|-20 to 20|Rotação aleatória da imagem|
|Redimensionar imagem|bool [True - False]|True|Se a imagem deve ser redimensionada em rotação|




### Transladar imagem

**Translação aleatória de imagem**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Probabilidade|percent 0% - 100%|0.3|Probabilidade de mudança de translação|
|Translação horizontal|range from -0.4 to 0.4|-0.2 to 0.2|mín. e máx. Para translação horizontal|
|Tradução vertical mínima e máxima|range from -0.4 to 0.4|-0.2 to 0.2|Porcentagem mínima e máxima para tradução vertical|
|Número de Tentativas|int [1 - 6]|3|Número máximo de tentativas sem degenerar caixas|




### Esticar imagem

**Deformação por cisalhamento aleatório da imagem**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Probabilidade|percent 0% - 100%|0.3|Probabilidade de mudança de cisalhamento|
|Imagem de cisalhamento mínimo e máximo|range from -60 to 60|-10 to 10|Valores mínimo e máximo para deformação por cisalhamento aleatório|




### Imagem em escala

**Escala aleatória da imagem**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Probabilidade|percent 0% - 100%|0.3|Probabilidade de escala aleatória|
|Imagem em escala mínima e máxima|range from 0.4 to 1.6|0.8 to 1.2|Valores mínimo e máximo para escala aleatória|




### Virada aleatória da imagem

**Flip Parameters**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Probabilidade de inversão horizontal|percent 0% - 100%|0.3|Virada horizontal aleatória da imagem|
|Probabilidade de inversão vertical|percent 0% - 100%|0.3|Virada vertical aleatória da imagem|




### Contraste aleatório

**Mudanças aleatórias no contraste da imagem**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Probabilidade|percent 0% - 100%|0.3|Probabilidade de mudança de contraste|
|Contraste mínimo e máximo|range from 0.4 to 2|0.8 to 1.2|Valores mínimo e máximo para mudanças no contraste da imagem|




### Brilho aleatório

**Mudanças aleatórias no brilho da imagem**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Probabilidade|percent 0% - 100%|0.3|Probabilidade de mudança de brilho|
|Brilho mínimo e máximo|range from -0.6 to 0.6|-0.2 to 0.3|Valores mínimo e máximo para mudanças no brilho da imagem|




### Gama aleatória

**Mudanças aleatórias na gama da imagem**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Probabilidade|percent 0% - 100%|0.3|Probabilidade de gama aleatória|
|Gama mín. e máx.|range from 0.1 to 12|0.4 to 1.6|Valores mínimo e máximo para mudanças na gama da imagem|




### Saturação aleatória

**Mudanças aleatórias na saturação da imagem**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Probabilidade|percent 0% - 100%|0.3|Probabilidade de mudança de saturação|
|Saturação mínima e máxima|range from 0.1 to 2|0.5 to 1.5|Valores mínimo e máximo para mudanças na saturação da imagem|




### Matiz aleatório

**Mudanças aleatórias no matiz da imagem**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Probabilidade|percent 0% - 100%|0.3|Probabilidade de matiz aleatório|
|Matiz mín. e máx.|range from -1 to 1|-0.05 to 0.05|Valores mínimo e máximo para mudanças no matiz da imagem|




### Ruído aleatório

**Inserção aleatória de ruído de imagem**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Probabilidade|percent 0% - 100%|0.3|Probabilidade de inserção de ruído|
|Método de ruído|choice ['gauss', 'poisson', 'speckle']|gauss|Método para inserção de ruído|




### Desfoque aleatório

**Desfoque aleatório da imagem**

|Parameter|Values|Default|Description|
|---------|------|-------|-----------|
|Probabilidade|percent 0% - 100%|0.3|Probabilidade de desfoque aleatório|
|Tamanho do kernel|choice [3, 5, 7, 9]|5|O tamanho do kernel para desfocar a imagem|




<!-- </parm_table> -->


## Para onde devo ir agora?

* [Parâmetros de Treinamento](/docs/concepts/training/train_parms): Parâmetros gerais para treinamento da rede neural
* [Parâmetros de Redes Neurais](/docs/concepts/training/dnn_parms): Parâmetros específicos da rede neural
* [Parâmetros de Expansão de Dados](/docs/concepts/training/data_augmentation_parms): Parâmetros para expansão de dados - Data Augmentation
