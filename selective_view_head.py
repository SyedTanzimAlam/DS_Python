"""@author: Tanzim"""
# View first 20 rows
import pandas as pd
filename = "PUT THE .csv file"
colnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataset = pd.read_csv(filename, names=colnames)
view_dataset = dataset.head(20)
print(view_dataset)