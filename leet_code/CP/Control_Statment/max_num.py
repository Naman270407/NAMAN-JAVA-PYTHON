# Write a program to input three numbers and print the maximum among them.

n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the second number : "))
n3 = int(input("Enter the third number : "))
if(n1>n2 and n1>n3) :
    print(n1,"is maximum")
elif(n2>n3):
    print(n2,"is maximum")
else:
    print(n3,"is maximum")


