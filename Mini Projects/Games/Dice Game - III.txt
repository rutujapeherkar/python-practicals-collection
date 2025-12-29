 # Dice Game..

from random import randint

total_players = int(input("Enter Total number of Players : "))
first_six = False
curr_player = 1

while True:
    print("Player", curr_player, "press ENTER to roll the DICE", end="")
    input()
    rolled = randint(1,6)
    print("You rolled ---->", rolled)
    if rolled==6 and first_six==False:
        first_six = True
        print("Please repeat your turn")
        continue
    if rolled==6 and first_six==True:
        print("Player", curr_player, "wins.....")
        break
    if rolled!=6:
        first_six = False
        curr_player = curr_player + 1
        if curr_player>total_players:
            curr_player = 1
