
p1_sum, p2_sum = 0,0    #tuple unpacking
import random

round = 1
while round <=5:
    print("\n---------Round ", round, "--------")
    print("Player - 1, press ENTER to roll the dice", end = "")
    input()
    rolled = random.randint(1,6)
    print("You rolled :", rolled)
    p1_sum += rolled

    if rolled == 6:
        print("Repeat your turn :", end = "")
        continue

    rolled = 6
    while rolled == 6:
        print("\nPlayer - 2, press ENTER to roll the dice ", end ="")
        input()
        rolled = random.randint(1,6)
        print("You rolled :",rolled)
        p2_sum += rolled

    round = round + 1

print("\nScore of Player - 1 is :",p1_sum)
print("Score of Player - 2 is :",p2_sum)

