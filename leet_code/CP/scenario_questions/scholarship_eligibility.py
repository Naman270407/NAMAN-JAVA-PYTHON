
n = int(input())  
count = 0
for i in range(n):
    marks, attendance = map(int, input("Enter marks and attendence of student : ").split())
    if (marks >= 75 and attendance >= 80):
        count = count + 1

print("Eligibile count : ", count)
