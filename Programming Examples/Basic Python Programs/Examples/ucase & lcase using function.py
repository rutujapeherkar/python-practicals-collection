
string = input("\nEnter any string : ")

ucount = 0
lcount = 0

for i in string :
        if(i.islower()):
             lcount = lcount + 1

        elif (i.isupper()):
             ucount = ucount + 1

print("\nCount of uppercase letters in the string is : ",ucount)
print("Count of lowercase letters in the string is : ",lcount)