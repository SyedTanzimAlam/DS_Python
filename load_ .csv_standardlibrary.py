"""@author: Tanzim"""
# Loading a .csv file using Python Standard Library
import csv
import numpy as np
filename = 'PUT THE .csv file'
open_dataset = open(filename, 'rb')
read_dataset = csv.reader(open_dataset, delimiter=',', quoting=csv.QUOTE_NONE)
dataset = list(read_dataset)
dataset = np.array(dataset).astype('float')
print(dataset.shape)