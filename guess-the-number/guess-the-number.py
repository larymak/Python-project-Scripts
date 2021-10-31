import random

try:
    lb = int(input("Enter the lower limit>>"))
    ub = int(input("Enter the upper limit>>"))
    number = random.randint(lb, ub+1)
    while True:
        guess = int(input("Enter your guess>>"))
        if guess<number:
            print("go higher")
        elif guess>number:
            print("go lower")
        elif guess==number:
            break

    print("Congrats! You guessed the number.")
except:
    pass
