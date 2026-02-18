# *        *
# **      **
# ***    ***
# ****  ****
# **********

N=int(input("Enter the number of rows:"))
for i in range(1,N+1):
    for j in range(i):
        print("*",end="")
    for j in range(2*N-2*i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()