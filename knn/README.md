# K-nearest neighbors

## Steps to build Music Genre Classification using KNN:

#### 1. Define a function to get the distance between feature vectors and find neighbors
Calculate distance between feature vectors so that we can find the k-neighbors by selecting k subsets with the smallest distance

#### 2. Identify the nearest neighbors
From the neighbors get the nearest one. These k-neighbors already have their classes labeled, so we will do the majority voting. So out of these k-neighbors, we directly see the majority class and whatever be the majority class, becomes the predicted class

#### 3. Define a function for model evaluation    
Calculate the accuracy of the predictions `accuracy = 1.0*correct/len(testSet)`

#### 4. Extract features from the dataset and dump these features into a binary .dat file “my.dat”
Using MFCC (Mel Frequency Cepstral Coefficients)
* Divide the signals into smaller frames. Each frame is around 20 ms long
* Identify different frequencies present in each frame
* Separate linguistic frequencies from the noise
* To discard the noise, it then takes discrete cosine transform (DCT) of these frequencies. Using DCT we keep only a specific sequence of frequencies that have a high probability of information
 
#### 5. Train and test split on the dataset

#### 6. Make prediction using KNN and get the accuracy on test data
