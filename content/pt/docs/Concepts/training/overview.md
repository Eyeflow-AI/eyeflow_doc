---
title: "Visão Geral"
linkTitle: "Visão Geral"
weight: 1
description: >
  Visão geral do treinamento
---

Treinamento é o processo onde os exemplos do dataset são alimentados na rede neural para aprendizado dos
padrões e geração do modelo.
É um processo matemático/algorítmico complexo, que exige uma grande capacidade computacional e necessita
rodar em servidores com placas gráficas GPU ou TPU no caso da cloud Google.

Esse processo é executado de forma iterativa buscando minimizar o erro medido entre o que a rede neural
apresentou na saída e a anotação feita no exemplo pelo usuário.
Ao longo do processo de minimização do erro é medida a assertividade da rede neural, e assim o usuário
pode verificar se a rede neural realmente aprendeu a identificar os padrões.

O processo de treinamento das redes neurais é bastante complexo, e dominar bem esse processo costuma demandar
bastante tempo, estudo e experimentação.

Felizmente, o Eyeflow.AI oferece um ambiente completo para acelerar e automatizar todas as tarefas para o desenvolvimento
de redes neurais, e possui sugestões de construção e parametrização, fruto de longos anos de experiência de uso
de redes neurais para solução de problemas reais.

## Conceitos importantes

### Quantidade de exemplos
A quantidade de exemplos de um dataset é um item muito importante para a eficácia das detecções. Para realizar
um treinamento de uma rede neural é necessário no mínimo 10 exemplos, sendo que um bom dataset para produção
vai demandar cerca de 1000 exemplos. Contudo, não adianta simplesmente lotar um dataset de exemplos sem testar
sua eficácia com casos reais, pois um excesso de exemplos semelhantes pode desbalancear o aprendizado e fazer com que seu
modelo fique enviesado e não tenha boa performance em produção.

Outro ponto importante é que deve-se manter uma quantidade similar de exemplos de cada classe, também para evitar
o desbalanceamento, e consequentemente enviesamento, do modelo. Se o dataset tiver muitos exemplos de uma só
classe e poucos das outras ele irá tender a detectar tudo como a classe dominante.

A melhor estratégia para adição de novos exemplos no dataset é testar o mesmo após o treinamento e verificar
os erros, para adicionar somente os novos exemplos que apresentaram erro, e daí corrigí-los e fazer um novo treinamento.
A cada iteração dessas o ideal é adicionar de 30 a 50 novos exemplos, e daí rapidamente o treinamento irá aumentar
a assertividade da detecção.

Após os testes com vídeos e publicação em produção o Eyeflow oferece um mecanismo para coleta de novos exemplos a
partir da borda, o que servirá para verificar se o modelo está tendo uma boa assertividade nos casos reais, e daí
podem ser adicionados os erros para continuar o processo de melhoria do dataset.

### Qualidade dos exemplos
Se a quantidade é importante, a qualidade é fundamental para garantir que a rede neural irá aprender a detectar os
padrões.

Para garantir a qualidade dos exemplos alguns pontos devem ser observados:
- O objeto a ser detectado deve estar bem visível na imagem. Se houver dúvidas para anotar o exemplo então a própria
rede neural terá dificuldades em aprender com esse exemplo.
- Para um dataset do tipo ObjectDetection as caixas não podem ser muito pequenas, nem grandes demais. Os testes de augmentation
vão indicar se as caixas estão sendo bem detectadas.
- Para um dataset Classification os exemplos precisam ser bem diferentes entre as classes. Será difícil detectar uma diferença
entre as classes se tal diferença for somente um pequeno detalhe na imagem total.
- Deve-se ter uma boa variedade nos exemplos. A adição de muitos exemplos muito parecidos irá fazer o modelo ficar enviesado
para detectar só esse tipo de imagem ou classe.

### Validação e Teste
No processo de treinamento o dataset é dividido em 3 grupos:
- Treino
- Validação
- Teste

A separação dos exemplos para os grupos é feita de forma aleatória, baseada nos parâmetros definidos para o treinamento.

O grupo de **Treino** é o que será efetivamente usado para treinar a rede neural. Ele deve ter a maior quantidade de exemplos,
sendo recomendado pelo menos 80% dos exemplos.

O grupo de **Validação** é usado para testar o modelo a cada final de época, e serve para verificar se o treino está evoluindo,
ou se estagnou ou viciou (*overfitting*). É recomendado que seja 10% dos exemplos até um máximo de 100 exemplos.

