# 1. 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 

# n = int(input())
# for i in range (n-1):
#     for j in range(n):
#         print("*",end=" ")
#     print()


# 2. 
# *  
# * * 
# * * *  
# * * * *  
# * * * * *

# n = int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()



# 3. 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

# n = int(input())
# for i in range (n,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()




# 4. 
# 1  
# 1 *  
# 1 * 3  
# 1 * 3 *  
# 1 * 3 * 5

# n = int(input())
# for i in range(1,n+1):
#     for j in range (1,i+1):
#         if (j % 2 == 1):
#             print(j,end = " ")
#         else:
#             print("*",end=" ")
#     print()


# 5. 
# *_ _ _* 
# *_ _ _* 
# *_ _ _* 
# *_ _ _* 
# *_ _ _*


# n = int(input())
# for i in range (1,n+1):
#     for j in range (1,n+1):
#         if (j == 1 or j == n):
#             print("*",end=" ")
#         else:
#             print("_",end=" ")
#     print()



# 6. 
# * _ _ _ _ *
# * _ _ _ *
# * _ _ *
# * _ *
# * *

# n = int(input())
# for i in range (n,0,-1):
#     for j in range(1):
#         print("*",end=" ")
#     for j in range (1,i):
#         print("_",end=" ")
#     for j in range (1):
#         print("*",end=" ")
#     print()


# 7. 
#  _ _ _ _*        
#  _ _ _ * *           
#  _ _ * * *           
#  _  * *  * * 
#   *  * *  * * 

# n = int(input())
# for i in range (n,0,-1):
#     for j in range (1,i):
#         print("_",end=" ")
#     for j in range (i,n+1):
#         print("*",end=" ")
#     print()



# 8. 
# * * * * *          
# _ * * * *        
# _ _ * * *         
# _ _ _* *        
# _ _ _ _*


# n = int(input())
# for i in range (n,0,-1):
#     for j in range (i,n):
#         print("_",end=" ")
#     for j in range (i):
#         print("*",end=" ")
#     print()


# 9.
# **********
# ****  ****
# ***    ***
# **      **
# *        *


# n = int(input())
# for i in range (n,0,-1):
#     for j in range (i):
#         print("*",end="")
#     for j in range (i,n):
#         print(" ",end=" ")
#     for j in range (i):
#         print("*",end="")
#     print()



# 10. 
# *        * 
# **      ** 
# ***    *** 
# ****  **** 
# ********** 

# n = int(input())
# for i in range(1,n+1):
#     for j in range (i):
#         print("*",end="")
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range (i):
#         print("*",end="")
#     print()


# 11.
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        * 
# **      ** 
# ***    *** 
# ****  **** 
# **********

# n = int(input())
# for i in range (n,0,-1):
#     for j in range (i):
#         print("*",end="")
#     for j in range (i,n):
#         print(" ",end=" ")
#     for j in range (i):
#         print("*",end="")
#     print()
# for i in range(1,n+1):
#     for j in range (i):
#         print("*",end="")
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range (i):
#         print("*",end="")
#     print()


# 12. 
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 

# n = int(input())
# for i in range (1,n+1):
#     for j in range (1,i+1):
#         print(j,end=" ")
#     print()


# 13. 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 

# n = int(input())
# for i in range (n,0,-1):
#     for j in range (1,i+1):
#         print(j,end=" ")
#     print()



# 14. 
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10

# n = int(input())
# k = 1
# for i in range (1,n+1):
#     for j in range (1,i+1):
#         print(k,end=" ")
#         k += 1 
#     print()


# 15. 
# * 
# ** 
# *** 
# **** 
# ***** 
# **** 
# *** 
# ** 
# *

# n = int(input())
# for i in range (1,n+1):
#     for j in range (i):
#         print("*",end="")
#     print()
# for i in range (n-1,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()


# * _ _ _ _ _ * 
# * _ _ _ _ *
# * _ _ _ *
# * _ _ *
# * _ *

# n = int(input())
# for i in range (1,n+1):
#     for j in range(1):
#         print("*",end=" ")
#     for j in range (n,i-1,-1):
#         print("_",end=" ")
#     for j in range (1):
#         print("*",end=" ")
#     print()
