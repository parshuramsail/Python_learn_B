import random
num=random.randint(1,100)

print("welcome to guess game")
print("i am thinking number between 0 and 100")
print("if ur guess is farther than my number i will tell u your cold")
print("if ur guess is within the my number i will tell you your warm")
print("if ur guess is farther than resent guess i will tell u your colder")
print("if ur guess number is within the recent guess i will tell u your warmer")

guesses=[0]

while True:
    guess=int(input("enter a number between 1 and 100"))
    if guess<1 or guess>100:
        print('out of bounds')
        continue
    break

while True:
    guess=int(input("enter a number between 1 and 100"))
    if guess<1 or guess>100:
        print('out of bounds')
        continue

    if guess==num:
        print(f"you guessesd it in {len(guesses)}")
        break


    guesses.append(guess)

    if guesses[-2]:
        if abs(guess-num)<abs(guesses[-2]):
            print("warmer")
        else:
            print("colder")
    else:
        if (guess-num)<10:
            print("warm")
        else:
            print('cold')






