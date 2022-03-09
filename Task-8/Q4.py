# Program to convert the first character of each element in a series to uppercase

import pandas as pd

string = str(input("Enter the string :"))  
val = list(map(str,string.split(' ')))
ser = pd.Series(val)        # Converting the string into series
x = ser.str.capitalize()    # Capitalizing the first elements

# Printing the final result as a string

print("The final result is :")
for item in x:
    print(item, end=" ")
