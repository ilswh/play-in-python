# imports a random word
import random
import os
# imports words from words.py
from words import word_list
# from stages import display_hangman
from lives import display_hangman


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


# gets a word for the game
def get_word():
    word = random.choice(word_list)
    return word.upper()


# for the actual interactive game
# display the word
def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Welcome! Here you can play hangman, with one clue.")
    print("The word is always an emotion.")
    print("The rules are simple.")
    print("Pick a letter or word until you guessed the right word.")
    print("You must do it before the man get's hanged.")
    print("Lets play!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n") 
    while not guessed and tries > 0:
        guess = input("Guess a letter or word: ").upper()
        clear()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Woohoo,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    clear()
    if guessed:
        print("WOOHOO! You guessed the right word! Congratulations!")
    else:
        print("BUHU. No more tries. The word was " + word + ".")


# sews everything together
def main():
    # runs the game once
    word = get_word()
    play(word)
    # creates the option to play again as long as the user chooses yes to play again
    while True:
        again = input("Play Again? (Y/N) ").upper()
        clear()
        if again == "Y":
            word = get_word()
            play(word)
        elif again == "N":
            print("Thanks for playing hangman!")
            break
        else:
            print(f"{again} is invalid. Try again.")


# run the main python application (play.py)
if __name__ == "__main__":
    clear()
    main()
