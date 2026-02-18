A = input()
B = int(input())

for i in range(len(A)):
    if ord(A[i]) == B:
        print(i)
        break
else:
    print(-1)


