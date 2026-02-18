#  1.Sum of list
#  Given an array compute the sum of all elements.
#  Input : A=[1 2 3 4 5]           Output: 15

# l = list(map(int, input().split()))
# a = sum(l)
# print(a)

# or

# l = list(map(int, input().split()))
# sum = 0
# for i in l:
#     sum = sum + i
# print(sum)




#  2.Copy the Array
#  You are given a constant array A and an integer B.
#  You are required to return another array where Arr[i] = A[i] + B.
#  Input: A=[1 2 3 2 1]      B=3       Output:[4 5 6 5 4]

# l = list(map(int, input().split()))
# b = int(input())
# u = []
# for i in l:
#     u.append(i+b)
# print(u)





#  3.Max and Min of an Array
#  Take input an array A of size N and write a program to print maximum and minimum
#  elements of the input array .Here N represents the length of the array .
#  Input :  A=[1 2 3 4 5]        Output:  5 1

# l = list(map(int, input().split()))
# print(max(l),min(l))
# or

# l = list(map(int, input().split()))
# max = l[0]
# min = l[0]
# for i in l:
#     if (i >= max):
#         max = i
#     if (i <= min):
#         min = i
# print(max,min)



#  4.Search Element
#  You are given array A and an integer B. You have to tell whether B is present in array A
#  or not.   Input: A=[1 5 9 1]       B=5          Output:1

# l = list(map(int, input().split()))
# b = int(input())
# count = 0
# for i in l:
#     if (i == b):
#         count = count + 1
# print(count)




# 5.Negative Integers 
# Write a program to print all negative numbers from input array A of size N. 
# Input:-  A = [1 -5 2 -8 -4]       Output: -5 -8 -4 

# l = list(map(int, input().split()))
# for i in l:
#     if (i < 0):
#         print(i,end=" ")




#   6.Even Odd Elements 
# For array A, you have to find the value of absolute difference between the counts of 
# even and odd elements in the array. 
# Array A diya h, usme jitne even (जोड़ संख्या) elements h aur jitne odd (विषम संख्या)
#  elements h un dono ki ginti ka difference nikalna hai — 
# aur wo difference hamesha positive hona chahiye (absolute difference).
# Input: A = [1 2 3 4]       Output: 0   

# l = list(map(int, input().split()))
# e_count = 0
# o_count = 0
# for i in l:
#     if(i%2 == 0):
#         e_count += 1
#     else:
#         o_count += 1
# print(abs(e_count - o_count))




# 7.Separate Odd Even 
# You are given an integer array A. 
# You have to print the odd and even elements of array A in 2 separate lines. 
# Input: A = [1 2 3 4 5]       Output: 1 3 5      2 4 


# l = list(map(int, input().split())) 
# even = [] 
# odd = [] 
# for i in l: 
#    if (i%2==0): 
#       even.append(i) 
#    else: 
#       odd.append(i) 
# print(*odd)
# print(*even) 




# 8.Square of Array 
# You are provided with an integer array A. Return another array B of size same as that of 
# A such that B[i] = A[i]^2 
# Input: A=[2, 6, 8, 1]         Output: [4, 36, 64, 1] 

# l = list(map(int, input().split()))
# u = []
# for i in l:
#     u.append(i**2)
# print(u)




# 9.Cube of Array 
# You are provided with an integer array A. Return another array B of size same as that of 
# A such that B[i] = A[i]^3 
# Input: A=[2, 6, 8, 1]       Output: [8, 216, 512, 1] 

# l = list(map(int, input().split()))
# b = []
# for i in l:
#     b.append(i**3)
# print(b)



 
# 10.Reverse 
# Given an array A, Find the reverse of it. (Solve this question with for loop) 
# Input:  A = [3, 5, 1, 2, 1, 2] 
# Output:  [2, 1, 2, 1, 5, 3] 

# l = list(map(int, input().split()))
# u = []
# for i in range (len(l)-1,-1,-1):
#     u.append(l[i])
# print(u)


