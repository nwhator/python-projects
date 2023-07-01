#!/usr/bin/python3
import random


# Function to generate a random number between 1 and 10
def generate_random_number():
    return random.randint(1, 10)


# Function to get user's name
def get_user_name():
    name = input("Enter your name: ")
    return name


# Function to get user's guess
def get_user_guess():
    while True:
        try:
            guess = int(input("Guess the number (between 1 and 10): "))
            return guess
        except ValueError:
            print("Invalid input! Please enter a valid number.")


# Function to validate user's guess
def validate_guess(guess, target):
    if guess < 1 or guess > 10:
        print("Invalid guess! The number should be between 1 and 10.")
        return False
    return True


# Function to provide hints based on user's guess
def provide_hint(guess, target):
    if guess < target:
        print("Higher! Try guessing a larger number.")
    elif guess > target:
        print("Lower! Try guessing a smaller number.")


# Function to play the number guessing game
def play_game():
    target_number = generate_random_number()
    guess_limit = 3
    guesses_taken = 0

    name = get_user_name()
    print(f"Hello {name}! Let's play the Number Guessing Game.")

    while guesses_taken < guess_limit:
        guess = get_user_guess()

        if not validate_guess(guess, target_number):
            continue

        guesses_taken += 1

        if guess == target_number:
            print(f"Congratulations, {name}! You guessed the correct number in {guesses_taken} attempts!")
            return True

        provide_hint(guess, target_number)

    print(f"Oops! You ran out of guesses, {name}. The correct number was {target_number}. Better luck next time!")
    return True


# Main program
play_again = True
score = 0

while play_again:
    game_result = play_game()
    if game_result:
        score += 1

    print(f"Your current score: {score}")

    while True:
        choice = input("Do you want to play again? (yes/no): ")
        if choice.lower() == "yes" or choice.lower() == "no":
            break
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")
    play_again = choice.lower() == "yes"

print(f"Thanks for playing! Your final score: {score}")
