# Program to make a 2-dimensional list that contains student details

a=[["RollNo", "Name", "Marks"],[1, "Abc", 90], [2, "Def", 95], [3, "Ghi", 85]]
rec1=[4, "Jkl", 98]
rec2=[5, "Mno", 100]

# Printing the existing matrix
print("Existing data")
for i in range(len(a)):
    for j in range(3):
        print(a[i][j], end = " ")
    print()
print("**********************************")

# Inserting new user input records to the list
n=int(input("How many records do you wish to enter?"))
for i in range(n):
    x=[]
    x.append(int(input("Enter the Roll Number : ")))
    x.append(str(input("Enter the Name : ")))
    x.append(int(input("Enter the Marks : ")))
    a.append(x)
    print("**********************************")

# Printing the matrix
print("Updated Data")
for i in range(len(a)):
    for j in range(3):
        print(a[i][j], end = " ")
    print()
print("**********************************")


# Printing the second row
second=a[2][:]
to_list=[str(elements) for elements in second]
final=" ".join(to_list)
print("The second row from the list is :")
print(final)
