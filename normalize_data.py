"""@author: Tanzim"""
# Normalize data (length of 1)
import pandas as pd
filename = "PUT THE .csv file"
colnames = ['Column names in quotes seperated by comma']
dataset = pd.read_csv(filename, names=colnames).values
# separate array into input and output components
X = dataset[:,0:8] # rows:columns
Y = dataset[:,8]
# Add normalize fit
from sklearn.preprocessing import Normalizer
normalized = Normalizer(threshold=0.0).fit_transform(X)
# summarize transformed data
import numpy as np
np.set_printoptions(precision=3)
print(normalized[0:5,:])