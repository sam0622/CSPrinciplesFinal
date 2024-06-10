"""
Tic-Tac-Toe for CS Principals final
Author: Samuel Greenfield
Author Credentials: sgreenfield517@gmail.com (Home Email),
samuel.greenfield@capeelizabethschools.org (School Email),
Sam0622 (GitHub Username)
"""

from time import sleep  # Grab a command to wait
import colorama  # Grab a package for colored output
from replit import clear  # Grab a command to clear the terminal

colorama.init(autoreset=True)  # Initiate colorama

game_board = [[" ", " 1", "2", "3"],  # Define the game board
              ["1 ", "_", "_", "_"],
              ["2 ", "_", "_", "_"],
              ["3 ", "_", "_", "_"]]

colored_board = [[" ", " 1", "2", "3"],  # Make a copy of the board for colored output
                 ["1 ", "_", "_", "_"],
                 ["2 ", "_", "_", "_"],
                 ["3 ", "_", "_", "_"]]  # Make a copy of the board for colored output
free_spaces = 9

def print_board():
    """
    A function to print the colored board.

    Args:
        None

    Returns:
        None
    """
    #  Print the game board
    for row in colored_board[0:]:
        print(" ".join(row[0:]))


def prompt_input(player):
    """
    Prompts the user for a row and column input for a move on the board,
    Runs it through a check to see if the move is valid.
    Updates the game board with the player's symbol.
    Updates the colored board with the player's symbol and color.

    Args:
        player (str): The player symbol to draw, either "X" or "O"

    Returns:
        None

    Globals:
        game_board, free_spaces, colored_board
    """
    global game_board, free_spaces, colored_board  # Access global variables
    clear()  # Clear terminal
    preview_board = [row[:] for row in colored_board]  # Update the preview board

    # Input loop
    while True:
        try:  # Grab input
            print_board()
            chosen_row = int(input("Enter horizontal row: "))  # Prompt for row
            if chosen_row < 1 or chosen_row > 3:
                print("Invalid input. Please try again.(1-3)")
                continue
            chosen_col = int(input("Enter vertical column: "))  # Prompt for column
            if chosen_col < 1 or chosen_col > 3:
                print("Invalid input. Please try again.(1-3)")
                continue
        except ValueError:
            # If input is invalid, try again,
            clear()
            print("Invalid input. Please try again.(1-3)")  # Print an error
            continue

        # If input is out of bounds, error out and try again
        #if chosen_row < 1 or chosen_row > 3 or chosen_col < 1 or chosen_col > 3:
            #print("Invalid input. Please try again.(1-3)")
            #clear()

        # If desired spot is taken, error out and try again
        if preview_board[chosen_row][chosen_col] != "_":
            clear()
            print(f"The spot {chosen_row},{chosen_col} is already taken, please choose a different one")
        else:
            clear()
            print("Previewing move...")
            if player == "X":
                # Puts the player's symbol in the chosen row and column in red and then resets color
                preview_board[chosen_row][
                    chosen_col] = colorama.Fore.RED + colorama.Style.BRIGHT + "X" + colorama.Style.RESET_ALL
                free_spaces -= 1  # Reduce the number of free spaces by 1
            elif player == "O":
                # Puts the player's symbol in the chosen row and column in blue and then resets color
                preview_board[chosen_row][
                    chosen_col] = colorama.Fore.BLUE + colorama.Style.BRIGHT + "O" + colorama.Style.RESET_ALL
                free_spaces -= 1  # Reduce the number of free spaces by 1

            # Print the preview board
            for row in preview_board[0:]:
                print(" ".join(row[0:]))

            # Input confirmation
            confirmation = input("Is this correct? (y/n): ")  # Get user confirmation
            if confirmation == "y":  # If input is confirmed
                game_board[chosen_row][chosen_col] = player  # Update the backend game board
                print("game board")
                for row in game_board:
                    print(" ".join(row[0:]))

                if player == "X":
                    # Puts the player's symbol in red and then resets to prevent unintentional coloring
                    colored_board[chosen_row][
                        chosen_col] = colorama.Fore.RED + colorama.Style.BRIGHT + "X" + colorama.Style.RESET_ALL
                    free_spaces -= 1  # Reduce the number of free spaces by 1
                    clear()  # Clear the terminal
                    return
                elif player == "O":
                    # Puts the player's symbol in blue and then resets to prevent unintentional coloring
                    colored_board[chosen_row][
                        chosen_col] = colorama.Fore.BLUE + colorama.Style.BRIGHT + "O" + colorama.Style.RESET_ALL
                    free_spaces -= 1  # Reduce the number of free spaces by 1
                    clear()  # Clear the terminal
                    return

                else:  # If the player isn't X or O, throw a ValueError and crash
                    print("Invalid player symbol in function prompt_input.")  # Print an error message
                    raise ValueError  # Throw error

            else:  # If input is not confirmed
                preview_board = [row[:] for row in colored_board]  # Reset the preview board
                clear()  # Clear the terminal
                print("Cancelling move...")


