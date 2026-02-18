def printing(n):
    if n>0:
        printing(n-1)
        print(n)
n=int(input())
print(printing(n))
