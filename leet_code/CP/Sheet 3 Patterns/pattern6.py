# *_ _ _ _ _*
# *_ _ _ _*
# *_ _ _*
# *_ _*
# *_*

N = int(input("Enter number of rows: "))

for i in range(1, N):   
    print("*", end=" ")           
    for j in range(N - i):         
        print("-", end=" ")
    print("*", end=" ")           
    print()   
