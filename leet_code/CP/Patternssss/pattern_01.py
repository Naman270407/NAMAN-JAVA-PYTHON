N = int(input("Enter the lines to print for stars : "))
for i in range(1, N+1):
    for j in range(i):
        print ("*", end=" ")
    print()


