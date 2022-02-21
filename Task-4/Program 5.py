# Program to print a pyramid pattern

n=5
x=(2*n)-2
for i in range(n):
    for j in range(x):
        print(end=" ")
    x-=1
    for j in range(i+1):       #printing the triangle
        print("*", end=" ")
    print()
