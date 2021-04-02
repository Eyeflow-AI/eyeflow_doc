---
title: "Overview"
linkTitle: "Overview"
weight: 1
description: >
 Training overview
---

Training is the process where the examples from the dataset are fed into the neural network to learn the patterns and generate the model. It is a complex mathematical / algorithmic process, which requires a large computational capacity and needs to run on servers with GPU or TPU graphics cards in the case of the Google cloud.

This process is performed in an iterative way, seeking to minimize the error measured between what the neural network presented in the output and the annotation made in the example by the user. Throughout the error minimization process, the neural network&#39;s assertiveness is measured, so that the user can verify if the neural network has really learned to identify the patterns.

The process of training neural networks is quite complex, and mastering this process well takes a lot of time, study and experimentation.

Fortunately, Eyeflow.AI offers a complete environment to accelerate and automate all tasks for the development of neural networks, and has suggestions for construction and parameterization, the result of long years of experience using neural networks to solve real problems.

## Important concepts

### Number of examples
The number of examples of a dataset is a very important item for the effectiveness of the detections. To perform a training of a neural network it is necessary at least 10 examples, and a good dataset for production will require about 1000 examples. However, there is no point in simply filling up a dataset of examples without testing its effectiveness with real cases, as an excess of similar examples can unbalance learning and cause your model to be biased and not perform well in production.

Another important point is that a similar number of examples from each class must be maintained, also to avoid imbalance, and consequently bias, of the model. If the dataset has many examples of a single class and few of the others, it will tend to detect everything as the dominant class.

The best strategy for adding new examples to the dataset is to test it after training and check for errors, to add only the new examples that showed errors, and then correct them and do a new training. At each of these iterations, the ideal is to add 30 to 50 new examples, and from there the training will quickly increase the assertiveness of detection.

After testing with videos and publishing in production, Eyeflow offers a mechanism for collecting new examples from the edge, which will serve to check if the model is having a good assertiveness in real cases, and then errors can be added to continue the process of improving the dataset.

### Quality of the examples
If quantity is important, quality is critical to ensuring that the neural network will learn to detect patterns.

To guarantee the quality of the examples, some points must be observed:
- The object to be detected must be clearly visible in the image. If there are doubts to note the example then the neural network itself will have difficulties in learning from that example. - For an ObjectDetection dataset, the boxes cannot be too small or too large. The augmentation tests will indicate whether the boxes are being well detected. - For a Classification dataset, the examples need to be quite different between classes. It will be difficult to detect a difference between classes if that difference is just a small detail in the total image. - There should be a good variety in the examples. The addition of many very similar examples will cause the model to be skewed to detect only that type of image or class.

### Validation and Testing
In the training process, the dataset is divided into 3 groups:
- Training
- Validation
- Test

The separation of the examples for the groups is done at random, based on the parameters defined for the training.

The **Training** group is what will be effectively used to train the neural network. It should have the largest number of examples, with at least 80% of the examples recommended.

The **Validation** group is used to test the model at each end of the season, and is used to check if the training is evolving, or has become stagnant or addictive (*overfitting*). It is recommended that 10% of the examples be up to a maximum of 100 examples.

The **Test** group is used to test the model at the end of training. As these examples were never presented to the dataset, they serve as a final assessment of learning, defining the assertiveness that the model presents. It is an indicator of whether the neural network has effectively learned to recognize patterns. It is recommended that 10% of the examples be up to a maximum of 100 examples.

{{< note >}}
The main objective of a neural network training is to ensure that the final model will **generalize**, it means that you will learn from the pattern the examples so that you can extrapolate to new examples in real situations. Often the result is good in training, but poor in production, indicating that the model did not generalize well. In these situations, you should collect more examples of errors in production to add to the dataset.
{{< /note >}}

### Loss and Val Loss
Loss is the measure of error observed in the training process between what the neural network detected (*predict*) and what should be the correct output according to the annotation (*ground thruth*). The mathematical / algorithmic training process of neural networks seeks to minimize this error.

Val Loss is the same measure, only done in the validation group at the end of a season. It serves to monitor the evolution of training at each training cycle.

### mAP and Accuracy
The training quality indicator is a measure of correctness that takes into account all the elements of output. Each type of dataset has its standard measure of assertiveness.

*Datasets* ObjectDetection *usually use**mAP**(* Mean Average Precision*) as an assertiveness indicator, as it measures how much the output box encompasses the object well, indicating the correct class, by the average of all classes. *Datasets* Classification *usually use**Accuracy**, which is the percentage of examples in which the neural network correctly predicted which class the object belongs to.

### Overfitting
It is a phenomenon that occurs with an increase in training. It occurs in training when we see *Loss*continue to fall, but* Val Loss * goes up instead of going down. This indicates that the neural network has become &quot;addicted&quot; to the training examples and has stopped generalizing to new examples, that is, it has learned a lot about the training examples, but is unable to get new examples right.

### Expanding examples - Data Augmentation
It is a long and repetitive job to write down the examples of a dataset, but it is the most important task to be able to use a neural network in a real application. Many AI projects stagnate in the part where they need to gather many thousands of annotated examples to start having good results with neural networks, but the experience with Eyeflow.AI indicates that it is possible to have good results with just 300 examples in a dataset, and great results with just 1000 examples. One of the key aspects of this performance is in Data Augmentation.

Data Augmentation is the process of inserting disturbances in the images of the examples, at the time of training, to force the neural network to learn the patterns of the objects, and not to be &quot;addicted&quot; to the few examples that were presented.

Eyeflow.AI offers a wide range of algorithms for Data Augmentation, ranging from geometric and photometric distortions in images to the insertion of noise or strange elements.

The important point to note here is that Data Augumentation should not be used to modify the examples, leaving them very different from the situations that will be encountered in the real environment, as this will unnecessarily hamper the learning of the network. For example, it would not make sense in a car dataset to insert the *Flip Vertical*, as we will not find a situation with the car upside down.

### Synthetic Datasets
In the same way that Data Augumentation helps to improve the learning of the network with few examples, a Synthetic Dataset helps to generate examples automatically for the training of the network.

There are few situations in which you can use synthetic datasets, one of them is for character recognition (*OCR*) for example, but when it is possible the gains are enormous, as you can generate an extremely robust and effective model.

Eyeflow.AI is an expandable platform, which allows the user to create their own neural network components and generate synthetic datasets.

## Where should I go now?

* [Training Parameters](/docs/concepts/training/train_parms)
* [Parameters of Neural Networks](/docs/concepts/training/dnn_parms)
* [Data Expansion Parameters](/docs/concepts/training/data_augmentation_parms)