def check_win(player):
    """
    A function to check if a player has won the game based on the current state of the game board.
    Args:
        player (str): The player to check for winning (should be either "X" or "O")

    Returns:
        bool: True if the player has won, False otherwise
    """
    if game_board[1][1] == player and game_board[1][2] == player and game_board[1][3] == player:
        return True  # Check top row
    elif game_board[2][1] == player and game_board[2][2] == player and game_board[2][3] == player:
        return True  # Check middle row
    elif game_board[3][1] == player and game_board[3][2] == player and game_board[3][3] == player:
        return True  # Check bottom row
    elif game_board[1][1] == player and game_board[2][1] == player and game_board[3][1] == player:
        return True  # Check left column
    elif game_board[1][2] == player and game_board[2][2] == player and game_board[3][2] == player:
        return True  # Check middle column
    elif game_board[1][3] == player and game_board[2][3] == player and game_board[3][3] == player:
        return True  # Check right column
    elif game_board[1][1] == player and game_board[2][2] == player and game_board[3][3] == player:
        return True  # Check diagonals
    elif game_board[1][3] == player and game_board[2][2] == player and game_board[3][1] == player:
        return True  # Check diagonals
    else:
        return False


def play_again():
    """
    Restarts the game or goes back to menu according to user input

    Args:
        None

    Returns:
        None

    Globals:
        game_board, colored_board, free_spaces, turn
    """
    global game_board, colored_board, free_spaces, turn

    game_board = [[" ", " 1", "2", "3"],  # Reset the game board
                  ["1 ", "_", "_", "_"],
                  ["2 ", "_", "_", "_"],
                  ["3 ", "_", "_", "_"]]

    colored_board = game_board  # Reset the colored board
    free_spaces = 9  # Reset the free spaces counter
    turn = 0  # Reset the turn counter

    choice = str.lower(input("Would you like to play again? (y/n) "))
    if choice == "y" or choice == "yes":
        # Fake loading bar
        print("Starting new game.")
        sleep(1)
        print("Starting new game..")
        sleep(1)
        print("Starting new game...")
        sleep(1)
        main_loop()  # Restart the game
    else:
        clear()  # Clear the terminal
        print("Goodbye!")
        sleep(0.5)
        clear()
        import main  # Dynamically grab the main menu script
        main.menu.choose_game()  # Return to menu


turn = 0  # Reset the turn counter


def main_loop():
    """
    A main game loop that takes turns for players X and O, checks for wins or ties, and prompts for user input.

    Args:
        None

    Returns:
        None

    Globals:
        turn
    """
    global turn

    while True:
        print_board()
        print("It's X's turn!")
        prompt_input("X")  # Prompt user for input
        if check_win("X"):  # If X has won:
            print_board()
            print("X has won!")
            break  # Break the loop if X has won

        turn += 1  # Increment the turn counter by one

        if turn == 9:  # Tie detection
            print("It's a tie!")
            break

        print_board()
        print("It's O's turn!")
        prompt_input("O")
        if check_win("O"):  # If O has won:
            print("O has won!")
            break

        turn += 1  # Increment the turn counter by one

    play_again()  # Prompt to play again
