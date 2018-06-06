"""@author: Tanzim"""
# binarization
import pandas as pd
filename = "PUT THE .csv file"
colnames = ['Column names in quotes seperated by comma']
dataset = pd.read_csv(filename, names=colnames).values
# separate array into input and output components
X = dataset[:,0:8] # rows:columns
Y = dataset[:,8]
# Add binary fit
from sklearn.preprocessing import Binarizer
binarized = Binarizer(threshold=0.0).fit_transform(X)
# summarize transformed data
import numpy as np
np.set_printoptions(precision=3)
print(binarized[0:5,:])