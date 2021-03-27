---
title: "Conceitos"
linkTitle: "Conceitos"
weight: 4
description: >
  Entenda os principais conceitos do Eyeflow e Vídeo Analytics
---

# Conceitos

-   **Epoch** in terms of artificial neural networks, an epoch refers to one
    cycle through the full training dataset. Usually, training a neural network
    takes more than a few epochs. ... With a neural network, the goal of the
    model is generally to classify or generate material which is right or wrong.

-   **steps_per_epoch** the number of batch iterations before a training epoch
    is considered finished. If you have a training set of fixed size you can
    ignore it but it may be useful if you have a huge data set or if you are
    generating random data augmentations on the fly, i.e. if your training set
    has a (generated) infinite size. If you have the time to go through your
    whole training data set I recommend to skip this parameter.

-   **batch_size** determines the number of samples in each mini batch. Its
    maximum is the number of all samples, which makes gradient descent accurate,
    the loss will decrease towards the minimum if the learning rate is small
    enough, but iterations are slower. Its minimum is 1, resulting in stochastic
    gradient descent: Fast but the direction of the gradient step is based only
    on one example, the loss may jump around. batch_size allows to adjust
    between the two extremes: accurate gradient direction and fast iteration.
    Also, the maximum value for batch_size may be limited if your model + data
    set does not fit into the available (GPU) memory.

-   **validation_steps** similar to steps_per_epoch but on the validation data
    set instead on the training data. If you have the time to go through your
    whole validation data set I recommend to skip this parameter.

-   **Stop condition:** In order to support both distributed and non-distributed
    configuration reliably, the only supported stop condition for model training
    is train_spec.max_steps. If train_spec.max_steps is None, the model is
    trained forever. Use with care if model stop condition is different. For
    example, assume that the model is expected to be trained with one epoch of
    training data, and the training input_fn is configured to throw
    OutOfRangeError after going through one epoch, which stops the
    Estimator.train. For a three-training-worker distributed configuration, each
    training worker is likely to go through the whole epoch independently. So,
    the model will be trained with three epochs of training data instead of one
    epoch.

-   **Max Boxes -** Maximum number of boxes in detection

-   **Test Size -** Percent of exemples selected for final test

-   **Expand Boxes -** Percent to expand size of boxes in detection

-   **Val Size -** Percent of exemples selected for Validation

-   **IoU Detection Threshold -** Minimum threshold for IoU detection

-   **Confidence Threshold –** Minimum confidence threshold for valid detection
