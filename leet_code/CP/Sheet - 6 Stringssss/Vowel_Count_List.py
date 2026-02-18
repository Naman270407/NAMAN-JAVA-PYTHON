n = int(input())
list = []
vowel = 0
consonants = 0
for i in range(n):
    element = input()
    list.append(element)

for i in range(n):
    list[i] = list[i].lower()


for i in range(n):
    vowel = 0
    consonants = 0
    for j in range(len(list[i])):
        if(list[i][j] == 'a' or list[i][j] == 'e' or list[i][j] == 'i' 
        or list[i][j] == 'o' or list[i][j] == 'u'): #this is because we have to check particular character of a list 
            vowel += 1
        else:
            consonants += 1
    print(vowel, consonants)
    


