def sum(n):
    su=0
    if n<=1:
        return n
    else:
        return n%10+sum(n//10)
n=int(input())
print(sum(n))