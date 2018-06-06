"""@author: Tanzim"""
# Univariate Histograms
import matplotlib.pyplot as plt
import pandas as pd
filename = "PUT THE .csv file"
colnames = ['Column names in quotes seperated by comma']
dataset = pd.read_csv(filename, names=colnames)
dataset.hist()
plt.show()