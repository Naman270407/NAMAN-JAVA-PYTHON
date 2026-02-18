# Write a program to input three numbers and print the minimum among them.

n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the second number : "))
n3 = int(input("Enter the third number : "))
if(n1<n2 and n1<n3) :
    print(n1,"is minimum")
elif(n2<n3):
    print(n2,"is minimum")
else:
    print(n3,"is minimum")

