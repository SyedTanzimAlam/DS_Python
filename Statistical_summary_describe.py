"""@author: Tanzim"""
# Statistical Summary
import pandas as pd
filename = "PUT THE .csv file"
colnames = ['Column names in quotes seperated by comma']
dataset = pd.read_csv(filename, names=colnames)
pd.set_option('display.width', 100)
pd.set_option('precision', 3)
description = dataset.describe()
print(description)