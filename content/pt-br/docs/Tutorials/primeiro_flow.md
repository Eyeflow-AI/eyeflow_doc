---
title: "Primeiro Flow"
date: 2021-03-26
weight: 4
description: >
  Tutorial 1 - Construa seu primeiro flow
---

>   **Treinamento EyeFlow**

>   **SERPRO**

>   Agenda

1.  A solução

    1.  Como funciona?

2.  Login

3.  Flow

    1.  Componentes

    2.  Entrada

    3.  Saída

    4.  Seleção

4.  Upload vídeo

    1.  Anotar

5.  Dataset

    1.  Edição de dataset

    2.  Edição parâmetros da rede neural

6.  Treinamento

7.  Dashboard

8.  Teste Vídeo

9.  Deploy

# A solução

##  Visão Geral da Plataforma EyeFlow

>   A plataforma de vídeo analytics desenvolvida pela SiliconLife foi construída
>   para possibilitar a criação de aplicações de mercado utilizando Inteligência
>   Artificial de uma maneira prática e ágil.

>   Nossa solução oferece diversas funcionalidades nativas:

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

    O EyeFlow oferece acessos simplificados às soluções Inteligência Artificial
    para vídeo analytics de forma simples, possibilitando a sua utilização por
    pessoas de áreas distintas. Esta solução também possibilita aos
    desenvolvedores de IA utilizar os seus códigos como componente do fluxo, no
    EYeFlow, possibilitando a utilização deste componente como parte da
    ferramenta, o que garante utilização de todas as facilidades disponíveis
    possibilitando uma entrega de maneira prática e ágil

### Como funciona?

>   ![](/screenshots/2edd9b0175960780ed479291d0adc6d8.png)

### ![flow Icon 3672795](/screenshots/036889fd1c08813042e32d9fe50439a9.png)Flow

>   Interface intuitiva para montagem de fluxos de processamento, defini passo a
>   passo das etapas a serem realizadas. O Fluxo é construído utilizando os
>   componentes previamente criados utilizando componentes próprios e de
>   terceiros para tratamento de dados. A interface dispõe da tecnologia Drag
>   And Drop, facilitando a criação do fluxo. Esta interface disponibiliza
>   componentes para classificar, detectar, realizar OCR, realizar processos
>   analíticos de pessoas, medição entre outros.

### ![Upload Icon 3738519](/screenshots/13526a42e6cba74c2ca123581f41d23d.png)Upload

>   ![](/screenshots/8f54bde44fd3300b8923ce16c7d6bafc.png)Interface disponível na
>   ferramenta para carregar o vídeo para o treinamento da Rede Neural,
>   disponibilizando frames retirado do vídeo para construção do Dataset

### ![pictures Icon 2518756](/screenshots/e11aa076d81124afd80c34d4cdfe8d09.png)Dataset

>   Interface para seleção de frames do vídeo carregado na etapa anterior,
>   parametrização e customização dos atributos para o treinamento na Rede
>   Neural,

### Marcação

>   ![](/screenshots/2cbc01d87ccb578ccf41bce161e9b13a.png)Ferramenta disponível dentro
>   da seção do Dataset para marcação das áreas de interesse no frame

### ![Running Man Icon 429544](/screenshots/3b897c90fad29c16aea0f2675bbe949b.png)Treinamento

>   Seção disponível no Dataset para submeter treinamento da Rede Neural,
>   executando os passos definido no fluxo criado.

### Teste

>   ![Video Icon 2529300](/screenshots/43412dcb99e664fe196d1f168404a4ae.png)Valida o
>   resultado da rede neural, através da interface de dashboard e através da
>   execução do vídeo carregado, caso o resultado não seja satisfatório, a
>   solução deverá ser submetida a um novo treinamento, objetivando um
>   aprimoramento do aprendizado da rede neural.

### Entrega

>   ![Deploy Icon
>   2715693](/screenshots/50064beae7ef575ef6ab69b87deda608.png)Disponibiliza o Flow
>   para uso, a rede neural já está treinada, pronta para ser entregue para
>   Operação

# Treinamento

