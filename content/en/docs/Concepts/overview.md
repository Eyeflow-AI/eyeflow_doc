---
title: "Overview"
linkTitle: "Overview"
weight: 1
description: >
 Main concepts of Eyeflow.AI
---

## Application
Set of elements that implement a complete Video Analytics process.

When we are faced with a problem that involves vision we start to think about how we can solve it using Eyeflow. At the entrance we have the capture of images by an industrial camera or a cell phone, and at the exit we want to have these images analyzed and interpreted, so that actions can be taken in response. This solution to the problem is what we call Application.

## Flow
Set of chained components that implement an application.

In the process of building an application the goal is to transform a video input (*unstructured data*) into a programmed action (*structured data*). In this process we will use neural networks and other chained software components to be able to decompose and interpret the input images and generate the desired outputs.

## Neural Network
Advanced mathematical algorithm that allows the computation of unstructured data.

Neural networks are computational elements that have been developed since the 1960s, inspired by scientific research on the functioning of the brain (*neurons*).

As of 2010, with advances in mathematical processing algorithms and approximation of algebraic functions, together with the increase in the capacity of mathematical processors and lower prices due to their popularization in graphics cards for games (*GPU*), neural networks have evolved to be used multilayer (*Deep Neural Network*). In this way, several new applications of this technology began to emerge in the solution of complex problems, mostly related to unstructured data, such as sounds and images. Neural networks are the fundamental components of Flow, as they allow the solution of complex computer vision problems, which previously were not amenable to being solved using traditional algorithms.

Neural networks have the ability to converge mathematically to a computational model that identifies patterns in the data. This ability allowed the emergence of Artificial Intelligence solutions that learn from examples that the user delivers to the network.

## Dataset
Set of examples that instruct the learning of the neural network.

A neural network is like a black box where we insert examples at the entrance and say what we want to have at the exit. Thus, the user must generate a set of these examples, annotated with the desired output, which will serve as data for training the neural network in the execution of the task.

## Training
Computational process to converge a neural network for learning patterns.

After we have an annotated dataset we put the neural network algorithms to process these examples until it learns how to generate the desired output. The training seeks to reduce the error measured between what the neural network presented in the output in relation to the example annotation made by the user. When this error is reduced, the neural network will be ready to process new data.

## Model
Neural network trained with a dataset.

After the training process, a model is generated, which can then be used in Flow to process the images and generate the desired outputs.

## Edge
Computational device that performs a flow in production.

After a flow is developed, tested and showing good results, it can be published for execution on a device that will start to work in production, such as the detection of a defect in the manufacturing line.

## Where should I go now?

* [Dataset](/docs/Concepts/dataset/)
* [Flow](/docs/Concepts/flow/)
