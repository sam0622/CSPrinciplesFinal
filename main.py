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
            print("1. Wordle")
            print("2. Tic-Tac-Toe")
            print("3. Hangman")
            print("4. Exit")
            try:
                choice = input("Enter your choice: ")
                if choice == "1":
                    import wordle  # Import the wordle game
                    clear()
                    print("Welcome to Wordle!")
                    wordle.game.start_game()  # Start a game of Wordle
                elif choice == "2":
                    import tictactoe  # Import the tictactoe game
                    clear()
                    print("Welcome to Tic-Tac-Toe!")
                    tictactoe.main_loop()  # Start a game of tictactoe
                elif choice == "3":
                    import hangman  # Import the hangman game
                    clear()
                    print("Welcome to hangman!")
                    hangman.game.main_loop()
                elif choice == "4":
                    clear()  # Clear the terminal
                    print("Goodbye!")
                    exit(0)
            except ValueError:
                print("Invalid choice. Please try again.")


menu = Menu()
menu.choose_game()
