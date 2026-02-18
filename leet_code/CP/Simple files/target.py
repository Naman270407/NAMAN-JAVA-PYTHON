#  Given a list of integers and a target no., find and print index of the target in the list.

# list = [1, 2, 3, 4, 5, 6, 7, 55, 9, 10]
# Tn = 7
# for i in range (len(list)) :
#     if ( list[i] == Tn):
#         print(i)



l1 = [1,2,3,4,4,5]
l2 = [5,6,7,8]
result = []
for i in range(len(l2)):
    result.append(l1[i] + l2[i])
print(result)
