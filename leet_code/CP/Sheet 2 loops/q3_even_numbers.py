# 3. Write a program to print all even numbers from 1 to N, 
# where you have to take N as input
# from the user.
# Input:- N = 10
# Output:- 2 4 6 8 10


# num = int(input("enter a number : "))
# for i in range(1,num+1):
#     if(i%2==0):
#         print(i)
    

n = int(input("Enter the number : "))
for i in range (2, n+1,+2):
    print(i)
