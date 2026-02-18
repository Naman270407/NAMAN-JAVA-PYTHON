def pal(str1):
    if len(str1)==0:
        return True
    elif str1[0]!=str1[-1]:
        return False
    else:
        return pal(str1[1:-1])
str1=input()
if pal(str1)==True:
    print("Palindrome")
else:
    print("Not Palindrome")