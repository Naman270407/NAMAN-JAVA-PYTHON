# 1. The Exam Result Analyzer 
# In a class of n students, each student’s marks are given in a list. A student 
# passes if their marks 
# are greater than or equal to 35. 
# Write a program to count the number of students who passed and failed. 
# Input Format 
# ● 
# First line: integer n (1 ≤ n ≤ 1000). 
# ● 
# Second line: n integers (marks of students). 
# Output Format 
# Print two integers: the count of passed students and the count of failed students. 
# Sample Input 
# 6 
# 12 67 45 22 90 33 
# Sample Output 
# 3 3 
# Explanation 
# Passed = 67, 45, 90 → 3 students. 
# Failed = 12, 22, 33 → 3 students.

# n = int(input())
# l = list(map(int, input().split()))
# p = 0
# f = 0
# for i in l:
#     if (i >= 35):
#         p = p +1
#     else:
#         f = f + 1
# print(p,f)



# 2. The Employee ID Filter 
# A company stores n employee IDs in a list. The HR wants to print only those IDs 
# that are even 
# numbers (since odd IDs are temporary employees). 
# Input Format 
# ● 
# First line: integer n (1 ≤ n ≤ 500). 
# ● 
# Second line: n integers (employee IDs). 
# Output Format 
# Print all even employee IDs separated by a space. If none, print -1. 
# Sample Input 
# 7 
# 101 202 303 404 111 222 333 
# Sample Output 
# 202 404 222 
# Explanation 
# Only even IDs are selected. 

# n = int(input())
# l = list(map(int, input().split()))
# count = 0
# for i in l:
#     if (i%2==0):
#         print(i,end=" ")
#         count = count +1
# if (count == 0):
#     print(-1)





# 3. The Product Sales Report 
# A store keeps a list of sales of n products. Each product has a sales count. The 
# manager wants 
# to print the highest-selling product count and the lowest-selling product count. 
# Input Format 
# ● 
# First line: integer n (1 ≤ n ≤ 1000). 
# ● 
# Second line: n integers (sales count of each product). 
# Output Format 
# Print two integers: max sales and min sales. 
# Sample Input 
# 5 
# 12 45 23 89 34 
# Sample Output 
# 89 12 
# Explanation 
# Maximum sales = 89, Minimum sales = 12. 


# n = int(input())
# l = list(map(int, input().split()))
# print(max(l),min(l))



# 4. The Scholarship Eligibility 
# In a university, n students applied for scholarships. The eligibility criteria are: 
# ● 
# The student’s marks must be greater than or equal to 75. 
# ● 
# The student’s attendance percentage must be greater than or equal to 80. 
# Write a program to count how many students are eligible for scholarships. 
# Input Format 
# ● 
# First line: integer n (1 ≤ n ≤ 500). 
# ● 
# Next n lines: each contains two integers → marks and attendance percentage. 
# Output Format 
# Print the number of eligible students. 
# Sample Input 
# 4 
# 85 90 
# 70 85 
# 75 80 
# 90 70 
# Sample Output 
# 2 
# Explanation 
# (85,90) eligible 
# (70,85) (marks < 75) 
# (75,80) eligible 
# (90,70) (attendance < 80)

# n = int(input())
# count = 0
# for i in range (n):
#     marks , percentage = map(int, input().split())
#     if (marks >= 75 and percentage >= 80):
#         count = count + 1
# print(count)



# 5. The Perfect Pair Finder 
# A company maintains a list of project deadlines (in days). Two projects are called a perfect pair 
# if the sum of their deadlines is exactly equal to a given target k. 
#  Find how many such pairs exist in the list. 
# Input Format 
# ● First line: integer n (1 ≤ n ≤ 1000). 
# ● Second line: n integers (project deadlines). 
# ● Third line: integer k. 
# Output Format 
# Print the number of perfect pairs. 
# Sample Input 
# 6 
# 1 5 7 -1 5 3 
# 6 
# Sample Output 
# 3 
# Explanation 
# Pairs are: (1,5), (1,5), (7,-1). → Total 3 pairs. 


