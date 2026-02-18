n = int(input())
list = []
reverse = []
isPalindrome = 1

for i in range(n):
    element = input()
    list.append(element)

for i in range(n):
    reverse.append(list[i][::-1])  #importatnt line

for i in range(n):
    if list[i] == reverse[i]:
        print(isPalindrome)
    else:
        print(0)

        # given an int array nums find the sum of all subarrays sums 
        # max subarray sum

# Kadane's Algorithm
