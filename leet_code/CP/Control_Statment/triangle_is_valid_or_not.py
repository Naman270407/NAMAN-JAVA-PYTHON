# You are given 3 integer angles of a triangle. tell whether the triangle is valid or not.

q1 = int(input("Enter the first angle of triangle : "))
q2 = int(input("Enter the second angle of triangle : "))
q3 = int(input("Enter the third angle of triagle : "))
sum = q1+q2+q3
if(q1!=0 and q2!=0 and q3!=0):
    if(sum == 180) :
        print("It is a valid triangle")
else:
    print("It is not a valid triangle")
