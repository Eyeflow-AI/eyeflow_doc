---
title: "Flow"
linkTitle: "Flow"
weight: 2
description: >
  Diagrama de fluxos para processamento das imagens e tomadas de decisões
---

O Flow é um programa no formato low-code, construído com componentes de código, orientado para a decomposição de dados de imagens
(*não estruturados*) em dados de saída (*estruturados*).

**O Flow é estruturado como um processo de entrada-saída.**

A entrada é um fluxo de imagens, como por exemplo:
- Câmera: Industrial, Segurança, IP
- Celular
- Arquivo de Vídeo

A saída pode ser para qualquer outro sistema de dados como:
- Arquivos: JSON, CSV, TXT
- Bancos de dados: MongoDB, Postgres
- Filas de mensagem: RabbitMQ, AMQP
- Controladores: CLP, IC, TCP, RS-232
- Envio de alarmes: E-mail, SMS, Notificações

Como o Eyeflow é uma plataforma extensível, não existe limites para criação de componentes. É possível criar rapidamente um componente
em Python e usá-lo no Flow para executar a função desejada.

Entre a entrada e a saída o processamento das imagens é feito em componentes de Redes Neurais. Cada componente desses estará ligado a
um dataset, e irá usar o modelo treinado com o dataset para executar em produção.

É possível também utilizar componentes que enviam as imagens para processamento em serviços de provedores de cloud. Por exemplo, usar um
componente que pega a imagem de um documento e envia para o reconhecimento de caracteres do Google, e daí processar a resposta para
digitalizar esse documento.

Criar um Flow é um processo bem simples.
#### Clique na aba Flow na barra de navegação
Abrirá a tela para carregar um Flow ou Criar um novo.
Ao clicar em **Novo Flow** irá abrir uma tela para entrar com os dados. É só preencher os dados e pronto, o Flow será criado.

![Criar Flow](/screenshots/pt-br_create_flow.jpg#bordered "Criar Flow")

Após a criação do Flow vamos adicionar alguns componentes para criar um flow simples que identifica de o Pet na imagem.
### Vamos adicionar 3 componentes nesse Flow:
#### Input Câmera IP - Coloque ```localhost``` como URL

![Componente Camera IP](/screenshots/pt-br_flow_camera_ip.jpg#bordered "Componente Camera IP")

#### ROI Cutter - Coloque o ```nome``` Identifica Pet e escolha o dataset ```Gatos e Cachorros```

![Componente ROI Cutter](/screenshots/pt-br_flow_roi_cutter.jpg#bordered "Componente ROI Cutter")

#### Output JSON File Save - Preencha ```filename``` como ```test.json```

![Componente File Save](/screenshots/pt-br_flow_file_save.jpg#bordered "Componente File Save")

#### Ligue as saídas de cada componente na entrada do próximo

![Flow Completo](/screenshots/pt-br_flow_basic.jpg#bordered "Flow Completo")

**Pronto! O Flow está completo.**

Uma das grandes vantagens da plataforma EyeFlow.AI é que ela é um ambiente integrado completo para o desenvolvimento de aplicações
de Video Analytics. O processo de redes neurais exige uma razoável quantidade de exemplos anotados para poder aprender, e a
maneira mais fácil de conseguir esses exemplos é utilizando vídeos.

Então, o processo de desenvolvimento envolve um ciclo de atividades:
1. Testa o vídeo no Flow observando se a aplicação está marcando o vídeo corretamente
2. Identifica os erros que a aplicação está cometendo e vai nos datasets
3. Na tela de **Novos Exemplos** procura por quadros onde a rede neural não identificou o objeto corretamente
4. Adiciona vários exemplos de erro (de 30 a 50 em cada ciclo é um bom número)
5. Anota os novos exemplos corrigindo os erros
6. Treina a rede neural e verifica os indicadores de assertividade para ver se a rede está aprendendo bem
7. Após os treinamentos volta para testar novamente o vídeo

Após termos bons resultados nas anotações dos vídeos nosso Flow já está pronto para publicarmos na borda.

## Para onde devo ir agora?

* [Dataset](/docs/concepts/dataset/): Anotando Datasets
* [Treinamento](/docs/concepts/training/): Treinando a rede neural
