def power(a,n):
    if n<=1:
        return a
    else:
        return a*power(a,n-1)
n=int(input())
a=int(input())
print(power(a,n))