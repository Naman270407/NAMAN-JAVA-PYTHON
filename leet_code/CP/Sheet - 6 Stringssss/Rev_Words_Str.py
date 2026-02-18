str = input().split()
reverse = []

for i in range(len(str)):
    reverse.append(str[i][::-1])
for element in reverse:
    print(element,end=" ")