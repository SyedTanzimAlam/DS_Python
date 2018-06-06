"""@author: Tanzim"""
# Correlation Matrix Plot(generic)
import matplotlib.pyplot as plt
import pandas as pd
filename = "PUT THE .csv file"
colnames = ['Column names in quotes seperated by comma']
dataset = pd.read_csv(filename, names=colnames)
correlations = dataset.corr()
# plot correlation matrix
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
plt.show()