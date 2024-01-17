import random
title ='''
        Hello, Welcome to guessing game
'''
print(title)

coumputer = random.randint(1,100)

game_trigger=True

while game_trigger:

    user = int(input("Enter your gussing : "))
    if user>coumputer:
        print("guess Lower :")
    elif user<coumputer:
        print("guess higher :")
    else:
        print("you won")
        game_trigger=False
