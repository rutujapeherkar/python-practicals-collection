print("Logic 1 : Counting the UPPERCASE & LOWERCASE count")
string = input("Enter any string : ")

def Count(string):
    ucount = 0
    lcount = 0

    for i in string :
        if i >= 'A' and i <= 'Z':
            ucount = ucount + 1

        elif i>= 'a' and i<='z':
            lcount = lcount + 1

    print("Count of uppercase letters in the string is : ",ucount)
    print("Count of lowercase letters in the string is : ",lcount)

Count(string)

print("\nLogic 2 : Counting the UPPERCASE & LOWERCASE count using Builtin Function ")

string = input("Enter any string : ")

ucount = 0
lcount = 0

for i in string :
        if(i.islower()):
             lcount = lcount + 1

        elif (i.isupper()):
             ucount = ucount + 1

print("Count of uppercase letters in the string is : ",ucount)
print("Count of lowercase letters in the string is : ",lcount)