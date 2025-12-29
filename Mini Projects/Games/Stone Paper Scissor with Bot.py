
# Stone Paper Game.. Simple 2 player Game..

print("1 - Stone")
print("2 - Paper")
print("3 - Scissor")

print("Player 1, select your option")
p1 = int(input())
print("Player 2, select your option")
p2 = int(input())

if p1==1 and p2==2:
    print("Player 2 Wins..")
elif p1==2 and p2==1:
    print("Player 1 Wins..")
elif p1==2 and p2==3:
    print("Player 2 Wins..")
elif p1==3 and p2==2:
    print("Player 1 Wins..")
elif p1==3 and p2==1:
    print("Player 2 Wins..")
elif p1==1 and p2==3:
    print("Player 1 Wins..")
elif p1==p2:
    print("Round Draw..")

