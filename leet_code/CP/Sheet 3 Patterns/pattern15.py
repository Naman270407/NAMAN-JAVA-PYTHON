# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

N=int(input("Enter the number of rows:"))
for i in range(1, N + 1):
    print("*" * i)
for i in range(N - 1, 0, -1):
    print("*" * i)
print()