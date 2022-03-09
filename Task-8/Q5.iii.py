# Program to print identity matrix

import numpy as np

d=int(input("Enter the dimension: "))   # Taking the dimension as input
matrix = np.identity(d)    # Initializing the required matrix
print("The identity matrix of dimension ", d,"is :")
print(matrix)  #Printing the matrix
