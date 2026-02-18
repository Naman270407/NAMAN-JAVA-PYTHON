# 5. Write a program to find the sum of all Natural numbers from 1 to N, 
# where you have to take N as
# input from user
# Input:- N = 10
# Output:- 55


num = int(input("enter a number : "))
sum = 0
for i in range(1,num+1):
   sum = sum+i
print(sum)

