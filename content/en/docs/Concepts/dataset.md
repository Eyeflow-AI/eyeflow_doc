---
title: "Dataset"
linkTitle: "Dataset"
weight: 3
description: >
 Set of annotated examples for training neural networks
---

<!-- {{< note >}}  {{< /note >}} -->
A dataset is a set of annotated examples that serve to instruct a neural network about what is desired to be recognized in the images. In the dataset set of images, we will have several different examples of the objects we want to identify or recognize. These examples will feed the training of the neural network so that the common pattern between them can be identified.

## Dataset types
Datasets can be of several types. The most used in Eyeflow are:
* [ObjectDetection](#objectdetection)
* [Classification](#classification)
* [AnomallyDetection](#anomallydetection)
* [InstanceSegmentation](#instancesegmentation)

Each type of dataset has a different annotation, and a different type of output.

### ObjectDetection
ObjectDetection datasets are often the most used for their versatility and ease of annotation. The objective is to identify a specific object in a large image, delimiting a rectangular area around the object. Your annotation is usually very simple and quick, as you just click and drag a rectangle (*box*) and define which class of the object. It is executed by a type of neural network that can be quite optimized for execution at the edge, reaching hundreds of FPS in real time.

### Classification
Classification datasets are the most common, and were the first to appear in the DeepLearning universe. It basically identifies an image as being one of N classes. For example, if you have a list of cat images, you can define the breed of each one, and the neural network will learn to identify the breed in any image.

### AnomallyDetection
{{< note >}}
This is a dataset still in the experimental phase.
{{< /note >}}

The AnomallyDetection dataset is designed to identify anomalies in images of the same object. The idea is to feed the dataset with many images of the &quot;correct&quot; object and thus the neural network learn the good pattern. When the neural network is presented to an image of an object that has a difference from the good pattern (anomaly), it will point out the anomaly.

### InstanceSegmentation
{{< note >}}
This is a dataset still in the experimental phase.
{{< /note >}}

InstanceSegmentation is a dataset that has become popular in recent years due to its intense use in autonomous vehicle systems and AI systems for medicine. It is about identifying the object, along with all its outline pixel by pixel. Its output is quite impressive, since it allows you to &quot;cut&quot; the object in detail in the background of the image, however, its annotation is extremely laborious, usually requiring a large team of people to generate an adequate set of annotated images for training.

## Creating a dataset
#### Creating a dataset is a very simple task. Just click on the side menu in **New Dataset**.

![Criar Dataset](/screenshots/pt-br_create_dataset.jpg#bordered "Criar Dataset")

#### A screen will open to enter data from the dataset.

![Criar Dataset](/screenshots/pt-br_create_dataset_modal.jpg#bordered "Criar Dataset")

Just fill in the Name and Description, choose the type and define which Application the dataset belongs to. Then you need to add at least one class.

## Classes
The goal of the neural network will be to identify a pattern in the image, and output it in data format. Thus, we created classes in the dataset to be able to use to mark the images, and thus teach the neural network to recognize these patterns and inform us which class was recognized. For example, if we have several images of examples of dogs and cats, and we want to know if it is one or the other in the image, we have created two classes:

![Criar Classes](/screenshots/pt-br_create_classes_modal.jpg#bordered "Criar Classes")

The colors chosen will help to annotate the dataset, and will appear in the annotation of the videos.

## Examples
Examples are annotated images that will instruct the neural network in learning pattern recognition. We insert several images in the dataset from frames of a video or photos, and then write down in each of these images what is desired to be recognized. The simplest and fastest way to add new examples is to extract sample videos. When playing a video in a Flow, the tool extracts some of the frames from the video and makes them available on the New Examples screen.

![Menu Novos Exemplos](/screenshots/pt-br_menu_new_examples.jpg#bordered "Menu Novos Exemplos")

On this screen it is also possible to upload new examples from images located on the computer.

![Inserir Novos Exemplos](/screenshots/pt-br_insert_new_examples.jpg#bordered "Inserir Novos Exemplos")

{{< tooltip >}}
For a neural network to learn well it is important that there is a good diversity of examples. Inserting several very similar images, or inserting many images of a class and few of the others will cause the dataset to become unbalanced and the network will not learn well
{{< /tooltip >}}

## Annotation
Annotation is the process where the user marks the object in the image that he wants to be identified, thus generating an example that will be used in the training of the neural network.

The annotations are different for each type of dataset. In a dataset [ObjectDetection](#objectdetection)

![Anotar Exemplo](/screenshots/pt-br_annotate_example.jpg#bordered "Anotar Exemplo")




## Where should I go now?

* [Training](/docs/concepts/training/)
* [Flow](/docs/concepts/flow/)
