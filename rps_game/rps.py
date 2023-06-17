#!/usr/bin/python3.11
import random
import tkinter as tk
from PIL import ImageTk, Image

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle button clicks
def handle_choice(choice):
    computer_choice = random.choice(choices)
    user_label.config(text="You chose: " + choice.capitalize())
    computer_label.config(text="Computer chose: " + computer_choice.capitalize())
    result_label.config(text=determine_winner(choice, computer_choice))

# Create the main window
window = tk.Tk()
window.title("Rock Paper Scissors")

# Load images or emojis
rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png"))

# Create the choice buttons
choices = ['rock', 'paper', 'scissors']
buttons = []
for choice in choices:
    button = tk.Button(window, image=eval(choice + "_img"), command=lambda choice=choice: handle_choice(choice))
    buttons.append(button)

# Create labels for displaying user choice, computer choice, and result
user_label = tk.Label(window, text="Make your choice", font=("Arial", 12))
computer_label = tk.Label(window, text="Computer's choice", font=("Arial", 12))
result_label = tk.Label(window, text="", font=("Arial", 16, "bold"))

# Position the widgets using grid layout
user_label.grid(row=0, column=0, columnspan=3, pady=10)
computer_label.grid(row=1, column=0, columnspan=3)
result_label.grid(row=2, column=0, columnspan=3, pady=10)
for i, button in enumerate(buttons):
    button.grid(row=3, column=i, padx=10, pady=10)

# Start the GUI event loop
window.mainloop()

