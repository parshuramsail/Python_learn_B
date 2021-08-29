import random
num=random.randint(1,100)

print("welcome to guess game")
print("i am thinking of number between 1 t0 100")
print("if your guess is farther than 10 away from my number i will tell you youre cold")
print("if your guess is within 10 of my number i will tell you toure warm ")
print("if your guess is farther than your most recent guess away from my number i will tell you youre colder")
print("if your guess is closer to recent gues number of my number i will tell you toure warmer ")
print("lets play")

guesses=[0]

while True:
    guess=int(input("enter a number between 1 to 100"))
    if num<1 or num>100:
        print("out of bound")
        continue
    break

while True:
     guess=int(input("enter a number between 1 to 100"))
     if num<1 or num>100:
        print("out of bound! try again")
        continue

     if guess==num:
         print(f"CONGRATULATION .YOU WON\n you guessed it in (len{guesses} guesses")
         break

     guesses.append(guess)

     if guesses[-2]:
          if abs(num-guess)>abs(num-guesses[-2]):
            print("warmer")
          else:
            print("colder")
     else:
         if abs(num-guess)<=10:
            print("warm")
         else:
            print("cold")



