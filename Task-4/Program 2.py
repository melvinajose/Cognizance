# Program to accept a string from the user and display characters that are present at an even index number

string=str(input("Enter the string :"))
final=string[::2]  #accessing the elements at even index number through string slicing
print("The characters present at even index is '",final,"'")
