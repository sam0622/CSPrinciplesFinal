"""
Hangman for CS Principals final
Author: Samuel Greenfield
Author Credentials: sgreenfield517@gmail.com (Home Email),
samuel.greenfield@capeelizabethschools.org (School Email),
Sam0622 (GitHub Username)
"""

from time import sleep  # Grab a package to pause the program

from replit import clear  # Grab a package for clearing the terminal
from wonderwords import RandomWord  # Grab a package for word generation


class Hangman:
    """
    The game of Hangman. Handles game logic, main loops, guessing, and outcomes

    Attributes:
        word (str): A randomly generated word with a length of 4 to 16, the word that the player has to guess
        incomplete_word (list, str): the incomplete word, and the letters guessed correctly,
            defaults to a list of underscores the length of the word
        guessed_letters (list, str): Any letters the player has guessed, including correct and incorrect guesses
        correct_guesses (list, str): Any letters the player has guessed that do appear in the word
        incorrect_guesses (list, str): Any letters the player has guessed that do not appear in the word
        guesses (int): The amount of times the player has guessed, correct or incorrect

    Methods:
        __init__(): Sets a bunch of attributes seen above ^
        generate_word(): Generates a word randomly and gets rid of characters like "-" and "'"
        guess(): Prompts the player for a guess and makes sure it is valid
        check_guess(): Checks if the guessed letter is in the word and adds it to incomplete_word
        print_incorrect_letters(): Prints all the guessed letters that are not in the word
        print_hangman(): Print the hangman himself
    """

    def __init__(self):
        """
        Sets a bunch of attributes, explained above ^
        """
        self.word = self.generate_word()  # Generate a word
        self.incomplete_word = ["_" for _ in self.word]  # The incomplete word for the player to piece together
        self.guessed_letters = []  # All guessed letters
        self.correct_guesses = []  # Only correct letters
        self.incorrect_guesses = []  # Only incorrect letters
        self.guesses = 0  # Number of times the player has guessed

    def generate_word(self):
        """
        Generates a random word with length between 4 and 16, sanitizes it, and returns it

        Args:
            None
,
        Returns:
            r_word (str): The sanitized random word
        """
        r = RandomWord()  # Defines an instance of the RandomWord class
        r_word = r.word(word_min_length=4, word_max_length=16)  # Generates a word with length from 4 to 16
        r_word = r_word.lower()  # Converts the word to lowercase

        # Gets rid of problematic characters
        while "-" in r_word:
            r_word = r_word.replace("-", "")
        while "'" in r_word:
            r_word = r_word.replace("'", "")

        return r_word  # Returns the scrubbed word

    def guess(self, devmode=False):
        """
        This function gets the players guess and sends it to check_guess.
        If you have guessed incorrectly once or more before, it will show all wrong letters.
        The guess should be a one letter string that is in the English Alphabet.

        Args:
            None

        Returns:
            None
        """
        while True:
            if devmode:
                print(f"game.word == {self.word}")
            guess = input("Guess a letter: ")
            # If the letter is a letter, is just one letter, and has not been guessed already
            if guess.isalpha() and len(guess) == 1 and guess not in self.guessed_letters:
                self.guessed_letters.append(guess)  # Add the letter to the ones that have been guessed before
                self.check_guess(guess)  # Check the guess
                break
            elif guess in self.guessed_letters:
                print(f"You have already guessed the letter '{guess}'")
                self.print_hangman(self.guesses)
                self.print_incorrect_letters()
                print(str.join("", self.incomplete_word))  # Print the incomplete word
            else:
                clear()
                print("Invalid guess, please guess again")
                self.print_hangman(self.guesses)
                self.print_incorrect_letters()
                print(str.join("", self.incomplete_word))  # Print the incomplete word

    def check_guess(self, guess):
        """
        This function takes a given letter, checks if it is in the word, and updates the incomplete word.

        Args:
            guess (str): The players guess. Should be only one letter

        Returns:
            None
        """
        print("Guess: ", guess)  # Print your guess
        if guess in self.word:  # If the guess is in the chosen word
            length = len(self.word)
            for i in range(0, length):  # Check what position the guess is in
                if guess == self.word[i]:
                    self.correct_guesses.append(guess)
                    self.incomplete_word[i] = guess  # Add the letter to the incomplete word
        else:
            self.guesses += 1
            self.incorrect_guesses.append(guess)
            print("That is not in the word, try again")

    def print_incorrect_letters(self):
        """
        Prints the list of incorrect guesses, with 3 entries per line

        Args:
            None

        Returns:
            None
        """
        # A loop that starts at zero, increments by three, and stops at the length of the list
        for i in range(0, len(self.incorrect_guesses), 3):
            print(" ".join(self.incorrect_guesses[i:i + 3]))  # Prints the 3 entries from the list selected above

    def print_hangman(self, stage):
        """
        Prints the hangman in different stages depending on the times the player has guesses

        Args:
            stage (int): The stage the hangman is in, higher stage, more man

        Returns:
            None
        """
        match stage:  # This is essentially a streamlined if else if block
            #  case = the value of stage, for example, if the value is one, case 1 executes
            case 0:
                print("""
                     ________
                     |      |
                     |          
                     |
                     |
                     | 
                """)
            case 1:
                print("""
                     ________
                     |      |
                     |      O    
                     |
                     |
                     | 
                 """)
            case 2:
                print("""
                      ________
                      |      |
                      |      O    
                      |     /
                      |
                      |
                      """)
            case 3:
                print("""
                          ________
                          |      |
                          |      O    
                          |     /|
                          |
                          |
                          """)
            case 4:  # The "\" is an escape character, to make it not do that, you have to put two, it shows up as one \
                print("""
                      ________
                      |      |
                      |      O    
                      |     /|\\
                      |
                      |
                      """)
            case 5:
                print("""
                      ________
                      |      |
                      |      O    
                      |     /|\\
                      |     /
                      |
                      """)
            case 6:
                print("""
                      ________
                      |      |
                      |      O    
                      |     /|\\
                      |     / \\
                      |
                      """)
            case _:  # _ means a default case, functionally the else at the very end of an if else if block
                print("ERROR: Player guesses exceeds 6.")
                raise ValueError  # Kills the program with a ValueError

    def play_again(self):
        """
        Restarts the game or goes back to the menu depending on user input

        Args:
            None

        Returns:
            None
        """
        self.__init__()  # Reinitialize the Hangman class and variables
        if str.lower(input("Do you want to play again? (y/n) ")) == "y":
            # Fake loading bar
            # The sleep function pauses the program for a given time
            print("Starting new game.")
            sleep(1)
            print("Starting new game..")
            sleep(1)
            print("Starting new game...")
            sleep(1)
            clear()
            self.main_loop()  # Restart the game
        else:
            clear()  # Clear the terminal
            print("Goodbye!")
            sleep(0.5)
            clear()
            import main  # Grab the main menu script so we can use it
            main.menu.choose_game()  # Return to menu

    def main_loop(self, devmode=False):
        """
        The main game loop. Checks for win and loss conditions, then prints info and has the player guess

        Args:
            None

        Returns:
            None
        """
        while True:
            clear()  # Clear the terminal

            # Loss detection
            if self.guesses >= 6:
                self.print_hangman(self.guesses)
                print("You lost! The word was", self.word)
                self.play_again()  # Prompt to play again
                break  # Break the game loop

            # Win detection
            if ("".join(self.incomplete_word)) == self.word:  # If the incomplete word is complete
                self.print_hangman(self.guesses)
                self.print_incorrect_letters()
                print("".join(self.incomplete_word))  # Print the incomplete word
                print("You win! The word was", self.word)
                self.play_again()  # Prompt to play again
                break

            # The actual input loop. Print info, and guess
            self.print_hangman(self.guesses)
            self.print_incorrect_letters()
            print(str.join("", self.incomplete_word))  # Print the incomplete word
            self.guess(devmode)


game = Hangman()  # Create an instance of hangman
