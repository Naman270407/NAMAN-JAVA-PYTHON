#  given an array of n integers
#  where all numbers occurs an even number of times except 1 which occurs odd number of time.
#  Find that number ?
# First line of the input contains integer n denoting the six=ze of array
# next line of input contains n seperated integers denoating the elements of array


n = int(input())
arr = list(map(int, input("Enter elements: ").split()))

result = 0
for num in arr:
    result ^= num
print("Number occurs odd number of times:", result)
