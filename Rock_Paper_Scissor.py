import random

title='''
              --: Welcome to Rock, Paper, Scissor :--
'''
your_choice=["rock","paper","scissor"]
game_trigger=True
computer=random.choice(your_choice)

while game_trigger:
    
    user=input("Enter Your choice :")
    print("computer's choice:",computer)
    if user == "rock" and computer == "rock":
                print("It's a tie")
    elif user == "paper" and computer == "paper":
                print("It's a tie")
    elif user == "scissor" and computer == "scissor":
                print("Its tie")
    elif user == "rock" and computer == "scissor":
                print("computer wins")
    elif user == "rock" and computer == "paper":
                print("computer wins")        
    elif user == "paper" and computer == "rock":
                print("user wins")
    elif user == "paper" and computer == "scissor":
                print("computer wins")
    elif user == "scissor" and computer == "rock":
                print("user wins")
    elif user == "scissor" and computer == "paper":
                print("user wins")
    else: print("invalid choice")
    
    game_trigger=False