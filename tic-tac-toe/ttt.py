#!/usr/bin/python3
import random


# Function to display the Tic Tac Toe board
def display_board(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])


# Function to take player input (X or O)
def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Player 1: Do you want to be X or O? ").upper()
    return ('X', 'O') if marker == 'X' else ('O', 'X')


# Function to take player input (X or O) for Player 2
def player2_input(player1_marker):
    return 'O' if player1_marker == 'X' else 'X'


# Function to place the marker on the board
def place_marker(board, marker, position):
    board[position] = marker


# Function to check if a player has won
def check_win(board, marker):
    return (
        (board[1] == board[2] == board[3] == marker) or
        (board[4] == board[5] == board[6] == marker) or
        (board[7] == board[8] == board[9] == marker) or
        (board[1] == board[4] == board[7] == marker) or
        (board[2] == board[5] == board[8] == marker) or
        (board[3] == board[6] == board[9] == marker) or
        (board[1] == board[5] == board[9] == marker) or
        (board[3] == board[5] == board[7] == marker)
    )


# Function to check if the board is full (a tie)
def check_tie(board):
    return ' ' not in board[1:]


# Function to get player's next move
def get_player_move(board):
    position = 0
    while position not in range(1, 10) or not is_space_free(board, position):
        position = int(input("Choose your next position (1-9): "))
    return position


# Function to check if a space on the board is free
def is_space_free(board, position):
    return board[position] == ' '


# Function to check if the board is full
def is_board_full(board):
    return ' ' not in board[1:]


# Function to get a random computer move
def get_computer_move(board):
    available_moves = [position for position in range(1, 10) if is_space_free(board, position)]
    return random.choice(available_moves)


# Function to ask players if they want to play again
def play_again():
    return input("Do you want to play again? Enter 'yes' or 'no': ").lower().startswith('y')


# Main game logic
def tic_tac_toe():
    print("Welcome to Tic Tac Toe!")

    while True:
        # Set up the board
        board = [' '] * 10
        player1_marker, player2_marker = player_input()

        # Determine player 2 (computer or second player)
        player2_type = input("Enter '1' to play with a second player or '2' to play with the computer: ")
        if player2_type == '1':
            print("Player 2 will be a second player.")
            player2_marker = player2_input(player1_marker)
        else:
            print("Player 2 will be the computer.")

        print("Player 1 will go first.")
        input("Are you ready to play? Press Enter to continue...")

        game_on = True
        while game_on:
            # Player 1's turn
            display_board(board)
            position = get_player_move(board)
            place_marker(board, player1_marker, position)

            if check_win(board, player1_marker):
                display_board(board)
                print("Congratulations! Player 1 wins!")
                game_on = False
            else:
                if check_tie(board):
                    display_board(board)
                    print("It's a tie!")
                    break
                else:
                    if player2_type == '1':
                        turn = 'Player 2'
                    else:
                        # Computer's turn
                        display_board(board)
                        position = get_computer_move(board)
                        place_marker(board, player2_marker, position)

                        if check_win(board, player2_marker):
                            display_board(board)
                            if player2_type == '2':
                                print("Computer wins!")
                            else:
                                print("Player 2 wins!")
                            game_on = False
                        else:
                            if check_tie(board):
                                display_board(board)
                                print("It's a tie!")
                                break
                            else:
                                turn = 'Player 1'

        if not play_again():
            break

# Run the game
tic_tac_toe()
