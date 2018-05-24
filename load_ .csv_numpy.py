"""@author: Tanzim"""
# Load CSV using NumPy
from numpy import loadtxt
filename = 'PUT THE .csv file'
open_dataset = open(filename, 'rb')
dataset = loadtxt(open_dataset, delimiter=",")
print(dataset.shape)