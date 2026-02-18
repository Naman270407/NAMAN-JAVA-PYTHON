# # # Read three angles of triangles and determine their types(Right triangle, Obtuse triangle, Acute triangle). 

# an acute triangle has all angles less than 90 degrees, 
# a right triangle has one angle exactly equal to 90 degrees, and 
# an obtuse triangle has one angle greater than 90 degrees

a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))
if a + b + c == 180 and a > 0 and b > 0 and c > 0:
    if a == 90 or b == 90 or c == 90:
        print("Right triangle")
    elif a > 90 or b > 90 or c > 90:
        print("Obtuse triangle")
    else:
        print("Acute triangle")
else:
    print("Invalid triangle")

