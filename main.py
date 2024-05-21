from replit import clear  # For clearing the terminal

class Menu:
    def __init__(self):
        """
        Does nothing
        """
        pass

    def choose_game(self):
        """
        A function that allows the user to choose a game.
        Will loop and ask the user what game they would like to play.
        Try Except loop handles input errors.

        Args:
            None

        Returns:
            None
        """
        while True:
            clear()
            print("Games:")
            print("1. Wordle")
            print("2. Tic-Tac-Toe")
            print("4. Exit")
            try:
                choice = input("Enter your choice: ")
                if choice == "1":
                    import wordle
                    clear()  # Clear the terminal
                    print("Welcome to Wordle!")
                    wordle.game.start_game()  # Start a game of Wordle
                elif choice == "2":
                    import tictactoe
                    clear()  # Clear the terminal
                    print("Welcome to Tic-Tac-Toe!")
                    tictactoe.main_loop()
                elif choice == "4":
                    clear()  # Clear the terminal
                    print("Goodbye!")
                    exit(0)
            except ValueError:
                print("Invalid choice. Please try again.")


menu = Menu()
menu.choose_game()
