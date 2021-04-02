---
title: "First Flow"
date: 2021-03-26
weight: 4
description: >
 Tutorial 1 - Build your first flow
---

>   This training will be based on a use case, for this case, a video is available to be used for training the neural network, which will have the objective of detecting the Nut element, identifying its faces (smooth face and prospecting face)

## Use Case: Detection and Identification of the Face of Sows

### Objective:
Identify the face of the sows, informing if the face is smooth or if the face is prospecting

![Porca](/screenshots/ec5e47ae04a38e9fdf615ecc47ccb97d.png "Porca face lisa")

## Follow the steps below

###  Login - Enter the EyeFlow platform

Access:

```
https://app.eyeflow.ai
**Usuario**: treinamento
**Senha**: Teste
```
![](/screenshots/54452b239b80e31c2b115e38884a828f.png)

## Application

Application is a subdirectory, an area made available in the tool, in which the user can create his projects (applications) to run on the neural network.

#### Click on the Application Tab

![](/screenshots/278595a445b84611c12da54e179d4a85.png)


#### Create a new application by pressing the \ &lt;+ \&gt; button

![](/screenshots/8aa5d0c1d01eab46d7f83cfcf61a024e.png)


#### Create a Named Application \<SERPRO.nome do aluno\>

![](/screenshots/5aeb0464310d01fd998a3330b34ab08a.png)


## Flow

The solution allows the user to create the flow for the execution of the neural network. This solution is based on a Drag and Drop (Drag and Drop) tool that is easy to use, where users can use the components displayed in their Menu.

#### Click on the Flow Tab

![](/screenshots/9624b3918209942bbedc3281fe844f9e.png)


Before creating a flow we will know the existing components in the Tool, in the image we will make a brief description:

![](/screenshots/b9ee846a7bef5d5a7d875987ec191d01.png)


![Câmera IP tipo Box - Planet Ello](/screenshots/ee5978b24eedb262e89aeb7872e05661.jpeg)
**Images of the informed camera models:**

![5MP Camera for NVIDIA Jetson Xavier NX / Nano developer kit](/screenshots/66934571ab2954b852cd3f5c3cc311ab.jpeg)
![](/screenshots/e47655b354ef9adf5ab04391acf39f75.png)

##  Build your Flow

**Input**

#### IP CAMERA - Drag the component into the stream

![](/screenshots/bcaa17768ffda276bfd23eb259fc2126.png)


#### Double Click on the CAMERA IP component, the screen below will appear:

![](/screenshots/cff838b4aeabb285995b06346a14e70e.png)


**Selector**

#### ROI CUTTER - Drag the component to the Flow

![](/screenshots/21d08445d07222cf875416ca0b88be0a.png)


#### Double Click on the ROI CUTTER component, the screen below will appear:

![](/screenshots/337b7304a836759447829c0218facd79.png)


**Follow the steps**

![](/screenshots/8f0d29dda6f9f27221d1e211c5dd27b8.png)


#### Create a new Class, following the step represented below:

![](/screenshots/b58b2a563154be20185941b41f43cf6d.png)


The image below will appear, in this step we will be adding two new classes

![](/screenshots/07fba474794f9334206980b7b17e212a.png)


#### Save the settings made in the ROI CUTTER component

![](/screenshots/e6a94df39e040762c7292296b673e677.png)


#### Make the communication between the IP CHAMBER with ROI CUTTER in the flow

![](/screenshots/55b2a4a94b260d0d95d41a746cf6320f.png)


#### Save Flow: Click on the \ button<Save Flow\>

![](/screenshots/c6d71a06358b7b35cfa5d3ecf4340ea0.png)


##  Upload

![](/screenshots/8f54bde44fd3300b8923ce16c7d6bafc.png)
![Upload](/screenshots/13526a42e6cba74c2ca123581f41d23d.png)

## Upload video
#### Click on the \ button<Teste Vídeo\>
![](/screenshots/4beaed025791a12acf13245f6156b0d7.png)

