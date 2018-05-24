"""@author: Tanzim"""
# Class Distribution
import pandas as pd
filename = "PUT THE .csv file"
colnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataset = pd.read_csv(filename, names=colnames)
class_counts = dataset.groupby('class').size()
print(class_counts)