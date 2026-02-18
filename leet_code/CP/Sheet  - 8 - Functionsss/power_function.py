def power(a,b):
    s=1
    for i in range(1,b+1):
        s*=a
    return s
print(power(2,3))