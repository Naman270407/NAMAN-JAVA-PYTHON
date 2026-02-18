# print all factors/divisor of a given +ve number.

n = int(input("Enter the positive number : "))
c=1
while (c<=n):
    if (n%c==0):
        print(c)
    c+=1
else:
    print("This is not a positive number")
