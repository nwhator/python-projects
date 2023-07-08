#!/usr/bin/python3
import random


# Function to generate a random number between 1 and 10
def generate_random_number(level):
    if level == 1:
        return random.randint(1, 10)
    elif level == 2:
        return random.randint(1, 25)
    elif level == 3:
        return random.randint(1, 50)


# Function to get user's name
def get_user_name():
    name = input("Enter your name: ")
    return name


# Function to get user's guess
def get_user_guess():
    while True:
        try:
            guess = int(input("Guess the number: "))
            return guess
        except ValueError:
            print("Invalid input! Please enter a valid number.")


# Function to validate user's guess
def validate_guess(guess, target, level):
    if level == 1:
        valid_range = (1, 10)
    elif level == 2:
        valid_range = (1, 25)
    elif level == 3:
        valid_range = (1, 50)
    else:
        valid_range = (1, target)

    if guess < valid_range[0] or guess > valid_range[1]:
        print(f"Invalid guess! The number should be between {valid_range[0]} and {valid_range[1]}.")
        return False
    return True


# Function to provide hints based on user's guess
def provide_hint(guess, target):
    if guess < target:
        print("Higher! Try guessing a larger number.")
    elif guess > target:
        print("Lower! Try guessing a smaller number.")


# Function to play the number guessing game
def play_game(level):
    target_number = generate_random_number(level)
    guesses_taken = 0
    guess_limit = get_guess_limit(level)

    name = get_user_name()
    print(f"Hello {name}! Let's play the Number Guessing Game.")
    print(f"\nLevel {level}")
    print("---------")
    print(f"You have {guess_limit} guesses to find the number.")

    while guesses_taken < guess_limit:
        guess = get_user_guess()

        if not validate_guess(guess, target_number, level):
            continue

        guesses_taken += 1

        if guess == target_number:
            print(f"Congratulations, {name}! You guessed the correct number in {guesses_taken} attempts!")
            return True

        provide_hint(guess, target_number)

    print(f"Oops! You ran out of guesses, {name}. The correct number was {target_number}. Better luck next time!")
    return True


# Function to get the guess limit for each level
def get_guess_limit(level):
    if level == 1:
        return 3
    elif level == 2:
        return 5
    elif level == 3:
        return 10

# Main program
play_again = True
score = 0

print("Welcome to the Number Guessing Game!")
print("------------------------------------")

while play_again:
    level = 1
    while level <= 3:
        guess_limit = get_guess_limit(level)
        print(f"\nLevel {level}")
        print(f"You have {guess_limit} guesses available.")
        game_result = play_game(level)
        if game_result:
            score += 1
            level += 1
        else:
            choice = input("Do you want to restart the level? (yes/no): ")
            if choice.lower() != "yes":
                break


    print(f"\nGame Over! Your final score: {score}")

    while True:
        choice = input("Do you want to play again? (yes/no): ")
        if choice.lower() == "yes" or choice.lower() == "no":
            break
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")
    play_again = choice.lower() == "yes"
    score = 0

print(f"Thanks for playing!")
