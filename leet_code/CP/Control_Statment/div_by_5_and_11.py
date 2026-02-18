# 5. Take an integer A as input. You have to tell whether A is divisible by both 5 and 11 or not

A = int(input("Enter the number : "))
if((A%5==0) and (A%11==0)):
    print(A, "is divided by 5 and 11")
else:
    print(A, "is not divided by 5 and 11")
