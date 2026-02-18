# 4.Trim (*)
#  You are given a character string A. You to trim both leading and trailing asterisk characters('*') in
#  the string and print the resultant string.
#  Input:
#  A="**h*e*l*lo*"
#  Output:
#  h*e*l*lo

A = input()
A = A.strip('*')
print(A)
