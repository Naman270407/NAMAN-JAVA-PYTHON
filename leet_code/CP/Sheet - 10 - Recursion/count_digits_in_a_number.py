def count(n):
    if n==0:
        return 0
    else:
        return 1+count(n//10)
n=int(input())
print(count(n))