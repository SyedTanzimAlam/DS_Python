"""@author: Tanzim"""
# Load CSV using Pandas from URL
import pandas as pd
url = 'PUT THE url'
colnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataset = pd.read_csv(url, names=colnames)
print(dataset.shape)