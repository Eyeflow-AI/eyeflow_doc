---
date: 2021-04-02
title: "Video Analytics with Deep Learning can be a easy task"
linkTitle: "Announcing Eyeflow.AI"
description: "How 4 years of pitfalls drive us to developer a great tool for the job"
author: Alex Sobral de Freitas ([@alexsobral](https://alexsobral.medium.com))
resources:
- src: "**.{png,jpg}"
  title: "Image #:counter"
  params:
    byline: "Photo: Ronaldo de Oliveira / Unsplash"
---

**Announcing Eyeflow.AI**

{{< imgproc featured-bridge-and-trees.jpg Fill "600x300" />}}

In 2016 I was invited by a friend for a challenge to develop a video analytics solution for a large Brazilian mining company. I have always been passionate about artificial intelligence. I have been following the topic since 1995, and was looking for applications for machine learning and deep learning since 2011, so I took the challenge right away.

> The task seemed quite complex: capturing images of ore transport wagons using video cameras to automate the components inspection and detect failures.

I’m a very skilled developer with 35yrs of experience, the more complex the task, the more excited I get.

I choose the Theano framework and SSD architecture for the Neural Network, setup the environment test if was all working. Then I took the wagon movie shot from a cell phone, extracted some frames, made a small python program that would allow me to annotate the boxes by drawing on the frames, and start to train the network with my simple dataset. After two weeks of hard work and several difficulties always present in open-source programs I was able to see the network training and detecting the objects in my dataset.

After show this small Proof of Concept to the customer, we started a pilot project that would detect the objects with a camera next to the railroad. It was 3 months of painstaking work, but in the end we managed to show the results to the client, who was very impressed with the solution.

This experience enlightened me. Deep learning was a very new technology with the ability to solve a whole class of new problems that are unsolvable by traditional algorithms. However, it was extremely laborious, and difficult to master. So, there was a space for a tool that simplify and streamline the development of Video Analytics applications. I had been looking for an idea to develop a product for years, and had finally found it.

> Introducing EyeFlow, a complete platform for the development and hosting of Video Analytics applications, oriented to be easy to learn, practical to use and fully extensible. From developers to developers.

![Eyeflow.AI](/logo-eyeflow-wide.png)

In the last 3 years we have developed several Video Analytics projects for large companies, some of which are in mission critical operations doing the final inspection of vehicles produced in a big car manufacturer. All of these projects we are developing using the EyeFlow platform, and now we decided to open this technology so that other companies and developers can also build applications and projects using video analytics.

We aim that our products can democratize the use of deep learning for building commercial applications and promote the development of applications for automation of repetitive tasks that can be performed by AI algorithms.

And above all, we want to share our experience with Video Analytics so that others will also be successful in the execution of their projects. I started writing here to promote our product, but also to be able to share knowledge and experience. I hope to be able to do this continuously.

Right now we are launching our platform in a private beta, but we hope to be able to open it soon for everyone who wants to try it.
