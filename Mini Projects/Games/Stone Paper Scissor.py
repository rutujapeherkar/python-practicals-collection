
# Stone Paper Game - I.. With BOT..

from random import randint
import time

bot_wcount = 0
player_wcount = 0
draws_count = 0

round = 1
while round<=5:
    print("\n------ Round", round, "--------")
    print("1 - Stone")
    print("2 - Paper")
    print("3 - Scissor")

    bot = randint(1,3)
    player = int(input("Select your option : "))

    print("Bot selects :", bot)
    print("Player selects :", player)

    if player==1 and bot==2:
        print("Bot wins..")
        bot_wcount = bot_wcount + 1
    elif player==2 and bot==1:
        print("Player Wins..")
        player_wcount = player_wcount + 1
    elif player==2 and bot==3:
        print("Bot wins..")
        bot_wcount = bot_wcount + 1
    elif player==3 and bot==2:
        print("Player Wins..")
        player_wcount = player_wcount + 1
    elif player==3 and bot==1:
        print("Bot Wins...")
        bot_wcount = bot_wcount + 1
    elif player==1 and bot==3:
        print("Player Wins..")
        player_wcount = player_wcount + 1
    elif player==bot:
        print("Round Draw..")
        draws_count = draws_count + 1
    round = round + 1

time.sleep(3)
print("\nBot wins", bot_wcount, "times")
print("Player wins", player_wcount, "times")
print("Draw", draws_count, "times")
