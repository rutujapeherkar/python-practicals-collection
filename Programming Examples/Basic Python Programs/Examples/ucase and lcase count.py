string = input("Enter any string : ")

def Count(string):

    ucount = 0
    lcount = 0

    for i in string :

        if i >= 'A' and i <= 'Z':
            ucount = ucount + 1

        elif i>= 'a' and i<='z':
            lcount = lcount + 1

    print("\nCount of uppercase letters in the string is : ",ucount)
    print("Count of lowercase letters in the string is : ",lcount)

Count(string)