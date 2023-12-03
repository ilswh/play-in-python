# imports a random word
import random
# imported for clear function
import os
# accesses words from diffrent categories
from primary_emotions import primary_emotions_list
from happy_emotions import happy_emotions_list
from sad_emotions import sad_emotions_list
# accesses hangman-art
from stages import display_hangman


global category


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


def get_word(category):
    """
    Gets a word for the game.
    """
    if category == "Primary Emotions":
        selected_list = primary_emotions_list
    if category == "Happy Emotions":
        selected_list = happy_emotions_list
    if category == "Sad Emotions":
        selected_list = sad_emotions_list

    # get a random word from the selected list
    word = random.choice(selected_list)
    return word.upper()


def welcome():
    """
    Welcome text for the user before the game starts.
    """
    print("Welcome! Here you can play hangman, with one clue.")
    print("The word is always an emotion.")
    print("The rules are simple.")
    print("Pick a letter or word until you guessed the right word.")
    print("You must do it before the man get's hanged.")
    print("Lets play!")


def play(word):
    """
    The actual interactive game.
    (Generates a word).
    """
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
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
                indices = [
                    i for i, letter in enumerate(word) if letter == guess]
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
            print(f"{guess} is not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    clear()
    if guessed:
        print(f"WOOHOO! You guessed the right word, {word}! Congratulations!")
    else:
        print("BUHU. No more tries. The word was " + word + ".")


def choose_category():
    """
    Gives the player an option to select a category.
    """
    global category
    while True:
        print("\nSelect a category:")
        user_choice = input("1. Primary Emotions\n2. Happy Emotions\n3. Sad Emotions\n>")
        clear()
        if user_choice == "1":
            category = "Primary Emotions"
            print("You've selected Primary Emotions")
            break
        elif user_choice == "2":
            category = "Happy Emotions"
            print("You've selected Happy Emotions")
            break
        elif user_choice == "3":
            category = "Sad Emotions"
            print("You've selected Sad Emotions.")
            break
        else:
            print(f"{user_choice} is invalid. Try again.")

    return category


def main():
    """
    Sews everything together.
    Runs the game, and repeats once completed.
    """
    global category

    # have the user select a category first
    category = choose_category()

    # pick a random word from selected category
    word = get_word(category)

    # play the game with the new word
    play(word)

    # creates the option to play again as long as
    # the user chooses yes to play again
    while True:
        again = input("Play Again? (Y/N) ").upper()
        clear()
        if again == "Y":
            category = choose_category()
            word = get_word(category)
            play(word)
        elif again == "N":
            print("Thanks for playing hangman!")
            break
        else:
            print(f"{again} is invalid. Try again.")


# run the main python application (play.py)
if __name__ == "__main__":
    clear()
    welcome()
    main()
    choose_category()
