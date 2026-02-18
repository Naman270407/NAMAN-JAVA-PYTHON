# **********
# ****  ****
# ***    ***
# **      **
# *        *


N=int(input("Enter the number of rows:"))
for i in range(1,N+1):
    for j in range(N-i+1):
        print("*",end="")
    for j in range(2*i-2):
        print(" ",end="")
    for j in range(N-i+1):
        print("*",end="")
    print()