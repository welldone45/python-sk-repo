title='''
        Rock, Paper, Scissor      
'''

flag=True

import random

game_choice=["rock","paper","scissor"]
computer_choice=random.choice(game_choice)

while flag:
    
user=input("enter your choice:")

print("user choice : ",user)
print("computer choice :",computer_choice)

if user== computer_choice :
    print("Tie")
elif user == 'rock' and computer_choice == 'paper' or user == 'scissor' and computer_choice== 'rock' or user == 'paper' and computer_choice == 'scissor':
    print("computer won")
elif user == 'paper' and computer_choice == 'rock' or user == 'rock' and computer_choice== 'paper' or user == 'scissor' and computer_choice == 'paper':
    print("user won")

choice=input("do you want to play again, if yes then press y and no then press n").lower()
if choice=='y':
    flag=True
else:
    flag=False