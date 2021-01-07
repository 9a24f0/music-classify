# Music Genre Classification using KMC:
## 1.KMC - K-means cluster method
- Unsupervised learning
- Each cluster represent for each genre

## 2. Extract MFCC features
Using `librosa` librosa to extract the data set, the dataset used is `gtzan` dataset

## 3. Create the K-means cluster
- Using `parseAudio` function,reading the file extracted by MFCC
- Labels different genres as subDir

## 4. Prepare the data
Split the data into:
- **train set**: 80% of the dataset
- **test set**: 20% of the dataset

Using 100% dataset give much lower rate than other method

## 5. Train the data with KMC model

## 6. Evaluate the model
The model is evaluated by train/test accuracy.
The accuracy is inconsistent as we continuously run the script since cluster might differs with different mfcc train sets
