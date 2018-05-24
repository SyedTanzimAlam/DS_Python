"""@author: Tanzim"""
# Load CSV from URL using NumPy
from numpy import loadtxt
from urllib import urlopen
url = 'PUT THE url'
open_dataset = urlopen(url)
dataset = loadtxt(open_dataset, delimiter=",")
print(dataset.shape)