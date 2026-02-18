# Given an array elements, every element repeat twice except 1. Find the unique element.

# [9,9,8,8,7,7,6,6,5,5,4,3,3,2,2,1,1]
# unique element = 4

arr = [9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 3, 3, 2, 2, 1, 1]

unique = 0
for i in arr:
    unique = unique ^ i

print(f'unique element is: {unique}')
