
from random import randint

target_value = int(input("Enter the target value to win : "))
p1_sum = 0
p2_sum = 0
flag = False

while True:
    print("\nPlayer - 1, press ENTER to roll the DICE ", end = "")
    input()
    rolled = randint(1,6)
    print("You rolled --->",rolled)
    p1_sum = p1_sum + rolled

    if p1_sum<= target_value:
        print("Sum is =", p1_sum)

    else:
        p1_sum = p1_sum - rolled
        remain = target_value - p1_sum
        print("You require =",remain)

    if p1_sum == target_value:
        print("Player - 1 is winner......")


    print("\nPlayer - 2, press ENTER to roll the DICE ", end = "")
    input()
    rolled = randint(1, 6)
    print("You rolled --->", rolled)
    p2_sum = p2_sum + rolled

    if p2_sum <= target_value:
        print("Sum is =", p2_sum)

    else:
        p2_sum = p2_sum - rolled
        remain = target_value - p2_sum
        print("You require =", remain)

    if p2_sum == target_value:
        print("Player - 2 is winner......")
        flag = True

    if flag == True:
        break




