---
title: "Flow"
linkTitle: "Flow"
weight: 2
description: >
 Flow diagram for image processing and decision making
---

Flow is a program in low-code format, built with code components, oriented to the decomposition of image data (*unstructured*) into output data (*structured*).

**Flow is structured as an input-output process.**

The input is a stream of images, such as:
- Camera: Industrial, Security, IP
- Cell
- Video Archive

The output can be for any other data system such as:
- Files: JSON, CSV, TXT
- Databases: MongoDB, Postgres
- Message queues: RabbitMQ, AMQP
- Controllers: PLC, IC, TCP, RS-232
- Sending alarms: E-mail, SMS, Notifications

As Eyeflow is an extensible platform, there are no limits to component creation. It is possible to quickly create a Python component and use it in Flow to perform the desired function.

Between input and output, image processing is done in Neural Network components. Each of these components will be linked to a dataset, and will use the model trained with the dataset to run in production.

It is also possible to use components that send the images for processing in services of cloud providers. For example, using a component that takes the image of a document and sends it to Google's character recognition API, and then processes the response to scan that document.

Creating a Flow is a very simple process.
#### Click on the Flow tab in the navigation bar
It will open the screen to load a Flow or Create a new one. Clicking on **New Flow** will open a screen to enter the data. Just fill in the data and that&#39;s it, Flow will be created.

![Criar Flow](/screenshots/pt-br_create_flow.jpg#bordered "Criar Flow")

After creating the Flow we will add some components to create a simple flow that identifies the Pet in the image.
### Let's add 3 components to this Flow:
#### 

![Componente Camera IP](/screenshots/pt-br_flow_camera_ip.jpg#bordered "Componente Camera IP")

#### 

![Componente ROI Cutter](/screenshots/pt-br_flow_roi_cutter.jpg#bordered "Componente ROI Cutter")

#### 

![Componente File Save](/screenshots/pt-br_flow_file_save.jpg#bordered "Componente File Save")

#### Connect the outputs of each component to the input of the next

![Flow Completo](/screenshots/pt-br_flow_basic.jpg#bordered "Flow Completo")

**Ready! Flow is complete.**

One of the great advantages of the EyeFlow.AI platform is that it is a complete integrated environment for the development of Video Analytics applications. The process of neural networks requires a fair amount of annotated examples in order to learn, and the easiest way to get these examples is to use videos.

So, the development process involves a cycle of activities:
1. Test the video in Flow by checking if the application is marking the video correctly
2. Identify the errors that the application is making and go in the datasets
3. On the **New Examples** screen, look for frames where the neural network did not correctly identify the object
4. Add several examples of error (30 to 50 in each cycle is a good number)
5. Note the new examples by correcting errors
6. Train the neural network and check the assertiveness indicators to see if the network is learning well
7. After training, go back to test the video again

After having good results in the annotations of the videos, our Flow is ready to publish on the edge.

## Where should I go now?

* [Dataset](/docs/concepts/dataset/)
* [Training](/docs/concepts/training/)
