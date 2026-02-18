# 1
# 1 *
# 1 * 3
# 1 * 3 *
# 1 * 3 * 5



  

N=int(input("Enter the Number of rows:"))
for i in range(1,N+1):
    sum=1
    for j in range(1, i+1):
        if(j%2==1):
            print(sum, end=" ")
            sum=sum+2
        else:
            print("*", end=" ")
    print()

