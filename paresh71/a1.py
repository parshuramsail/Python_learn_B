# SNAKE GAME
import random
lst=['s','w','g']
chance=10
no_of_chance=0
computer_point=0
human_point=0

print("\t \t \t \t SNAKE,WATER,GUN GAME \n \n")
print("s for snake \nw for water \ng for gun \n ")

# MAKNG THE GAEME IN WHILE
while no_of_chance < chance:
    _input=input("Snake,Water,Gun:")
    _random=random.choice(lst)

    if _input==_random:
        print(" tie both 0 point to each \n")

    # IF USER ENTERS S
    elif _input=='s' and _random=='g':
        computer_point=computer_point+1
        print(f" your guess {_input} and computer guess is {_random}\n")
        print("computer wins 1 point \n")
        print(f" computer point is {computer_point} and your point is {human_point}\n")

    elif _input=='s' and _random=='w':
        human_point=human_point+1
        print(f" your guess {_input} and computer guess is {_random}\n")
        print("human wins 1 point \n")
        print(f" computer point is {computer_point} and your point is {human_point}\n")

    # IF USER ENTERS W
    elif _input=='w' and _random=='s':
        computer_point=computer_point+1
        print(f" your guess {_input} and computer guess is {_random}\n")
        print("computer wins 1 point \n")
        print(f" computer point is {computer_point} and your point is {human_point}\n")

    elif _input=='w' and _random=='g':
        human_point=human_point+1
        print(f" your guess {_input} and computer guess is {_random}\n")
        print("human wins 1 point \n")
        print(f" computer point is {computer_point} and your point is {human_point}\n")

    # IF USER ENTERS G
    elif _input=='g' and _random=='s':
        computer_point=computer_point+1
        print(f" your guess {_input} and computer guess is {_random}\n")
        print("computer wins 1 point \n")
        print(f" computer point is {computer_point} and your point is {human_point}\n")

    elif _input=='g' and _random=='w':
        human_point=human_point+1
        print(f" your guess {_input} and computer guess is {_random}\n")
        print("human wins 1 point \n")
        print(f" computer point is {computer_point} and your point is {human_point}\n")

    else:
        print('you entered wrong input \n')
    no_of_chance=no_of_chance+1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("GAME OVER")

if computer_point==human_point:
    print("TIE")

elif computer_point > human_point:
    print(' COMPUTER WINS AND YOU LOOSE')

else:
    print("YOU WIN AND COMPUTER LOOSE")

print(f"your point is {human_point} and computers point is {computer_point}")




