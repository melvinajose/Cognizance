# Program to check if the given number is a palindrome number

print("Program to check if the given number is a palindrome number")
num=int(input("Enter the number :"))
temp=num
rev=0
while temp>0:
    l=temp%10
    temp=temp//10
    rev=rev*10+l
if rev==num:
    print("True")
else:
    print("False")
