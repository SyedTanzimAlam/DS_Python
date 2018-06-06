"""@author: Tanzim"""
# Skew for each attribute
import pandas as pd
filename = "PUT THE .csv file"
colnames = ['Column names in quotes seperated by comma']
dataset = pd.read_csv(filename, names=colnames)
skew = dataset.skew()
print(skew)