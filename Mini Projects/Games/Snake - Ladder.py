import random

print("Enter the number of players you want :", end=" ")
pl_num = int(input())

ls = []

i = 0
while i<pl_num:
    ls.append(0)
    i = i + 1

pl_sum = 0

while True:
    i = 0
    curr_player = 1

    while i<pl_num:
        print("Player ",curr_player, "turn : ")
        print("Player ",curr_player," press enter to roll the dice :", end = " ")
        input()
        roll = random.randint(1,6)
        pl_sum += roll
        print("You rolled :" ,roll)
        ls[i] = ls[i] + roll
        pl_sum = 0

        #All ladder's condition...
        if ls[i] == 1:
            pl_sum = ls[i] + 37
            print("Wow... You got ladder at 1 and moved at block 38")
            ls[i] = pl_sum

        elif pl_sum == 4:
            pl_sum = ls[i] + 37
            print("Wow... You got ladder at 4 and moved at block ")
            ls[i] = pl_sum

        elif pl_sum== 8:
            ls[curr_player-1] = 30
            print("Wow... You got ladder and jumped at block 30")

        elif pl_sum == 21:
            ls[curr_player-1] = 42
            print("Wow...You got ladder and jumped at block 42")

        elif pl_sum == 28:
            ls[curr_player-1]= 76
            print("Wow...You got ladder and jumped at block 72")

        elif pl_sum == 50:
            ls[curr_player-1] = 67
            print("Wow...You got ladder and jumped at block 67")

        elif pl_sum == 71:
            ls[curr_player-1] = 92
            print("Wow...You got ladder and jumped at block 92")

        elif pl_sum == 88:
            ls[curr_player-1] = 99
            print("Wow...You got ladder and jumped at block 99")

        # All snake's conditions...
        elif pl_sum == 32:
            ls[curr_player-1]= 10
            print("Oops...You ate by snake and fall down at block 10")

        elif pl_sum == 36:
            ls[curr_player-1] = 6
            print("Oops...You ate by snake and fall down at block 6")

        elif pl_sum == 48:
            ls[curr_player-1] = 26
            print("Oops...You ate by snake and fall down at block 26")

        elif pl_sum == 62:
            ls[curr_player-1] = 18
            print("Oops...You ate by snake and fall down at block 18")

        elif pl_sum == 88:
            ls[curr_player-1] = 24
            print("Oops...You ate by snake and fall down at block 24")

        elif pl_sum ==95:
            ls[curr_player-1] = 56
            print("Oops...You ate by snake and fall down at block 56")

        elif pl_sum == 97:
            ls[curr_player-1] = 78
            print("Oops...You ate by snake and fall down at block 78")

        else:
            pl_sum += roll
            ls[curr_player - 1] = pl_sum

        if pl_sum == 100:
            print("Player ", curr_player, "is winner")
            break
        elif pl_sum > 100:
            pl_sum = pl_sum - roll

        curr_player += 1
        if curr_player>pl_num:
            curr_player = 1
            print("Current board is :", ls)
            print("\n")














