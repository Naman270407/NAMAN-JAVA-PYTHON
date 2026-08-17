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


n = int(input())
l = list(map(int, input().split()))
target = int(input())
count = 0
for i in range (n):
    for j in range (i+1,n):
        if (l[i]+l[j]==target):
            count = count + 1
print(count)
