import random

title= '''
        Hi, Let's Play guessing game with computer...
'''
print(title)

max_attemps=6
attemps=0

computer=random.randint(1,100)

while attemps<max_attemps:

    user=int(input("Your Guessing Number : "))
    attemps +=1
    print("Your attemps :",attemps)
    
   
    if user == computer:
            print("won")
            
    elif user<computer:
            print("think, higher number,try again")
    else:
            print("think, Lower Number,try again")
if attemps == max_attemps and user != computer:
                print("sorry, you tried max numbers...")