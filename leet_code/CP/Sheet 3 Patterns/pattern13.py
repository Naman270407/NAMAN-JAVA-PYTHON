# 1234
# 123
# 12
# 1

N=int(input("Number of rows:"))
for i in range(N, 0, -1):    
    for j in range(1, i + 1):   
        print(j, end=" ")
    print()