def num(n):
    if n == 0:
        return 0
    num(n - 1)
    print(n)


n = int(input("Enter n: "))
print("Numbers from 1 to", n, ": ")
num(n)
