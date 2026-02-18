# print nth number of fibnocii series 

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1)+fib(n-2)

n = int(input("Enter n : "))
print("Fibnociii series number : ",fib(n))

