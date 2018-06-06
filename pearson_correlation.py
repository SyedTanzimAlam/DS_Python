"""@author: Tanzim"""
# Pairwise Pearson correlations
import pandas as pd
filename = "PUT THE .csv file"
colnames = ['Column names in quotes seperated by comma']
dataset = pd.read_csv(filename, names=colnames)
pd.set_option('display.width', 100)
pd.set_option('precision', 3)
correlations = dataset.corr(method='pearson')
print(correlations)