# importing random and used it to choose a random number number between 1 and 100.
import random
num=random.randint(1,100)

#introduction to explain the rules
print("WELCOME TO GUESS GAME")
print("IAM THINKING OF NUMBER BETWEEN 1 AND 100")
print("IF YOUR GUESS IS MORE THAN 10 AWAY FROM MY NUMBER I WILL TELL YOU YOU'RE COLD")
print("IF YOUR GUESS IS WITHIN 10 OF MY NUMBER I WILL TELL YOU YOU'RE WARM")
print("IF YOUR GUESS IS FARTHER THAN  YOUR MOST RECENT GUESS. I WILL SAY YOU YOU'RE GETTING COLDER")
print("IF YOUR GUESS IS CLOSER THAN  YOUR MOST RECENT GUESS. I WILL SAY YOU YOU'RE GETTING WARMER")
print("LET'S PLAY!")

#create a list to store guesses
guesses=[0]

#write a while loop that asks for a valid guess.test it few times  to make sure it works.
while True:
    guess=int(input("IAM THINKING OF A NUMBER BETWEEN 1 AND 100.\n WHAT YOUR GUESS?"))
    if (guess<1) or (guess>100):
        print("OUT OF BOUND ! TRY AGAIN")
        continue
    break


#write a while loop that compares the players guess to our number.if the player guesses correctly, break from the loop.Otherwise tell the player if they are warmer or colder ,and continue asking for gesses.
while True:
    guess=int(input("IAM THINKING OF A NUMBER BETWEEN 1 AND 100.\n WHAT YOUR GUESS?"))
    if (guess<1)or(guess>100):
        print("OUT OF BOUND ! TRY AGAIN")
        continue
    if guess==num:
        print(f"CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESS!")
        break

    guesses.append(guess)

    if guesses[-2]:
        if abs(num-guess) <abs(num-guesses[-2]):
            print("WARMER")
        else:
            ("COLDER")
    else:
        if abs(num-guess)<=10:
            print("WARM!")
        else:
            print("COLD!")
