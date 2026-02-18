# Accept the percentage from the user and display the grade according to criteria.

Eng = int(input("Enter the grade of the english:"))
hindi = int(input("Enter the grade of the hindi:"))
Maths = int(input("Enter the grade of the maths:"))
total = Eng + hindi + Maths
per = (total / 300) * 100

if per >= 80.0:
    print("Student obtaained GRADE A")
elif per >= 70 and per < 80:
    print("Student obtaained GRADE B")
elif per >= 60 and per < 70:
    print("Student obtaained GRADE C")
elif per >= 40 and per < 60:
    print("Student obtaained GRADE D")
else:
    print("Student obtaained GRADE E")
