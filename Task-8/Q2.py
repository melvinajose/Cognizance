# Checking if two user input arrays are equal

import numpy as np

#Taking the array values

first_array = []
n = int(input('How many elements do you want in first array : '))
for i in range(0, n):
    x = input('Enter a number into the array: ')
    first_array.append(x)

second_array = []
n = int(input('How many elements do you want in second array : '))
for i in range(0, n):
    x = input('Enter a number into the array: ')
    second_array.append(x)

print("---------------")
print("First Array : ", first_array)
print("Second Array : ", second_array)
print("---------------")

# Checking the equality of the arrays

print(np.array_equal(first_array, second_array, equal_nan=False))