>   **Este treinamento será baseado em um caso de uso, para este caso, está
>   disponível um vídeo para ser utilizado para treinamento da rede neural, que
>   terá o objetivo de detecção do elemento Porca, identificando suas faces
>   (face lisa e face prospecção)**,

### Atividade

>   **Caso Uso: Detecção e Identificação da Face das Porcas.**

>   Objetivo: identificar a face das porcas, informando se a face é lisa ou se a
>   face é prospecção

>   ![](/screenshots/ec5e47ae04a38e9fdf615ecc47ccb97d.png)
>   ![](/screenshots/5801a2ce81fee943c1a839d20dc38c53.png)

>   Face Porca Lisa Face Porca Prospecção

>   Siga os passos abaixo:

##  Login – Entre na plataforma EyeFlow

>   Acesse:

>   https://app.eyeflow.ai

>   ![](/screenshots/54452b239b80e31c2b115e38884a828f.png)

>   **Usuario**: treinamento

>   **Senha**: Teste

## diretório

>   Quando o usuário acessar a ferramenta, este terá acesso ao seu domínio, este
>   domínio é chamado de Diretório.

>   Diretório é uma subdivisão lógica da ferramenta que permite ao usuário uma
>   determinada área de uso, obedecendo os critérios e os padrões de segurança
>   de acesso.

## Aplicação

>   Aplicação é um subdiretório, área disponibilizada na ferramenta, em que o
>   usuário pode criar seus projetos(aplicações) para executar na rede neural.

>   Click na Aba de Aplicação, vide Figura 2

>   **![](/screenshots/278595a445b84611c12da54e179d4a85.png)Figura 2**

>   Crie uma nova aplicação, pressionando o botão \< + \>, vide figura 3

>   **Figura 3**

>   **![](/screenshots/8aa5d0c1d01eab46d7f83cfcf61a024e.png)**

>   Crie uma Aplicação com nome \<SERPRO.nome do aluno\>, vide Figura 4

>   **Figura 4**

>   ![](/screenshots/5aeb0464310d01fd998a3330b34ab08a.png)

## Fluxo

>   A solução permite ao usuário criar o fluxo para execução da rede neural.
>   Esta solução baseia-se em uma ferramenta Drag and Drop (Arrastar e Soltar)
>   de fácil manuseio onde os usuários podem utilizar os componentes dispostos
>   em seu Menu.

>   Click na Aba Fluxo, vide Figura 5

>   **Figura 5**

>   **![](/screenshots/9624b3918209942bbedc3281fe844f9e.png)**

>   Antes de Criar fluxo vamos conhecer os componentes existentes na Ferramenta,
>   na figura 6 faremos uma breve descrição:

>   **Figura 6**

>   ![](/screenshots/b9ee846a7bef5d5a7d875987ec191d01.png)

>   ![](/screenshots/86ee8dc27659b8a3a46be6ca58af2a22.png)

>   **![Câmera IP tipo Box - Planet
>   Ello](/screenshots/ee5978b24eedb262e89aeb7872e05661.jpeg)Imagens dos modelos
>   cameras informados:**

>   ![](/screenshots/e47655b354ef9adf5ab04391acf39f75.png)

>   ![Flea3 USB3 \| FLIR Systems](/screenshots/6fe5ed6c4580c42d994e0f89ab9e8daf.png)

>   ![5MP Camera for NVIDIA Jetson Xavier NX / Nano developer
>   kit](/screenshots/66934571ab2954b852cd3f5c3cc311ab.jpeg)

>   ![](/screenshots/a1b0663d945545f97c22c6ccdc81b022.png)

>   ![](/screenshots/26680cdce30aa9c375711fa8faa957e6.png)

####  Construa seu Fluxo

>   **Input**

CAMERA IP – Arraste o componente para o fluxo, vide figura 7

**Figura 7**

![](/screenshots/bcaa17768ffda276bfd23eb259fc2126.png)

>   Double Click no componente CAMERA IP, aparecerá a tela da figura 8
>   demonstrada abaixo:

>   **Figura 8**

>   ![](/screenshots/cff838b4aeabb285995b06346a14e70e.png)

>   **Seletor**

ROI CUTTER – Arraste o componente para o Fluxo, vide Figura 9

**Figura 9**

>   ![](/screenshots/21d08445d07222cf875416ca0b88be0a.png)

