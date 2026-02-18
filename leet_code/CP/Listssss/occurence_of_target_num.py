#  give a list and a target find number of accurance of target no. in the list


a = [2,4,6,8,10,12,14,2,5,9,7,2,4,2]
tg = int(input("Taget your number : "))
count = 0
for i in a:
    if(tg == i):
        count = count +1
print("Occurence of ", tg, " = " , count)

