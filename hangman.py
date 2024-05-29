"""
Hangman for CS Principals final
Author: Samuel Greenfield
Author Credentials: sgreenfield517@gmail.com(Home Email),
samuel.greenfield@capeelizabethschools.org(School Email),
Sam0622(GitHub Username)
"""

from wonderwords import RandomWord
from replit import clear
from time import sleep


class Hangman:
    """
    The game of Hangman

    Params:
        word (str): A randomly generated word with a length of 4 to 16, the word that the player has to guess
        incomplete_word (list, str): the incomplete word, and the letters guessed correctly,
            defaults to a list of underscores the length of the word
        guessed_letters (list, str): Any letters the player has guessed, including correct and incorrect guesses
        correct_guesses (list, str): Any letters the player has guessed that do appear in the word
        incorrect_guesses (list, str): Any letters the player has guessed that do not appear in the word
        guesses (int): The amount of times the player has guessed, correct or incorrect

    Methods:
        __init__()
        generate_word()
        guess()
        check_guess()
        print_incorrect_letters()
        print_hangman()
    """

    def __init__(self):
        self.word = self.generate_word()
        print(self.word)
        self.incomplete_word = ["_" for _ in self.word]  # Adjust amount of underscores
        self.guessed_letters = []  # All guessed letters
        self.correct_guesses = []  # Only correct letters
        self.incorrect_guesses = []  # Only incorrect letters
        self.guesses = 0

    def generate_word(self):
        """
        Generates a random word with length between 4 and 16, sanitizes it, and returns it

        Args:
            None
,
        Returns:
            r_word (str): The sanitized random word
        """
        r = RandomWord()
        r_word = r.word(word_min_length=4, word_max_length=16)
        r_word = r_word.lower()

        while "-" in r_word:
            r_word = r_word.replace("-", "")
        while "'" in r_word:
            r_word = r_word.replace("'", "")

        return r_word

    def guess(self):
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
            guess = input("Guess a letter: ")
            if guess.isalpha() and len(guess) == 1 and guess not in self.guessed_letters:
                self.guessed_letters.append(guess)
                self.check_guess(guess)
                break
            elif guess in self.guessed_letters:
                print("You have already guessed this letter")
            else:
                print("Invalid guess, please guess again")

    def check_guess(self, guess):
        """
        This function takes a given letter, checks if it is in the word, and updates the incomplete word.

        Args:
            guess (str): The players guess. Should be only one letter

        Returns:
            None

        """
        print("Guess: ", guess)
        if guess in self.word:
            length = len(self.word)
            for i in range(0, length):
                if guess == self.word[i]:
                    self.correct_guesses.append(guess)
                    self.incomplete_word[i] = guess
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
            print(" ".join(self.incorrect_guesses[i:i+3]))  # Prints the 3 entries from the list selected above

    def print_hangman(self, stage):
        """
        Prints the hangman in different stages depending on the times the player has guesses

        Args:
            stage (int): The stage the hangman is in, higher stage, more man

        Returns:
            None

        """
        match stage:  # This is essentially a streamlined if, elif block
            #  case = the value of stage, if the value is one, case 1 executes
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
            case _:
                print("ERROR: Player guesses exceeds 6.")
                raise ValueError


    def play_again(self):
        """
        Restarts the game or goes back to the menu depending on user input

        Args:
            None

        Returns:
            None
        """
        if str.lower(input("Do you want to play again? (y/n) ")) == "y":
            self.__init__()  # Reintialize the Hangman class and variables
            # Fake loading bar
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
            input()  # Wait for input
            clear()
            import main  # Dynamically grab the main menu script
            main.menu.choose_game()  # Return to menu




    def main_loop(self):
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
                print("you dead, dead as hell. The word was", self.word)
                self.play_again()  # Prompt to play again
                break

            # Win detection
            if ("".join(self.incomplete_word)) == self.word:
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
            self.guess()








game = Hangman()
game.main_loop()
