"""@author: Tanzim"""
# Scatterplot Matrix
import matplotlib.pyplot as plt
import pandas as pd
filename = "PUT THE .csv file"
colnames = ['Column names in quotes seperated by comma']
dataset = pd.read_csv(filename, names=colnames)
pd.scatter_matrix(dataset)
plt.show()