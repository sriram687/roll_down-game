import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
             print("Must be between 2 - 4 players")
    else:
         print("The Entered Number is invalid")

print(players)