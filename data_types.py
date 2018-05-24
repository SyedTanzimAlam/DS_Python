"""@author: Tanzim"""
# Data Types for Each Attribute
import pandas as pd
filename = "PUT THE .csv file"
colnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataset = pd.read_csv(filename, names=colnames)
types = dataset.dtypes
print(types)