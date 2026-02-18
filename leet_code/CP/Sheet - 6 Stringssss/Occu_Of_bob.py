str = input().strip()
count = 0

for i in range(len(str) - 2):
    if str[i:i+3] == "bob":
        count += 1
print(count)