-   Double Click no componente ROI CUTTER, aparecerá na tela a figura 10
    demonstrada abaixo:

    **Figura 10**

    ![](/screenshots/337b7304a836759447829c0218facd79.png)

    **Siga os passos da figura 11**

    **Figura 11**

    ![](/screenshots/8f0d29dda6f9f27221d1e211c5dd27b8.png)

    Crie uma nova Classe, seguindo passo representado na figura 12 abaixo:

    **Figura 12**

    ![](/screenshots/b58b2a563154be20185941b41f43cf6d.png)

Aparecerá a figura 13 demonstrada abaixo, nesta etapa estaremos adicionando duas
novas classes

>   **Figura 13**

>   ![](/screenshots/07fba474794f9334206980b7b17e212a.png)

>   Save as configurações realizadas no componente ROI CUTTER, vide figura

>   Figura

>   ![](/screenshots/e6a94df39e040762c7292296b673e677.png)

Faça a comunicação entre a CÂMARA IP com ROI CUTTER no fluxo, conforme figura 14
abaixo:

>   **Figuro 14**

>   ![](/screenshots/55b2a4a94b260d0d95d41a746cf6320f.png)

>   Salve o Flow: Click no botão \<Save Flow\> conforme figura 15 abaixo:

>   **Figura 15**

>   ![](/screenshots/c6d71a06358b7b35cfa5d3ecf4340ea0.png)

##  Upload

>   Para este treinamento foi disponibilizado um vídeo teste:

>   Endereço do vídeo para Download

>   C:Tets\\bbi\\nnn

>   ![Upload Icon 3738519](/screenshots/13526a42e6cba74c2ca123581f41d23d.png)![flow
>   Icon
>   3672795](/screenshots/036889fd1c08813042e32d9fe50439a9.png)![](/screenshots/8f54bde44fd3300b8923ce16c7d6bafc.png)

>   Carregue o vídeo

>   Click no botão \<Teste Vídeo\>, conforme figura 16 abaixo:

>   **Figura 16**

>   ![](/screenshots/4beaed025791a12acf13245f6156b0d7.png)

>   Faça o upload de Video teste, click no botão \<UPLOAD VIDEO\> vide Figura 17

>   **Figura 17**

>   ![](/screenshots/6ff411258db74b91e1ecacf0db27e66e.png)

>   Arraste o vídeo para o local informado na figura 18 abaixo:

>   **Figura 18**

>   ![](/screenshots/2d4a53d3b31d9783e49fc511c615004c.png)

>   Neste momento aparecerá uma barra demonstrando a carga do vídeo na
>   ferramenta, vide Figura 19

>   **Figura 19**

>   ![](/screenshots/626a6c42c6b044d26f05fd704fe91eac.png)

>   Neste momento a solução estará executando o seu fluxo criado e
>   disponibilizando novos exemplos(frames) para seu Dataset.

## Dataset![pictures Icon 2518756](/screenshots/e11aa076d81124afd80c34d4cdfe8d09.png)![Upload Icon 3738519](/screenshots/13526a42e6cba74c2ca123581f41d23d.png)![flow Icon 3672795](/screenshots/036889fd1c08813042e32d9fe50439a9.png)

>   ![](/screenshots/8f54bde44fd3300b8923ce16c7d6bafc.png)

>   Entre na Aba DATASETS, vide Figura 20

>   **Figura 20**

>   ![](/screenshots/cb0d9f16e443fad19887ac227943415c.png)

>   Abrirá a pasta do Dataset, vide Figura 21

>   **Figura 21**

>   ![](/screenshots/2c258bb34ea7d868a9c67fb6a019439d.png)

>   Selecione frames/imagens para ser treinadas no Dataset, click nos botões de
>   seleção, conforme a figura 22 abaixo:

>   **Figura 22**

>   ![](/screenshots/911c7bcf7b17c08f3c2da836c62e6165.png)

>   Insira os novos exemplos selecionados, click no botão \<Insira novos
>   exemplos\>, vide Figura 23

>   **Figura 23**

>   ![](/screenshots/94702afc11390778519bb29e9439d074.png)

>   Retorne para a Aba Dataset, vide Figura 24

