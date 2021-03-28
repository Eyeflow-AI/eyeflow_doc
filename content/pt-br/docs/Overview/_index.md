---
title: "Visão Geral"
linkTitle: "Visão Geral"
weight: 1
description: >
  Entenda todos os elementos que irá utilizar para construir sua aplicação
---

#  Visão Geral da Plataforma EyeFlow

>   A plataforma de vídeo analytics desenvolvida pela SiliconLife foi construída
>   para possibilitar a criação de aplicações de mercado utilizando Inteligência
>   Artificial de uma maneira prática e ágil.

## Diversas funcionalidades nativas:

-   Condições de detecção configuráveis e modulares

-   Interface amigável:

    -   Construção de fluxos operacionais com *drag’n’drop* de componentes de AI

    -   Ambiente de desenvolvimento completo para novas aplicações

    -   Extensibilidade para adição/desenvolvimento de novos componentes

-   Gerenciamento ágil de novos requisitos de dados e processos de negócios

-   Integração simplificada com outras plataformas

-   Integração de maneira simples e consistente com sistemas de dados legados

-   Design modular, orquestrado para grandes volumes de chamadas

-   Facilidade de integração de componentes de software aberto, novos algoritmos
    de AI ou com serviços de nuvem

-   Configuração de diversos tipos de alarmes e relatórios

-   Integração com *Data Lake* corporativo

>   O EyeFlow oferece acessos simplificados às soluções Inteligência Artificial
>   para vídeo analytics de forma simples, possibilitando a sua utilização por
>   pessoas de áreas distintas. Esta solução também possibilita aos
>   desenvolvedores de IA utilizar os seus códigos como componente do fluxo, no
>   EYeFlow, possibilitando a utilização deste componente como parte da
>   ferramenta, o que garante utilização de todas as facilidades disponíveis
>   possibilitando uma entrega de maneira prática e ágil

# Como funciona?

![Visão Geral](/screenshots/2edd9b0175960780ed479291d0adc6d8.png)

## ![Flow](/screenshots/036889fd1c08813042e32d9fe50439a9.png#icon) Flow

Interface intuitiva para montagem de fluxos de processamento, defini passo a
passo das etapas a serem realizadas. O Fluxo é construído utilizando os
componentes previamente criados utilizando componentes próprios e de
terceiros para tratamento de dados. A interface dispõe da tecnologia Drag
And Drop, facilitando a criação do fluxo. Esta interface disponibiliza
componentes para classificar, detectar, realizar OCR, realizar processos
analíticos de pessoas, medição entre outros.

## ![Upload](/screenshots/13526a42e6cba74c2ca123581f41d23d.png#icon) Upload

![Botão Anotar](/screenshots/8f54bde44fd3300b8923ce16c7d6bafc.png#button)
Interface disponível na ferramenta para carregar o vídeo para o treinamento da Rede Neural,
disponibilizando frames retirado do vídeo para construção do Dataset

## ![Dataset](/screenshots/e11aa076d81124afd80c34d4cdfe8d09.png#icon) Dataset

Interface para seleção de frames do vídeo carregado na etapa anterior,
parametrização e customização dos atributos para o treinamento na Rede
Neural,

## ![Marcação](/screenshots/2cbc01d87ccb578ccf41bce161e9b13a.png#icon) Marcação

Ferramenta disponível dentro da seção do Dataset para marcação das áreas de interesse no frame

## ![Treinamento](/screenshots/3b897c90fad29c16aea0f2675bbe949b.png#icon) Treinamento

Seção disponível no Dataset para submeter treinamento da Rede Neural, executando os passos definido no fluxo criado.

## ![Botão Video](/screenshots/43412dcb99e664fe196d1f168404a4ae.png#icon) Teste

Valida o resultado da rede neural, através da interface de dashboard e através da
execução do vídeo carregado, caso o resultado não seja satisfatório, a
solução deverá ser submetida a um novo treinamento, objetivando um
aprimoramento do aprendizado da rede neural.

## ![Publicar](/screenshots/50064beae7ef575ef6ab69b87deda608.png#icon) Publicar

Disponibiliza o Flow para uso, a rede neural já está treinada, pronta para ser entregue para
Operação


# Para onde devo ir agora?

* [Para começar](/docs/getting-started/): Primeiros passos para construir sua aplicação
* [Exemplos](/docs/examples/): Veja alguns exemplos!
