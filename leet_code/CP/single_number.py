def Single_number(arr):
    ans = 0
    n = len(arr)
    for i in range (n):
        ans = ans ^ arr[i]
    return ans
arr = [6,7,9,7,6]
print(Single_number(arr))

