"""
Hangman for CS Principals final
Author: Samuel Greenfield
Author Credentials: sgreenfield517@gmail.com(Home Email),
samuel.greenfield@capeelizabethschools.org(School Email),
Sam0622(GitHub Username)

"""
# TODO: Make the main game loop, also comment and docstring
from wonderwords import RandomWord
from replit import clear


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
        self.incomplete_word = ["_" for _ in self.word]  # Adjust amount of underscores
        self.guessed_letters = []  # All guessed letters
        self.correct_guesses = []  # Only correct letters
        self.incorrect_guesses = []  # Only incorrect letters
        self.guesses = 0

    def generate_word(self):
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
        for i in range(0, len(self.incorrect_guesses), 3):  # A loop that starts at zero, increments by three, and stops at the length of the list
            print(" ".join(self.incorrect_guesses[i:i+3]))  # Prints the 3 entries from the list selected above

    def print_hangman(self, stage):
        """
        Prints the hangman in different stages depending on the times the player has guesses

        Args:
            stage (int): The stage the hangman is in

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
            case 4:
                print("""
                      ________
                      |      |
                      |      O    
                      |     /|\
                      |
                      |
                      """)
            case 5:
                print("""
                      ________
                      |      |
                      |      O    
                      |     /|\
                      |     /
                      |
                      """)
            case 6:
                print("""
                      ________
                      |      |
                      |      O    
                      |     /|\
                      |     / \
                      |
                      """)

    def main_loop(self):
        while self.incomplete_word != self.word:
            self.print_hangman(self.guesses)
            self.print_incorrect_letters()
            print(str.join("", self.incomplete_word))
            self.guess()








game = Hangman()
game.main_loop()