#### Upload Video test, click on the \ button<UPLOAD VIDEO\>

![](/screenshots/6ff411258db74b91e1ecacf0db27e66e.png)


#### Drag the video to the location you entered

![](/screenshots/2d4a53d3b31d9783e49fc511c615004c.png)


At this moment, a bar will appear showing the video load in the tool

![](/screenshots/626a6c42c6b044d26f05fd704fe91eac.png)


At this point, the solution will be executing its created flow and providing new examples (frames) for its Dataset.

## Dataset
![Flow](/screenshots/036889fd1c08813042e32d9fe50439a9.png)![Dataset](/screenshots/e11aa076d81124afd80c34d4cdfe8d09.png)

![](/screenshots/8f54bde44fd3300b8923ce16c7d6bafc.png)


#### Enter the DATASETS Tab

![](/screenshots/cb0d9f16e443fad19887ac227943415c.png)


The Dataset folder will open

![](/screenshots/2c258bb34ea7d868a9c67fb6a019439d.png)


#### Select frames / images to be trained in the Dataset, click on the selection buttons

![](/screenshots/911c7bcf7b17c08f3c2da836c62e6165.png)


#### Insert the new selected examples, click on the \ button<Insira novos exemplos\>

![](/screenshots/94702afc11390778519bb29e9439d074.png)


#### Return to Dataset Tab

![](/screenshots/a3ac82b770d68bce6bb087659a597bce.png)


#### Click on your created Dataset

![](/screenshots/8f36879c60fbf6b59200f537e27f2605.png)


#### Mark the regions of interest by selecting the Nut with the Smooth Face and the Projection Face

![](/screenshots/c55290311d8113c5c93a917cd5cef3e3.png)


After marking all selected frames click on the \ button<Painel de Treino\>

![](/screenshots/18e3818244e9afbe876baf9392c69560.png)


## Editing Parameters for training the neural network

### Follow the steps below

![](/screenshots/16b5d277d6395f1288ab844a59fbc686.png)


The image below will appear

>  Description of parameters in the tool
![](/screenshots/22c40d8d1c363711e6f5e3a39b924112.png)

## Neural network training
![Flow](/screenshots/036889fd1c08813042e32d9fe50439a9.png)![](/screenshots/8f54bde44fd3300b8923ce16c7d6bafc.png)

![Dataset](/screenshots/e11aa076d81124afd80c34d4cdfe8d09.png)

After editing the parameters of the neural network, we will submit your marked frames for training, where you will execute the flow created.

#### Follow the steps below

![](/screenshots/ee2abb31954fea2099d8790c8dd0429d.png)


A confirmation pop-up will appear on the screen

![](/screenshots/646bc2a77c289b3e681f03f328ecae5a.png)


After this step, a screen will appear with the progress of the training

![](/screenshots/33e934dfaa47afa81bcff852189c6b34.png)


## Test-result

After training the neural network, you will be able to see the training result in the report shown in the image, you will also be able to run the loaded video and observe the result you have achieved, if the result is not satisfactory, the neural network must perform a new training, for this case, we must submit new examples in Datasets, in order to improve the learning of the neural network

![](/screenshots/b3810a2f7f2f9724e96680b013bb77ed.png)


## Video validation

As previously seen in the Flow item, the tool provides a test option on the loaded video.

### Follow the steps below

#### Click on the &lt;&lt;Flow \&gt; Tab

![](/screenshots/ef0e2286e9d11d6f3a8292ad4bfb8c08.png)


#### Follow the steps below

![](/screenshots/db80a153eac05e2394fdd281d30392ed.png)


#### Follow the steps below

![](/screenshots/949318d213279ca64c1db3fe43563b42.png)


After this step you will be able to check the result of your Project on the video, if the result is not satisfactory, the neural network must be submitted to a new training, for this you must perform the steps informed in the item Datasets, this process must occur until the neural network find the satisfactory result.
