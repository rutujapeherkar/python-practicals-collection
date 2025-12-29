import random
import time

values = list(range(1,11))
operators = ["+", "-", "*", "/", "//", "<", ">", "==", "!="]
ls = []

print("Enter the number of players you want : ", end = "")
no_of_players = int(input())

i = 1
while i<=no_of_players:
    j = 1
    while j<=5:

        print("PLayer ", i, ",turn")
        op1 = random.choice(values)
        op2 = random.choice(values)
        opr = random.choice(operators)
        print(op1 , opr , op2)

        print("Enter your answer : ",end = "")
        time1 =  time.perf_counter()
        if opr == "/" :
            ans = float(input())
        else:
            ans = int(input())

        ans2 = eval(str(op1) + opr + str(op2))

        if ans2 == True:
            ans2 = 1
        elif ans2 == False:
            ans2 = 0

        if ans2 == ans:
            print("Your answer is correct ")
        else:
            print("Your answer is wrong. ")
            j = j - 1
        j = j + 1
    time2 = time.perf_counter()
    time3 = time2 - time1
    ls.append(time3)
    i = i + 1

min_time = min(ls)
win_ind = ls.index(min_time)

print("Player ", win_ind + 1,"wins . Time taken by Player - 1 is : ",min_time)





