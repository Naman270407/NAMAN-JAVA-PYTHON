# Write a program to input two numbers(A & B) from the user and print the maximum element among A & B.

A = int(input("Enter the first number : "))
B = int(input("Enter the second number : "))

if(A>B):
    print("A is greater than B.")
elif(A==B):
    print("A is equal to B.")
else:
    print("B is greater than A.")
