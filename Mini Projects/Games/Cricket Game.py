import random

tossch = ["H", "T"]
print("Let's play cricket game : ")
print("Player 1, enter your choice (H/T) :")
ch = input()
ch2 = random.choice(tossch)

if ch== ch2:
    print("Player 1 you win the toss")

else:
    print("Player 2 wins the toss")

if ch == ch2:
    print("\nWhat would you like to choose ?")
    print("1. Batting")
    print("2. Bowling")
    print("Player 1, provide your choice : ")
    op = int(input())


if op==1 and ch == ch2:
    print("Player 1, choosed batting")
elif op==2 and ch == ch2:
    print("Player 1, choosed bowling")
elif op==1 and ch == ch2:
    print("Player 1, choosed batting")
elif op==2 and ch == ch2:
    print("Player 1, choosed bowling")
p1sum = 0
compsum = 0

while True:
    print("Player 1, turn : ", end = " ")
    p1 = int(input())
    p1sum = p1sum + p1

    print("Computer's turn : ", end = " ")
    c1 = random.randint(1,6)
    print(c1)
    compsum = compsum + c1

    if p1 == c1:
        print("Player is winner")
        break

