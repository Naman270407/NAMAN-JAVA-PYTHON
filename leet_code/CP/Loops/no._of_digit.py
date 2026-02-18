# # count the digit of a number
# # Read N, print no of digits in N.



num = int(input("Enter a number: "))
count = 0

# Agar number negative ho to positive banalo
if num < 0:
    num = -num

# Special case: agar number 0 hai to ek digit hai
if num == 0:
    count = 1
else:
    while num > 0:
        num = num // 10   # last digit hatao
        count += 1        # ek digit count karo

print("Total digits:", count)
