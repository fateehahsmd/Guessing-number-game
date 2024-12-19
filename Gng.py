# Python number guessing game
import random

def number_guessing_game():
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 10
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 10  # Maximum number of attempts

    print(f"Welcome to the Number Guessing Game!")
    print(f"I have selected a number between {lower_bound} and {upper_bound}.")
    print(f"You have {attempts} attempts to guess it.")

    for attempt in range(attempts):
        guess = int(input(f"Attempt {attempt + 1}: Enter your guess: "))

        if guess < lower_bound or guess > upper_bound:
            print(f"Please guess a number between {lower_bound} and {upper_bound}.")
            continue

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly!")
            break
    else:
        print(f"Sorry, you've used all your attempts. The number was {secret_number}.")

# Start the game
number_guessing_game()