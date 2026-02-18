# 8. Take an integer N as input and print the count of digits of that number.
# Input:- N = 10101
# Output:- 5
# Explanation:- 10101 has 5 digits



# num = int(input("enter a number : "))
# digit = len(str(num))
# print(digit)


num = int(input("Enter the number : "))
count = 0
while(num!=0):
    num = num//10
    count = count + 1
print(count)
