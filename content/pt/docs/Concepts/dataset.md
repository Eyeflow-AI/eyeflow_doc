---
title: "Dataset"
linkTitle: "Dataset"
weight: 3
description: >
  Conjunto de exemplos anotados para treinamento das redes neurais
---

<!-- {{< note >}}  {{< /note >}} -->
Um dataset é um conjunto de exemplos anotados que servem para instruir uma rede neural sobre o que é desejado
que seja reconhecido nas imagens.
No conjunto de imagens do dataset iremos ter vários exemplos diferentes dos objetos que desejamos identificar
ou reconhecer. Esses exemplos irão alimentar o treinamento da rede neural para que possa ser identificado o padrão
comum entre eles.

## Tipos de dataset
Os datasets podem ser de vários tipos. Os mais utilizados no Eyeflow são:
* [ObjectDetection](#objectdetection)
* [Classification](#classification)
* [AnomallyDetection](#anomallydetection)
* [InstanceSegmentation](#instancesegmentation)

Cada tipo de dataset possui uma anotação diferente, e um diferente tipo de saída.

### ObjectDetection
Os datasets ObjectDetection costumam ser os mais utilizados pela sua versatilidade e facilidade de anotação.
O objetivo é identificar um objeto específico em uma imagem ampla, delimitando uma área retangular ao redor do objeto.
Sua anotação costuma ser bem simples e rápida, pois basta clicar e arrastar um retângulo (*box*) e definir qual a
classe do objeto.
É executado por um tipo de rede neural que pode ser bastante otimizada para execução na borda, podendo chegar a
centenas de FPS em tempo real.

### Classification
Os datasets de Classification são os mais comuns, e foram os primeiros a surgir no universo de DeepLearning.
Basicamente identifica uma imagem como sendo uma de N classes. Por exemplo, se tiver uma lista de imagens de gato
pode-se definir qual a raça de cada um, e a rede neural irá aprender a identificar a raça em qualquer imagem.

### AnomallyDetection
{{< note >}} Este é um dataset ainda em fase experimental. {{< /note >}}

O dataset AnomallyDetection é orientado para identificar anomalias em imagens de um mesmo objeto. A ideia é
alimentar o dataset com muitas imagens do objeto "correto" e assim a rede neural aprender o padrão bom.
Quando a rede neural for apresentada a uma imagem de um objeto que tem uma diferença do padrão bom (anomalia),
ela irá apontar a anomalia.

### InstanceSegmentation
{{< note >}} Este é um dataset ainda em fase experimental. {{< /note >}}

InstanceSegmentation é um dataset que se popularizou nos últimos anos devido a sua intensa utilização nos sistemas
de veículos autônomos e sistemas de IA para medicina. Trata-de de identificar o objeto, juntamente com todo seu contorno
pixel a pixel. Sua saída é bastante impressionante, pois permite "recortar" detalhadamente o objeto do fundo da imagem,
porém, sua anotação é extremamente trabalhosa, geralmente demandando uma grande equipe de pessoas para gerar um
conjunto adequado de imagens anotadas para treinamento.

## Criando um dataset
#### Criar dataset é uma tarefa bem simples. Basta clicar no menu lateral em **Novo Dataset**.

![Criar Dataset](/screenshots/pt-br_create_dataset.jpg#bordered "Criar Dataset")

#### Irá abrir uma tela para entrar com os dados do dataset.

![Criar Dataset](/screenshots/pt-br_create_dataset_modal.jpg#bordered "Criar Dataset")

É só preencher o Nome e Descrição, escolher o tipo e definir a qual Aplicação o dataset pertence.
Depois é preciso adicionar pelo menos uma classe.

## Classes
O objetivo da rede neural será identificar um padrão na imagem, e dar saída disso em formato de dados. Assim, criamos
classes no dataset para poder usarmos para marcar as imagens, e assim ensinar a rede neural a reconhecer esses padrões
e nos informar qual foi a classe reconhecida.
Por exemplo, se temos várias imagens de exemplos de cachorros e gatos, e queremos saber se trata-se de um ou outro na
imagem, criamos duas classes:

![Criar Classes](/screenshots/pt-br_create_classes_modal.jpg#bordered "Criar Classes")

As cores escolhidas servirão para ajudar na anotação do dataset, e irão aparecer na anotação dos vídeos.

## Exemplos
Exemplos são imagens anotadas que irão instruir a rede neural no aprendizado do reconhecimento dos padrões. Inserimos
várias imagens no dataset a partir de quadros de um video ou fotos, e depois anotamos em cada uma dessas imagens
aquilo que é desejado ser reconhecido.
A maneira mais simples e rápida de adicionar novos exemplos é extraindo de vídeos de exemplo. Ao passar um vídeo em
um Flow a ferramenta extrai alguns dos quadros do vídeo e os disponibiliza na tela de Novos Exemplos.

![Menu Novos Exemplos](/screenshots/pt-br_menu_new_examples.jpg#bordered "Menu Novos Exemplos")

Nessa tela também é possivel subir novos exemplos a partir de imagens localizadas no computador.

![Inserir Novos Exemplos](/screenshots/pt-br_insert_new_examples.jpg#bordered "Inserir Novos Exemplos")

{{< tooltip >}}
Para que uma rede neural aprenda bem é importante que haja uma boa diversidade
de exemplos. Inserir várias imagens muito parecidas, ou inserir muitas imagens de uma classe e poucas das outras
irá fazer com que o dataset fique desbalanceado e a rede não aprende bem
{{< /tooltip >}}

## Anotação
Anotação é o processo onde o usuário marca na imagem o objeto que deseja que seja identificado, gerando assim um exemplo
que será utilizado no treinamento da rede neural.

As anotações são diferentes para cada tipo de dataset. Em um dataset [ObjectDetection](#objectdetection) o usuário clica e
arrasta o mouse para desenhar uma caixa ao redor do objeto, e depois define a qual classe esse objeto pertence.

![Anotar Exemplo](/screenshots/pt-br_annotate_example.jpg#bordered "Anotar Exemplo")




## Para onde devo ir agora?

* [Treinamento](/docs/concepts/training/): Treinando a rede neural
* [Flow](/docs/concepts/flow/): Criando o Flow
