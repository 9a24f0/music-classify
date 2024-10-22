# Music Genre Classification

The project is attempt to classify music genre using 4 approaches:
- Multiclass classification using Support Vector Machines (MCSVM)
- K-means clustering (KMC)
- K-nearest neighbors (KNN)
- Convolutional neural networks (CNN)

## Data set
The dataset being used in this project is [GTZAN Genre Collection](http://marsyas.info/downloads/datasets.html).

> The dataset consists of 1000 audio tracks each 30 seconds long. It contains 10 genres, each represented by 100 tracks. The tracks are all 22050Hz Mono 16-bit audio files in .wav format.

## Methods
### Multiclass Classification using Support Vector Machines(SVM)
`folder: /mcsvm`

***Multiclass Classification:***

Classify an instance as only one of three or more classes.

***Support Vector Machines:***

[SVM](https://www.baeldung.com/cs/ml-support-vector-machines) is a supervised machine learning algorithm that helps in classification or regression problems. It aims to find an optimal boundary between the possible outputs.

Simply put, SVM does complex data transformations depending on the selected kernel function and based on that transformations, it tries to maximize the separation boundaries between your data points depending on the labels or classes you’ve defined.

***Multiclass Classification using SVM***

In its most simple type, SVM doesn’t support multiclass classification natively. It supports binary classification and separating data points into two classes. For multiclass classification, the same principle is utilized after breaking down the multiclassification problem into multiple binary classification problems.

### K-mean clustering
`folder : /kmc`

K-mean clustering is unsupervised learning type, using unlabeled data. This method is simpler compared to NN, but less precision since the data used is unsupervised. The method take each genre as a cluster. The centroid of a cluster is a collection of feature values which are the resulting of the genre.
### K-nearest neighbors
`folder : /knn`

K-Nearest Neighbors is a popular machine learning algorithm for regression and classification. It makes predictions on data points based on their similarity measures i.e distance between them. The KNN algorithm uses ‘feature similarity’ to predict the values of any new data points. This means that the new point is assigned a value based on how closely it resembles the points in the training set.

### Convolutional neural networks
`folder : /cnn`

Convolutional neural networks (CNNs) are made up of layers of neurons that have learnable weights and biases. Each neuron receives some inputs, performs a dot product and optionally follows it with a non-linearity.

The architecture of CNN (not including *input layer*) commonly contains 3 type of layers : convolutional layer, pooling layer and fully-connected layer(output). Some may contains normalization layer. The most simple CNN architecture is:
```
INPUT -> CONV -> POOL -> FC
```
