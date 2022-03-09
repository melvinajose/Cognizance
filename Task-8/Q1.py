# Program to build a new vector with 5 consecutive zeros interleaved between each value

import numpy as np

x=int(input("First Number :"))
y=int(input("Last Number :"))

arr=np.arange(x,y+1)    #Creating the array
final=np.zeros(len(arr)+((len(arr)-1)*5))
final[::6]=arr      #Creating the final vector
print(final)