O grupo de **Teste** é usado para testar o modelo ao final do treinamento. Como esses exemplos nunca foram apresentados ao
dataset então servem como uma avaliação final do aprendizado, definindo qual a assertividade que o modelo apresenta. É o indicador
se a rede neural efetivamente aprendeu a reconhecer os padrões. É recomendado que seja 10% dos exemplos até um máximo de 100 exemplos.

{{< note >}}
O principal objetivo de um treinamento de rede neural é garantir que o modelo final irá **generalizar**, significa que irá
aprender com os exemplos o padrão para assim poder extrapolar para novos exemplos em situações reais. Muitas vezes o resultado
fica bom no treino, mas ruim em produção, indicando que o modelo não generalizou bem. Nessas situações deve-se coletar mais
exemplos de erro em produção para adicionar ao dataset.
{{< /note >}}

### Loss e Val Loss
Loss é a medida de erro que no processo de treinamento foi observado entre o que a rede neural detectou (*predict*) e o que deveria
ser a saída correta segundo a anotação (*ground thruth*). O processo matemático/algorítmico de treinamento das redes neurais busca
a minimização desse erro.

O Val Loss é a mesma medida, só que feita no grupo de validação ao final de uma época. Serve para acompanhar a evolução do treino
a cada ciclo de treinamento.

### mAP e Accuracy
O indicador de qualidade do treino é uma medida de acerto que leva em consideração todos os elementos de saída. Cada tipo de
dataset tem sua medida padrão de assertividade.

* Datasets *ObjectDetection* costumam utilizar o **mAP** (*Mean Average Precision*) como indicador de assertividade, pois mede o quanto a
box de saída engloba bem o objeto, indicando a classe correta, pela média de todas as classes.
* Datasets *Classification* costumam utilizar a **Accuracy**, que é o percentual de exemplos em que a rede neural previu corretamente
a qual classe o objeto pertence.

### Overfitting
É um fenômeno que ocorre comumento nos treinamentos. Ocorre no treinamento quando vemos o *Loss* continuar caindo, mas o *Val Loss* subir
ao invés de descer. Isso indica que a rede neural ficou "viciada" nos exemplos do treinamento e parou de generalizar para novos exemplos,
ou seja, ela aprendeu muito sobre os exemplos do treino, mas não consegue acertar exemplos novos.

### Expansão dos exemplos - Data Augmentation
É um trabalho demorado e repetitivo anotar os exemplos de um dataset, sendo porém a tarefa mais importante para poder usar uma
rede neural em uma aplicação real. Muitos projetos de AI estagnam na parte em que precisam reunir muitos milhares de exemplos anotados
para começar a ter bons resultados com redes neurais, mas a experiência com o Eyeflow.AI indica que é possível ter bons resultados apenas
com 300 exemplos em um dataset, e ótimos resultados com apenas 1000 exemplos.
Um dos aspectos chaves dessa performance está no Data Augmentation.

Data Augmentation é o processo de inserir perturbações nas imagens dos exemplos, no momento do treinamento, para forçar a rede neural
a aprender os padrões dos objetos, e não ficar "viciada" nos poucos exemplos que foram apresentados.

O Eyeflow.AI oferece uma ampla gama de algoritmos para Data Augmentation, que vão desde distorções geométricas e fotométricas nas imagens
até inserção de ruidos ou elementos estranhos.

O ponto importante a observar aqui é que não deve-se usar o Data Augumentation para modificar os exemplos deixando-os muito diferentes
das situação que serão encontradas no ambiente real, pois isto irá dificultar desnecessariamente o aprendizado da rede. Por exemplo, não
faria sentido em um dataset de carros inserir o *Flip Vertical*, pois não encontraremos uma situação com o carro de cabeça para baixo.

### Datasets sintéticos
Da mesma forma que o Data Augumentation ajuda a melhorar o aprendizado da rede com poucos exemplos, um Dataset Sintético ajuda a gerar
exemplos automaticamente para o treinamento da rede.

São poucas situação em que dá pra usar datasets sintéticos, uma delas é para reconhecimento de caracteres (*OCR*) por exemplo, mas quando
é possível os ganhos são enormes, pois dá pra gerar um modelo extremamente robusto e eficaz.

O Eyeflow.AI é uma plataforma expansível, que permite ao usuário a criação de seus próprios componentes de redes neurais e geração de datasets
sintéticos.

## Para onde devo ir agora?

* [Parâmetros de Treinamento](/docs/concepts/training/train_parms): Parâmetros gerais para treinamento da rede neural
* [Parâmetros de Redes Neurais](/docs/concepts/training/dnn_parms): Parâmetros específicos da rede neural
* [Parâmetros de Expansão de Dados](/docs/concepts/training/data_augmentation_parms): Parâmetros para expansão de dados - Data Augmentation
