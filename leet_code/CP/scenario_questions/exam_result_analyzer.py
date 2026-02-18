n = int(input())
marks = list(map(int, input().split()))
p = 0
f = 0
for m in marks:
    if m >= 35:
        p = p + 1
    else:
        f = f + 1
print(p, f)
