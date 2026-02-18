# 11. Take a number A as input, print its multiplication table having the first 10 multiples.
# Input:-3
# Output:-
# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9
# 3 * 4 = 12
# 3 * 5 = 15
# 3 * 6 = 18
# 3 * 7 = 21
# 3 * 8 = 24
# 3 * 9 = 27
# 3 * 10 = 30




num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "*", i, "=", num * i)