# n = int(input())
# l = list(map(int, input().split()))
# target = int(input())
# count = 0
# for i in range (n):
#     for j in range (i+1,n):
#         if (l[i]+l[j]==target):
#             count = count + 1
# print(count)


# 6. The Attendance Tracker 
# A teacher records attendance for n students, where 1 means present and 0 means absent. 
# Write a program to count the number of consecutive absences (0’s) that lasted the longest. 
# Input Format 
# ● First line: integer n (1 ≤ n ≤ 1000). 
# ● Second line: n integers (0 or 1). 
# Output Format 
# Print the length of the longest streak of absentees. 
# Sample Input 
# 10   
# 1 0 0 1 0 0 0 1 1 0 
# Sample Output 
# 3

# n = int(input())
# l = list(map(int, input().split()))
# count = 0
# d = []
# e = 0
# for i in l:
#     if (i == 0):
#         count += 1
#         e = count
#     else:
#         count = 0
#         d.append(e)
# print(max(d))



# 7. The Stock Price Fluctuation 
# A company records daily stock prices of n days. The manager wants to know how many 
# days 
# the stock price was strictly higher than the previous day. 
# Input Format 
# ● 
# First line: integer n (1 ≤ n ≤ 1000). 
# ● 
# Second line: n integers (stock prices). 
# Output Format 
# Print the number of days where price increased compared to the previous day. 
# Sample Input 
# 7 
# 100 102 101 105 107 106 110 
# Sample Output 
# 4


# n = int(input())
# l = list(map(int, input().split()))
# count = 0
# for i in range(1,n):
#     if (l[i] > l[i-1]):
#         count += 1
# print(count)




 
# 8. The Reverse Order Processing 
# A factory records n product IDs. The supervisor wants to print them in reverse order, but 
# only 
# those IDs that are divisible by 5. If none, print -1. 
# Input Format 
# ● 
# First line: integer n (1 ≤ n ≤ 1000). 
# ● 
# Second line: n integers (product IDs). 
# Output Format 
# Print the IDs divisible by 5 in reverse order. 
# Sample Input 
# 6 
# 12 25 40 33 50 27 
# Sample Output 
# 50 40 25


# n = int(input())
# l = list(map(int, input().split()))
# u = []
# for i in l:
#     if (i % 5 == 0):
#         u.append(i)
# if (len(u)==0):
#     print(-1)
# u.reverse()
# print(*u)



# 9. The Temperature Monitor 
# A weather station records the temperature of n days. The station wants to count how 
# many days 
# the temperature was above the average temperature. 
# Input Format 
# ● 
# First line: integer n (1 ≤ n ≤ 1000). 
# ● 
# Second line: n integers (temperature of each day). 
# Output Format 
# Print the count of days with temperature above average. 
# Sample Input 
# 5 
# 30 40 35 50 45 
# Sample Output 
# 2 
# (Avg = 40, above average = 50, 45 → 2 days)

# n = int(input())
# l = list(map(int, input().split()))
# avg = sum(l)/len(l)
# count = 0
# for i in l:
#     if (i > avg):
#         count += 1
# print(count)



# 10. The Unique Gift Finder 
# A shop maintains a list of customer gift codes (n codes). The manager wants to find and 
# print 
# the codes that appear exactly once in the list. Print them in the same order as they 
# appeared. 
# If none, print -1. 
# Input Format 
# ● 
# First line: integer n (1 ≤ n ≤ 1000). 
# ● 
# Second line: n integers (gift codes). 
# Output Format 
# Print unique gift codes separated by space. 
# Sample Input 
# 8 
# 10 20 30 10 40 20 50 60 
# Sample Output 
# 30 40 50 60


# n = int(input())
# l = list(map(int, input().split()))
# count = 0
# u = []
# for i in l:
#     if (l.count(i)==1):
#         print(i,end=" ")
#         u.append(i)
# if(len(u)==0):
#     print(-1)
