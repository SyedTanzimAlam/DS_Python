"""@author: Tanzim"""
# Univariate Density Plots
import matplotlib.pyplot as plt
import pandas as pd
filename = "PUT THE .csv file"
colnames = ['Column names in quotes seperated by comma']
dataset = pd.read_csv(filename, names=colnames)
dataset.plot(kind='density', subplots=True, layout=(3,3), sharex=False)
plt.show()