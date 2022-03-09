# Program to perform addition on two numpy arrays

import numpy as np
  
# Taking the first array as input

size = int(input("Enter the number of rows in array 1 : ")) 
arr1 = []
print("Enter the column-wise values :")
for x in range(size):
    arr1.append([int(y) for y in input().split()])

# Taking the second array as input

size = int(input("Enter the number of rows in array 2 : ")) 
arr2 = []
print("Enter the column-wise values :")
for x in range(size):
    arr2.append([int(y) for y in input().split()])

# Printing the sum

print("The sum of both the arrays is : ")
add = np.add(arr1, arr2)
print(add)
