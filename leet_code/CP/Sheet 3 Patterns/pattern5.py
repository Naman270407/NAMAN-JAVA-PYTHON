# *_ _ _*
# *_ _ _*
# *_ _ _*
# *_ _ _*
# *_ _ _*

N=int(input("Enter number of rows:"))
for i in range(1, N+1):
    for j in range(1, N+1):
        if(j == 1) or (j == N):
           print("*", end="")
        else:
            print("_", end=" ")
    print()