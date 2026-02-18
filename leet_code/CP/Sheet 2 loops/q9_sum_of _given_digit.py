# 9. Take an integer N as input. Your task is to calculate and
#  print the sum of the digits of thegiven number N.
#  Input:- N = 1589
# Output:- 23
# Explaination:- For the number 1589, the digits are 1,5,8,9. 
# The Sum(1589) = 1+5+8+9 = 23.


num = int(input("enter a number : "))
sum = 0
while (num>0):
    digit = num % 10
    sum = sum+digit
    num = num // 10 
print(sum)
