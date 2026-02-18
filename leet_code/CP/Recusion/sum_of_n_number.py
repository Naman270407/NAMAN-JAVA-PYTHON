def sum(n):

    if n == 1:
        return 1
    else:
        return n + sum(n - 1)
n = int(input("Enter a number: "))
result = sum(n)
print(result)


#  print number from 1 to n using recursion
#  print number from n to 1 using recursion
#  using a recursion function find the nth fibonacci series 
# python program