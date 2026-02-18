# 1. Write a program that takes a positive integer N as input from the user and prints all natural numbers 
# numbers from 1 to N, with each number followed by a space. 
# Input:- N = 5 
# Output:- 1 2 3 4 5 

# n  = int(input())
# for i in range (1, n+1):
#     print(i, end=" ")





# 2. Write a program to print all Natural numbers from N to 1, where you have to take N as input 
# from the user. 
# Input:- N = 5 
# Output:- 5 4 3 2 1 

# n = int(input())
# for i in range (n,0,-1):
#     print(i, end =" ")




# 3. Write a program to print all even numbers from 1 to N, where you have to take N as input 
# from the user. 
# Input:- N = 10 
# Output:- 2 4 6 8 10 

# n = int(input())
# for i in range(2,n+1,2):
#     print(i, end=" ")



# 4. Write a program to print all odd numbers from 1 to N, where you have to take N as input 
# from user. 
# Input:- N = 10  Output:- 1 3 5 7 9 

# n = int(input())
# for i in range (1,n+1,2):
#     print(i, end = " ")



# 5. Write a program to find the sum of all Natural numbers from 1 to N, where you have to take N as 
# input from user 
# Input:- N = 10 
# Output:- 55 

# n = int(input())
# sum = 0
# for i in range (1,n+1):
#     sum = sum + i
# print(sum)



# 6. You are given an integer A, you need to find and return the sum of all the even numbers 
# between 1 and A. Even numbers are those numbers that are divisible by 2. 
# Input:- A = 5 
# Output:- 6 
# Explanation:- Even numbers between [1, 5] are (2, 4). 


# n = int(input())
# even_sum = 0
# for i in range (1,n+1):
#     if (i % 2 == 0):
#         even_sum += i
# print(even_sum)



# 7. Take an integer A as input. You have to print the sum of all odd numbers in the range [1, A]. 
# Input:- A= 4 
# Output:- 4 
# Explanation:- For A = 4, Odd numbers 1 and 3 lie in the range [1, 4]. Sum = 1 + 3 = 4. 

# n = int(input())
# odd_sum = 0
# for i in range (1,n+1):
#     if (i % 2 == 1):
#         odd_sum += i
# print(odd_sum)



# 8. Take an integer N as input and print the count of digits of that number. 
# Input:- N = 10101 
# Output:- 5 
# Explanation:- 10101 has 5 digits 

# n = int(input())
# count = 0
# while(n>0):
#     count += 1
#     n = n//10
# print(count)




# 9. Take an integer N as input. Your task is to calculate and print the sum of the digits of the 
# given number N. 
# Input:- N = 1589 
# Output:- 23 
# Explaination:- For the number 1589, the digits are 1,5,8,9. The Sum(1589) = 1+5+8+9 = 23. 

# n = int(input())
# sum = 0
# while (n>0):
#     sum = sum + n%10
#     n = n//10
# print(sum)



 
# 10. You are given an integer A as input, and you need to determine whether it is a palindrome 
# or not. Note: The given integer will not have any leading zeros. 
# Input:- A = 131 
# Output:- Yes 
# Explanation:- For A = 131, reverse(A) = reverse(131) = 131, which is the same as A. 

# n = int(input())
# rev = 0
# z = n
# while (n>0):
#     rev = rev*10 + n%10
#     n = n//10
# if (rev == z):
#     print("Yes")
# else:
#     print("No")


 
# 11. Take a number A as input, print its multiplication table having the first 10 multiples. 
# Input:-3 
# Output:- 
# 3 * 1 = 3 
# 3 * 2 = 6 
# 3 * 3 = 9 
# 3 * 4 = 12 
# 3 * 5 = 15 
# 3 * 6 = 18 
# 3 * 7 = 21 
# 3 * 8 = 24 
# 3 * 9 = 27 
# 3 * 10 = 30 


# n = int(input())
# for i in range(1,11):
#     print(n," * ",i," = ", n*i )



 
# 12. You are given two integers A and B. You have to find the value of A^B. 
# Input:- A = 2 , B = 3 
# Output:- 8 
# Explaination:- For A=2 and B=3, the value of 2^3 = 2 * 2 * 2 = 8. 


# a = int(input())
# b = int(input())
# pro = 1
# for i in range (1,b+1):
#     pro = pro * a
# print(pro)


# a = int(input())
# b = int(input())
# print(a**b)
