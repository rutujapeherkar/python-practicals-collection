str1 = input("Enter the first name :- ")
str2 = input("Enter the second name :- ")
str1 = str1.lower()
str2 = str2.lower()

str3 = str1 + str2

t = str3.count('t')
r = str3.count('r')
u = str3.count('u')
e = str3.count('e')

l = str3.count('l')
o = str3.count('o')
v = str3.count('v')
e = str3.count('e')

a = t+r+u+e
b = l+o+v+e

scores = str(a) + str(b)

score = int(scores)

if(score < 0 and score > 90):
     if not(score > 40 and score  <= 60):
        print("Everything is okay, can go for dinner")
elif(score > 40 and score <=60):
     print("Fine")
else:
     print("True love is",score ,"%")

