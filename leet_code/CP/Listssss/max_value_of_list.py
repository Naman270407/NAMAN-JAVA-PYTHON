# given an list find the max value of list

print("Enter the elements of the list : ")
a = list(map(int, input().split()))

max = a[0]   # list ke pehle element se start
for i in a:
    if (i > max):
        max = i

print("Max value = ", max)
