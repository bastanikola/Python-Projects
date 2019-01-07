------------------------------------
### PROJECT: FORTUNE TELLER GAME ###
------------------------------------
#importing library
import random

name = input("What is your name player?")

print('WELCOME TO THE FORTUNE TELLER ' + name.upper() + "!")
print('Select a color and a number and I will tell you what the future holds for you!')

answer = 'y'

while answer == 'y':
    
    color = input("Select a colour [yellow, green, blue, red] ")
        
    if color == "yellow" or color =="green":
        number = int(input("Select a number [1, 2, 5, 6]"))
        if number == 1:
              print("Worried about your future career? Don't worry. You'll 100% get what you want, be patient!")
        elif number == 2:
              print("You will become a millionaire at the age of 35!")
        elif number == 5:
              print("You will have a great family with 10 kids!")
        elif number == 6:
              print("You will become famous and everyone will love you!")
        else:
              print("Numbers 1, 2, 5, 6 are the only numbers allowed")
              continue

    
    elif color == "blue" or color == "red":
        number = int(input("Select a number [3, 4, 7, 8]"))
        if number == 3:
              print("You will live a happy life for 100 years at least!")
        elif number == 4:
              print("You will become a successful doctor one day!")
        elif number == 7:
              print("All your dreams will come true, just be patient!")
        elif number == 8:
              print("You're lucky, You will have it all one day!")
        else:
              print("Numbers 3, 4, 7, 8 are the only numbers allowed")
              continue
            
            
    else:
        print("Colors [yellow, green, blue, red] are only allowed")
        
        
    
    answer = input("Play again? insert 'y' for YES or 'n' for NO")
