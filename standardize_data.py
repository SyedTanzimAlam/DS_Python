"""@author: Tanzim"""
# Standardize data (0 mean, 1 stdev)
import pandas as pd
filename = "PUT THE .csv file"
colnames = ['Column names in quotes seperated by comma']
dataset = pd.read_csv(filename, names=colnames).values
# separate array into input and output components
X = dataset[:,0:8] # rows:columns
Y = dataset[:,8]
# Add standard fit
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler().fit_transform(X)
# summarize transformed data
import numpy as np
np.set_printoptions(precision=3)
print(scaler[0:5,:])