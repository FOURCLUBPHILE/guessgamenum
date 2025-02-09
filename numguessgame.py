secnum=9
guess=None

while guess != secnum:
    guess=int(input("SO..GUESS THE THE MYSTICAL NUMBER (BETWEEN 5 AND 15): "))
    if guess<secnum:
     print("TOO LOW !!! TRY AGAIN")
    elif guess>secnum:
     print("TOO HIGH!!! TRY AGAIN")
else:
    print("Congratulations! You guessed the secret number.")