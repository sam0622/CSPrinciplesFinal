"""
CS Principals final
Author: Samuel Greenfield
Author Credentials: sgreenfield517@gmail.com (Home Email),
samuel.greenfield@capeelizabethschools.org (School Email),
Sam0622 (GitHub Username)
"""

import colorama
from replit import clear  # For clearing the terminal


class Menu:

    def choose_game(self):
        """
        A function that allows the user to choose a game.
        Will loop and ask the user what game they would like to play.
        Has four options, Wordle, Tic-Tac-Toe, Hangman, and Exit
        The first three options take the user to the corresponding game, the Exit option kills the program

        Args:
            None

        Returns:
            None

        """
        while True:
            clear()  # Clear the terminal
            print("Games:")
            print("1: Wordle")
            print("2: Tic-Tac-Toe")
            print("3: Hangman")
            print("\n4: Exit")
            try:
                choice = input("Enter the number of the game you would like to play: ")
                if choice == "1":
                    import wordle  # Import the wordle game
                    clear()
                    if str.lower(input("Would you like instructions? (y/n) ")) == 'y':
                        clear()
                        # Print the instructions across multiple lines
                        # This ( lets me move the parentheses to another line
                        (print

                         ("""
Wordle is a game about words.
You have six guesses to get a five letter word
If any letter you guessed appears in the word and is in the correct spot,
The letter will be""", colorama.Fore.LIGHTGREEN_EX + colorama.Style.BRIGHT + "GREEN", """
If the letter appears in the word but is in the wrong spot,
The letter will be""", colorama.Fore.LIGHTYELLOW_EX + "YELLOW", """
And lastly, if the letter doesn't appear in the word at all,
The letter will be""", colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + """RED
"""))
                        input("Press enter to continue ")
                        pass
                    print("Welcome to Wordle!")
                    wordle.game.start_game()  # Start a game of Wordle
                elif choice == "2":
                    import tictactoe  # Import the tictactoe game
                    clear()
                    if str.lower(input("Would you like instructions? (y/n) ")) == 'y':  # Prompt for instructions
                        # Print instructions
                        (print

                         ("""
Tic-Tac-Toe is a two-player game where the goal is to line up 3 X's or O's in a row
These rows can be horizontal, diagonal, or vertical
Whoever lines up a row first, wins
If spaces are taken in a way that makes it impossible for anyone to win, the game will end in a tie

"""))
                        input("Press enter to continue ")
                    tictactoe.main_loop()  # Start a game of tictactoe
                elif choice == "3":
                    import hangman  # Import the hangman game
                    clear()
                    if str.lower(input("Would you like instructions? (y/n) ")) == 'y':
                        # Print instructions
                        (print

                         ("""
Hangman is a word game where you have to guess a word one letter at a time
If you get the letter correct, the letter will show up where it goes in the word
For example, if the word is "soup" and you guess "o", the incomplete word will show "_o__"
If the letter you guess appears more than once in the word, all spots the letter is at will be filled
For example, if the word is "hello" and you guess "l", the incomplete word will show "__ll_"
If you get a letter wrong, it will show up in a board of incorrect letters
You can not guess a letter you have already guessed, correct or incorrect
If you guess a letter incorrectly six times, you lose
The amount of guesses is represented by the graphic of the hanging person
The amount of the person's body corresponds to the number of incorrect guesses
For example, one wrong guess just shows the head, two shows the head and torso, three adds an arm, and so on

"""))
                    input("Press enter to continue")
                    print("Welcome to hangman!")
                    hangman.game.main_loop()  # Start a game of hangman
                elif choice == "4":
                    clear()  # Clear the terminal
                    print("Goodbye!")
                    exit(0)
            except ValueError:
                print("Invalid choice. Please try again.")


menu = Menu()
menu.choose_game()
