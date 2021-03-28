---
title: "Visão Geral"
linkTitle: "Visão Geral"
weight: 1
description: >
  Principais conceitos do Eyeflow.AI
---

## Aplicação
Conjunto de elementos que implementam um processo completo de Video Analytics.

Quando a gente se depara com um problema que envolve visão começamos a pensar em como podemos resolvê-lo
utilizando o Eyeflow. Na entrada temos a captura de imagens por uma câmera industrial ou um celular, e na saída
queremos ter essas imagens analisadas e interpretadas, para que ações possam ser tomadas em resposta.
Essa solução do problema é que chamamos de Aplicação.

## Flow
Conjunto de componentes encadeados que implementam uma aplicação.

No processo de construir uma aplicação o objetivo é transformar uma entrada de vídeo (*dados não estruturados*)
em uma ação programada (*dados estruturados*). Nesse processo iremos usar redes neurais e outros componentes de
software encadeados para poder decompor e interpretar as imagens de entrada e gerar as saídas desejadas.

## Rede Neural
Algorítmo matemático avançado que permite a computação de dados não estruturados.

As redes neurais são elementos computacionais que vêm sendo desenvolvidos desde os anos 60, inspiradas
nas pesquisas científicas sobre o funcionamento do cérebro (*neurônios*).

A partir de 2010, com avanços nos
algoritmos de processamento matemático e aproximação de funções algébricas, juntamente com o aumento de
capacidade dos processadores matemáticos e barateamento pela popularização dos mesmos nas placas gráficas
para jogos (*GPU*), as redes neurais evoluíram para utilização de várias camadas (*Deep Neural Network*).
Dessa forma começaram a surgir várias novas aplicações dessa tecnologia na solução de problemas complexos,
em sua maioria relacionados a dados não estruturados, como sons e imagens.
As redes neurais são os componentes fundamentais do Flow, pois permitem a solução de problemas de visão
computacional complexos, que antes não eram passíveis de serem resolvidos utilizando algorítmos tradicionais.

As redes neurais possuem uma capacidade de convergir matematicamente para um modelo computacional que
identifica os padrões nos dados. Essa capacidade permitiu o surgimento de soluções de Inteligência Artificial
que aprendem com exemplos que o usuário entrega para a rede.

## Dataset
Conjunto de exemplos que instruem o aprendizado da rede neural.

Uma rede neural é como uma caixa preta onde vamos inserindo exemplos na entrada e vamos dizendo o que queremos
ter na saída. Assim, o usuário deve gerar um conjunto desses exemplos, anotados com a saída desejada, que servirão
de dados para treinamento da rede neural na execução da tarefa.

## Treinamento
Processo computacional para convergir uma rede neural para o aprendizado dos padrões.

Depois que temos um dataset anotado colocamos os algorítmos de redes neurais para processar esses exemplos
até ela aprender a gerar a saída desejada. O treinamento busca reduzir o erro medido entre o que a rede neural
apresentou na saída em relação à anotação do exemplo feita pelo usuário. Quando esse erro é bem reduzido a
rede neural estará pronta para processar novos dados.

## Modelo
Rede neural treinada com um dataset.

Após o processo de treinamento é gerado um modelo, que poderá então ser utilizado no Flow para processamento
das imagens e geração das saídas desejadas.

## Edge / Borda
Dispositivo computacional que executa um flow em produção.

Depois que um flow está desenvolvido, testado e apresentando bons resultados ele pode ser publicado para
execução em um dispositivo que passará a funcionar em produção, como por exemplo a detecção de um defeito
na linha de manufatura.

## Para onde devo ir agora?

* [Dataset](/docs/Concepts/dataset/): Anotando Datasets
* [Flow](/docs/Concepts/flow/): Criando o Flow
