
while True:
    guess=int(input("IAM THINKING OF A NUMBER BETWEEN 1 AND 100.\n WHAT YOUR GUESS?"))
    if guess<1 or guess>100:
        print("OUT OF BOUND ! TRY AGAIN")
        continue
    if guess==num:
        print(f"CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESS!")
        break

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
