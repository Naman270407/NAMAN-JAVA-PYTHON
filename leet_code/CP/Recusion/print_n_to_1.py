def num(n):
    if n == 0:
        return 0
    print(n)
    num(n-1)
n = int(input("Enter n : "))
print("Number from ",n,"to 1 : ")
num(n)
