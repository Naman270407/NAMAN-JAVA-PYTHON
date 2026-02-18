def reverse(str1):
    if len(str1)==0:
        return str1
    else:
        return reverse(str1[1:])+str1[0]
str1=input()
print(reverse(str1))