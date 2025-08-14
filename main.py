import random

while True:
    min_val = input("Select the lowest number: ")
    try:
        min_val = int(min_val)
        break
    except ValueError:
        print("Wrong input. Give a number: ")

while True:
    max_val = input("Select the highest number: ")
    try:
        max_val = int(max_val)
        if max_val > min_val:
            break
        else:
            print(f"The second number must be higher than {min_val}.")
    except ValueError:
        print("Wrong input. Give a number: ")

answer = random.randint(min_val, max_val)
guesses = 0

while True:
    if guesses >= 10:
        print(f"You ran out of guesses. The answer was {answer}")
        break
    else:
        while True:
            guess = input(f"Guess a number between {min_val} and {max_val}: ")
            try:
                guess = int(guess)
                if min_val <= guess <= max_val:
                    guesses += 1
                    break
                else:
                    print(f"The number must be between {min_val} and {max_val}.")
            except ValueError:
                print("Wrong input. Give a number: ")

        if guess < answer:
            print("Too low! Guess a higher number.")
        elif guess > answer:
            print("Too high! Guess a lower number.")
        else:
            print(f"Correct. The answer was {answer}")
            print(f"You found the answer in {guesses} guesses.")
            break



