import random

a = random.randint(65,90)
fchar = chr(a - 1)
schar =  chr(a +1)
a = chr(a)

while True:

    print("PLAYER - 1, Guess the character ---> ", end ="")
    p1 = input()

    if p1 == a or p1 == fchar or p1 == schar :
        print("PLAYER - 1 is winner...")
        print("Character was :",a)
        print("You guessed :",p1)
        break

    print("PLAYER - 2, Guess the character ---> ", end ="")
    p2 = input()

    if p2 == a or p2 == fchar or p2 == schar:
        print("PLAYER - 2 is winner...")
        print("Character was :", a)
        print("You guessed :", p1)


    print("PLAYER - 3, Guess the character ---> ", end ="")
    p3 = input()
    if p3 == a or p3 == fchar or p3 == schar:
        print("PLAYER - 3 is winner...")
        print("Character was :", a)
        print("You guessed :", p1)




