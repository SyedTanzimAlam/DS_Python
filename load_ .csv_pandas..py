"""@author: Tanzim"""
# Load CSV using Pandas
import pandas as pd
filename = 'PUT THE.csv file'
colnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataset = pd.read_csv(filename, names=colnames)
print(dataset.shape)