A = input()
A = A + A
B = ""
result = ""
for i in range(len(A)):
    if A[i] >= 'A' and A[i] <= 'Z':
        continue
    else:
        B += A[i]
for i in range(len(B)):
    if B[i] == 'a' or B[i] == 'e' or B[i] == 'i' or B[i] == 'o' or B[i] == 'u':
        result += '#'
    else:
        result += B[i]
print(result)    # =>###z###z