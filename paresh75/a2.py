#GUESS GAME

import random
answer=random.randint(0,100)
guess_number=int(input("enter your guess number:"))
guess=1
game_over=False
while not game_over:
    if guess_number==answer:
        print(f"you got it in {guess} times")
        game_over=True
    else:
        if guess_number>answer:
            print(f"you guessed to large number")
            guess+=1
            guess_number=int(input("guess again'"))
        else:
            print(f"you guessed to small number")
            guess+=1
            guess_number=int(input("guess again'"))


