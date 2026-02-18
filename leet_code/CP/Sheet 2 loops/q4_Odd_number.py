# 4. Write a program to print all odd numbers from 1 to N, where you have to take N as input
# from user.
# Input:- N = 10
# Output:- 1 3 5 7 9


# num = int(input("enter a number : "))
# for i in range(1,num+1):
#     if(i%2!=0):
#         print(i)

n = int(input("Enter the number : "))
for i in range (1,n+1,+2):
    print(i)
