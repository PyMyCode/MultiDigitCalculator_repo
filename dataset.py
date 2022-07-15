#~~~1. Data set ~~~

import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
import seaborn as sns

np.random.seed(2)

'load the dataset'
dataset = pd.read_csv("...\\dataset.csv")

'creating label'
y = dataset["label"]

'dropping label'
X = dataset.drop(labels = ["label"], axis = 1)

'deleting dataset to reduce memory usage'
del dataset

'overview of dataset'
g = sns.countplot(y)
y.value_counts()

'Grayscale normalization to reduce the effect of illumination differences.'
X = X / 255.0

'reshaping the dataset to fit standard of a 4D tensor of shape [mini-batch size, height = 28px, width = 28px, channels = 1 due to grayscale].'
X = X.values.reshape(-1,28,28,1)

'categorical conversion of label'
y = to_categorical(y, num_classes = 14)

'90% Training and 10% Validation split'
random_seed = 2
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size = 0.1 , random_state = random_seed, stratify = y)