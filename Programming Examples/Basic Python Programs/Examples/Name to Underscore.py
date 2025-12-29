
ls = []
print("Enter the number of names you want to add in the list : ", end = '')
n = int(input())

i = 0
while i<n:
    print("Enter name ", i +1, " : ", end = '')
    ls.append(input())
    i = i + 1

for word in ls:
    underscore = '_'
    for ch in word :
        underscore = underscore + ' '
        ls[i] = underscore

print(ls)
