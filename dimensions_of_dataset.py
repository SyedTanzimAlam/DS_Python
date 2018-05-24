"""@author: Tanzim"""
# Dimensions of your data
import pandas as pd
filename = "PUT THE .csv file"
colnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataset = pd.read_csv(filename, names=colnames)
shape = dataset.shape
print(shape)