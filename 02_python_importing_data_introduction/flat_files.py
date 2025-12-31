# Flat files
#   - Text files containing records
#   - That is, table data
#   - Record: row of fields or attributes
# File extension
#   - .csv - Comma separated values
#   - .txt Text file
#   - commmas, tabs -Delimiters

# How do you import flat files
#   - Two main packages: NumPy, pandas

# NUMPY
# If all the data is numerical we use NUMPY
#   - NumPy arrays: standard for storing numerical data
#   - Essential for other packages: e.g. scikit-learn
#   - loadtxt()
#   - getfromtxt()

# Importing flat files using NumPy
#   
import numpy as np
filename = 'MNIST_header.txt'
data = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=[0,2])
print(data)

# importing only str with numpy
# data = np.loadtxt(filename, delimiter=',', dtype=str)

# PANDAS
# Importing pandas
import pandas as pd
filename = 'winequality-red.csv'
data = pd.read_csv(filename)
print(data.head())

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Assign filename: file
file = 'titanic_corrupt.txt'

# Import file: data
data = pd.read_csv(file, sep='\t', comment='#', na_values=['Nothing'])

# Print the head of the DataFrame
print(data.head())

# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()