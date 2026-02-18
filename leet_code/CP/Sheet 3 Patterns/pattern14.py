# 1
# 23
# 456
# 78910

N=int(input("Number of rows:"))
num=int(input("Enter the Number:"))
for i in range(1, N + 1):        
    for j in range(1, i + 1):       
        print(num, end=" ")
        num =num + 1
    print() 