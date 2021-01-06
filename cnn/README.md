# Music Genre Classification using CNN:

## 1. Extract MFCC features
Since `librosa` provided buildt-in function for extracting MFCCs. The work is only to try the parameters that works for the project. In this project, the params are:
- `signal`: the audio load from dataset
- `sample_rate`: 22050 (default)
- `n_mfcc`: 13 (default was 20)
- `n_ftt`: 2048 (default)
- `hop_length`: 512 (default)

The extracted MFCCs are then labeled and dumped into `data.json` for the ease of using.

## 2. Create the neural network
With the help of `tensorflow.keras`, the network is built as:
- **3 convolutional layers**:
  - `Conv2D`: 2D convolutional layer
  - `Maxpooling2D`: help extracts the sharpest features
  - `BatchNormalization()`: speed up training and more reliable model
- **Dense layer**:
  - `Flatten()`: convert from 2D to 1D layer
  - `Dropout()`: improve network robustness (network can rely too much on specific neuron)
- **Output layer**

## 3. Prepare the data
Split the data into:
- **train set**: 60% of the dataset
- **test set**: 25% of the dataset
- **validate set**: 15% of the dataset

## 4. Train the data with CNN model
The model is compiled with:
- `optimizer`: Adam optimizer (stochastic gradient descent method)
- `learning_rate`: 0.0001 (tried to avoid overfitting)
- `loss`: `sparse_categorical_crossentropy` (as classes is mutually exclusive and samples can have soft probabilities labels)
- `metrics`: `accuracy` (as we use accuracy to evaluate the performance of the model)

## 5. Evaluate the model
The model is evaluated by train/test accuracy and train/test loss. The figure is plotted to illustrate whether the model is suffering from overfitting or underfitting.