>   **Figura 24**

>   ![](/screenshots/a3ac82b770d68bce6bb087659a597bce.png)

>   Click no seu Dataset criado, vide Figura 25

>   **Figura 25**

>   ![](/screenshots/8f36879c60fbf6b59200f537e27f2605.png)

>   Marque as regiões de interesse, selecionando a Porca com a Face Lisa e com a
>   Face Projeção, conforme a Figura 26 abaixo

>   **Figura 26**

>   ![](/screenshots/c55290311d8113c5c93a917cd5cef3e3.png)

>   Após a marcação de todos os frames selecionados click no botão \<Painel de
>   Treino\>, conforme Figura 25

>   **Figura 27**

>   ![](/screenshots/18e3818244e9afbe876baf9392c69560.png)

### Edição de Parâmetros para treinamento da rede neural

>   Siga os passos da figura 28, representada abaixo:

>   **Figura 28**

>   ![](/screenshots/16b5d277d6395f1288ab844a59fbc686.png)

>   Aparecerá figura 29 demonstrada abaixo:

>   **Figura 29**

>   Descrição dos parâmetros na ferramenta

>   ![](/screenshots/22c40d8d1c363711e6f5e3a39b924112.png)

>   \*Ao final do treinamento você encontrará o Glossário com algumas definições
>   dos parâmetros da rede neural

## ![](/screenshots/8f54bde44fd3300b8923ce16c7d6bafc.png)![Upload Icon 3738519](/screenshots/13526a42e6cba74c2ca123581f41d23d.png)![flow Icon 3672795](/screenshots/036889fd1c08813042e32d9fe50439a9.png)Treinamento da rede neural

>   ![pictures Icon
>   2518756](/screenshots/e11aa076d81124afd80c34d4cdfe8d09.png)![Running Man Icon
>   429544](/screenshots/3b897c90fad29c16aea0f2675bbe949b.png)

>   Após edição dos parâmetros da rede neural, vamos submeter os seus frames
>   marcados para treinamento, onde executará o fluxo criado.

>   Siga os passos representado na figura 30 abaixo:

>   **Figura 30**

>   ![](/screenshots/ee2abb31954fea2099d8790c8dd0429d.png)

>   Aparecerá um pop-up na tela com o pedido de confirmação, vide figura 31

>   **Figura 31**

>   ![](/screenshots/646bc2a77c289b3e681f03f328ecae5a.png)

>   Após esta etapa, aparecerá uma tela com o andamento do treinamento, vide
>   Figura 32

>   **Figura 32**

>   **![](/screenshots/33e934dfaa47afa81bcff852189c6b34.png)**

## Teste -resultado

>   Após o treinamento da rede neural, você poderá ver o resultado do
>   treinamento no relatório demonstrado na figura 33, você também poderá
>   executar o vídeo carregado e observar o resultado que alcançou, caso o
>   resultado não seja satisfatório, a rede neural deverá realizar um novo
>   treinamento, para este caso, devemos submeter novos exemplos no Datasets,
>   com o objetivo de melhorar o aprendizado da rede neural

>   **Figura 33**

>   ![](/screenshots/b3810a2f7f2f9724e96680b013bb77ed.png)

### Validação no vídeo

>   Conforme visto anteriormente no item Flow, a ferramenta disponibiliza a
>   opção de teste no vídeo carregado.

>   Siga os passos descrito na figura 34 abaixo:

>   Click na Aba\< Flow\>

>   **Figura 34**

>   ![](/screenshots/ef0e2286e9d11d6f3a8292ad4bfb8c08.png)

>   Siga os passos representados na figura 35

>   **Figura 35**

>   **![](/screenshots/db80a153eac05e2394fdd281d30392ed.png)**

>   Siga os passos representados na figura 31

>   **Figura 36**

>   **![](/screenshots/949318d213279ca64c1db3fe43563b42.png)**

>   Após esta etapa você poderá verifica no vídeo o resultado do seu Projeto, se
>   o resultado não for satisfatório, a rede neural deverá ser submetida a um
>   novo treinamento, para isso você deverá executar os passos informados no
>   item Datasets, este processo deve ocorrer até a rede neural encontrar o
>   resultado satisfatório.
