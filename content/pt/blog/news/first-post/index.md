---
date: 2021-04-02
title: "Video Analytics com Deep Learning pode ser simples"
linkTitle: "Apresentando o Eyeflow.AI"
description: "Como 4 anos superando desafios nos impulsionaram a desenvolver uma grande ferramenta"
author: Alex Sobral de Freitas ([@alexsobral](https://alexsobral.medium.com))
resources:
- src: "**.{png,jpg}"
  title: "Image #:counter"
  params:
    byline: "Photo: Ronaldo de Oliveira / Unsplash"
---

**Apresentando Eyeflow.AI**

{{< imgproc featured-bridge-and-trees.jpg Fill "600x300" />}}

Em 2016 fui convidado por um amigo para o desafio de desenvolver uma solução de monitoração por vídeo para uma grande mineradora brasileira. Sempre fui apaixonado por inteligência artificial. Acompanho o tópico desde 1995 e procuro aplicações reais para machine learning e deep learning desde 2011, então aceitei o desafio imediatamente.

> A tarefa parecia bastante complexa: capturar imagens de vagões de transporte de minério usando câmeras de vídeo para automatizar a inspeção dos componentes e detectar falhas.

Eu sou desenvolvedor com 35 anos de experiência, quanto mais complexa a tarefa, mais animado eu fico.

Escolhi o framework Theano e arquitetura SSD para Rede Neural, configurei o ambiente e testei se estava tudo funcionando. Então peguei um filme gravado de um celular, extraí alguns frames, fiz um pequeno programa python que me permitiria anotar as caixas desenhando nos frames e comecei a treinar a rede com meu dataset simples. Após duas semanas de muito trabalho e várias dificuldades sempre presentes nos programas de código aberto, pude ver o treinamento da rede e detectar os objetos em meu dataset.

Após mostrar esta pequena Prova de Conceito ao cliente, iniciamos um projeto piloto que detectaria os objetos com uma câmera próximo à ferrovia. Foram 3 meses de trabalho árduo, mas no final conseguimos mostrar os resultados ao cliente, que ficou muito impressionado com a solução.

Essa experiência me iluminou. O Deep Learning era uma tecnologia muito nova com a capacidade de resolver toda uma classe de novos problemas que não podiam ser resolvidos por algoritmos tradicionais. No entanto, era extremamente trabalhoso e difícil de dominar. Então, havia espaço para uma ferramenta que simplificasse e agilizasse o desenvolvimento de aplicativos de Video Analytics. Há anos que procurava uma ideia para desenvolver um produto e finalmente tinha encontrado.

> Apresentando EyeFlow.AI, uma plataforma completa para o desenvolvimento e hospedagem de aplicações de Video Analytics, orientada para ser fácil de aprender, prática de usar e totalmente extensível. De desenvolvedores a desenvolvedores.

![Eyeflow.AI](/logo-eyeflow-wide.png)

Nos últimos 3 anos desenvolvemos vários projetos de Video Analytics para grandes empresas, algumas das quais estão em operações de missão crítica realizando a inspeção final de veículos produzidos em uma grande montadora. Todos esses projetos estamos desenvolvendo usando a plataforma EyeFlow, e agora decidimos abrir essa tecnologia para que outras empresas e desenvolvedores também possam construir aplicativos e projetos usando Vídeo Analytics.

Desejamos que nossos produtos possam democratizar o uso do Deep Learning para a construção de aplicativos comerciais e promover o desenvolvimento de aplicativos para automação de tarefas repetitivas que podem ser realizadas por algoritmos de IA.

E acima de tudo, queremos compartilhar nossa experiência com Video Analytics para que outros também tenham sucesso na execução de seus projetos. Comecei a escrever aqui para divulgar o nosso produto, mas também para poder partilhar conhecimentos e experiências. Espero ser capaz de fazer isso continuamente.

No momento, estamos lançando nossa plataforma em uma versão beta privada, mas esperamos poder abri-la em breve para todos que quiserem experimentá-la.
