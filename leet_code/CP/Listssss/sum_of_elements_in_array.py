#  Given an array compute the sum of all elements.

print("Enter the elements of the list : ")
a = list(map(int,input().split()))
sum = 0
for i in a:
    sum = sum + i
print(sum)
