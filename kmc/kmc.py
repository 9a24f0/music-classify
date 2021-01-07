import glob
import os
import librosa
import numpy as np
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# change data path here
DATA_PATH = "../data/genres"


def featureExtraction(fileName):
    raw, rate = librosa.load(fileName)
    mfcc = np.mean(librosa.feature.mfcc(y=raw,sr=rate,n_mfcc=13).T, axis=0)
    return mfcc


# Takes parent directory name, subdirectories within parent directory, and file extension as input.
def parseAudio(parentDirectory, subDirectories, fileExtension="*.wav"):
    features, labels = np.empty((0,13)), np.empty(0)
    for subDir in subDirectories:
        for fn in glob.glob(os.path.join(parentDirectory, subDir, fileExtension)):
            mfcc = featureExtraction(fn)
            tempFeatures = np.hstack(mfcc)
            features = np.vstack([features, tempFeatures])
            # pop = 1, classical = 2, metal = 3, rock = 0
            if subDir == "pop":
                labels = np.append(labels,1)
            elif subDir == "classical":
                labels = np.append(labels,2)
            elif subDir == "metal":
                labels = np.append(labels,3)
            else : # Corresponds to "rock"
                labels = np.append(labels,0)
    return np.array(features), np.array(labels, dtype=np.int)



subDirectories = ["pop", "classical", "metal", "rock"]
# Traning Labels [1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 0 0 0 0 0 0 0 0]
X, y = parseAudio(DATA_PATH, subDirectories)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


###################### Training Loop ######################################

model = KMeans(n_clusters=4)
model.fit(X_train)

###################### Test Results ###################################

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_pred, y_test)
print("y_pred: {}\n".format(y_test))
print("y_test: {}\n".format(y_test))
print("Predict accuracy:", accuracy)

# please delete these comment and add to your colab, rephrasing is your work:
# the accuracy is inconsistent as we continuously run the script
# since cluster might differs with different mfcc train sets

